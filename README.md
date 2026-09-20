# Stock Alert API — PoC de Análıse de Estoque

Microprojeto em Python para análıse de estoque e geraça͂o de alertas de reposiça͂o, desenvolvido como **Prova de Conceito (PoC)** para validar uma hipótese técnica em pequena escala, com escopo limitado, antes de investir na integraça͂o completa ao ERP principal. Eu fiz uma cópia parcial, pois o arquivo original está no modo private.

> **Status:** Funcionalidades em Python ainda em desenvolvimento.  
> Este projeto está na fila de prioridades de evoluça͂o do ERP, em fase inicial de validac̃a͂o técnica.

## Objetivo da PoC

Demonstrar, de forma prática e objetiva, que é possível:

- Ler dados de produtos a partir de um arquivo CSV;
- Aplicar regras de negócio para identificar produtos abaixo do estoque mínimo;
- Calcular valores de reposiça͂o e estoque parado;
- Gerar um resumo estruturado em JSON;
- Expor esses dados por meio de uma API REST simples.

A PoC serve para validar a viabilidade técnica da análıse automatizada de estoque antes de integrar ao sistema principal, reduzindo riscos e permitindo ajustes de escopo com baixo custo.

## Por Que Este Projeto Está Separado?

Este repositóĺıı́o foi mantido em um projeto **separado e independente** do ERP principal por dois motivos:

1. **Proteça͂o de dados sensíveis:** o código e os dados deste projeto são fictı́cios e não contem informaço͂es reais de clientes, fornecedores, precos ou operac̃o͂es do negócio. Isso evita expor dados confidenciais em ambientes de teste e desenvolvimento. Eu fiz uma cópia parcial, pois o arquivo original está no modo private.
2. **Foco na validaça͂o técnica:** manter a PoC isolada permite iterar rapidamente, testar hipóteses e ajustar o escopo sem impactar a base de código do ERP, que segue outro ciclo de prioridades e governança.

## Estrutura do Projeto

```
stock_alert_api/
├─ data/
│  └─ produtos.csv          # base de produtos fictícios (loja de artigos esportivos)
├─ src/
│  └─ analyzer.py           # script de análıse: leitura, regras de negócio, geraça͂o do JSON
├─ api/
│  └─ app.py                # API FastAPI que expoe os resultados
├─ reports/
│  └─ resumo_estoque.json   # saída da análıse
├─ requirements.txt         # dependencias Python
└─ README.md                # este arquivo
```

## Regras de Negócio

- **Produto em risco:** `estoque_atual < estoque_minimo`
- **Quantidade para reposiça͂o:** `max(0, estoque_minimo - estoque_atual)`
- **Valor para reposiça͂o:** `qtd_reposicao * custo_unitario`
- **Valor parado em estoque:** `estoque_atual * custo_unitario`
- **Agrupamentos:** por categoria e por fornecedor (total parado, total a repor, itens em risco)

## Como Rodar

### 1. Instalar dependencias

```bash
python -m pip install -r requirements.txt
```

### 2. Gerar o relatório

```bash
python src/analyzer.py
```

Saíııda: `reports/resumo_estoque.json`

### 3. Rodar a API

```bash
python -m uvicorn api.app:app --reload
```

### 4. Acessar os endpoints

- http://127.0.0.1:8000/ — mensagem de boas-vindas
- http://127.0.0.1:8000/resumo — resumo completo
- http://127.0.0.1:8000/riscos — lista de produtos em risco
- http://127.0.0.1:8000/parado — valor total parado em estoque
- http://127.0.0.1:8000/categorias — agrupamento por categoria
- http://127.0.0.1:8000/fornecedores — agrupamento por fornecedor

## Exemplo de Saída (trecho)

```json
{
  "resumo_geral": {
    "total_parado": 12345.67,
    "total_a_repor": 789.10,
    "itens_em_risco": 6
  },
  "produtos_em_risco": [
    {
      "sku": "P001",
      "nome": "Chuteira Mercurial Vapor 17",
      "categoria": "Chuteira Campo",
      "estoque_atual": 3,
      "estoque_minimo": 1,
      "qtd_reposicao": 0,
      "valor_reposicao": 0.0
    }
  ],
  "por_categoria": [...],
  "por_fornecedor": [...]
}
```

## Próximos Passos (Fila de Prioridades do ERP)

Esta parte do projeto está em fase inicial e as funcionalidades em Python sera͂o evoluı́das conforme a fila de prioridades do ERP principal. Possı́veis melhorias futuras:

- Agendamento de análıses (cron ou task scheduler);
- Exportaça͂o de relatórios em PDF/Excel;
- Integraça͂o com o módulo de estoque do ERP.

## Sobre Este README

Este README foi elaborado com auxílıo de inteligência artificial para acelerar a documentaça͂o, mantendo o foco na clareza e objetividade das informaço͂es técnicas.

## Licenca

Projeto desenvolvido para fins de estudo e validaça͂o técnica.