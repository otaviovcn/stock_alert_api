import pandas as pd
import json
from pathlib import Path

def analisar_estoque(csv_path: str, output_path: str):
    """
    Lê o CSV de produtos, aplica regras de negócio e gera um resumo em JSON.
    Regras:
      - Produto em risco: estoque_atual < estoque_minimo
      - qtd_reposicao = max(0, estoque_minimo - estoque_atual)
      - valor_reposicao = qtd_reposicao * custo_unitario
      - valor_parado = estoque_atual * custo_unitario
    """
    df = pd.read_csv(csv_path)

    df["em_risco"] = df["estoque_atual"] < df["estoque_minimo"]
    df["qtd_reposicao"] = (df["estoque_minimo"] - df["estoque_atual"]).clip(lower=0)
    df["valor_reposicao"] = df["qtd_reposicao"] * df["custo_unitario"]
    df["valor_parado"] = df["estoque_atual"] * df["custo_unitario"]

    resumo_geral = {
        "total_parado": float(df["valor_parado"].sum()),
        "total_a_repor": float(df["valor_reposicao"].sum()),
        "itens_em_risco": int(df["em_risco"].sum()),
    }

    produtos_em_risco = (
        df[df["em_risco"]]
        .loc[:, ["sku","nome","categoria","estoque_atual","estoque_minimo","qtd_reposicao","valor_reposicao"]]
        .to_dict(orient="records")
    )

    por_categoria = (
        df.groupby("categoria")
        .agg(
            total_parado=("valor_parado","sum"),
            total_a_repor=("valor_reposicao","sum"),
            itens_em_risco=("em_risco","sum")
        )
        .reset_index()
        .to_dict(orient="records")
    )

    por_fornecedor = (
        df.groupby("fornecedor")
        .agg(
            total_parado=("valor_parado","sum"),
            total_a_repor=("valor_reposicao","sum"),
            itens_em_risco=("em_risco","sum")
        )
        .reset_index()
        .to_dict(orient="records")
    )

    resultado = {
        "resumo_geral": resumo_geral,
        "produtos_em_risco": produtos_em_risco,
        "por_categoria": por_categoria,
        "por_fornecedor": por_fornecedor,
    }

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    analisar_estoque("data/produtos.csv", "reports/resumo_estoque.json")
    print("Relatorio gerado: reports/resumo_estoque.json")