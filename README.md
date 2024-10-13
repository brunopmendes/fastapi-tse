# Aplicação FastAPI - Dados de Candidatos do TSE

Esta aplicação web desenvolvida com o framework FastAPI permite buscar e processar dados a partir de arquivos CSV, especificamente os dados disponíveis no sistema de dados abertos do Tribunal Superior Eleitoral (TSE). 

## Dados

Os dados utilizados pela aplicação são provenientes do seguinte dataset do TSE: 

[Resultados 2024 - Boletim de Urna](https://dadosabertos.tse.jus.br/sv/dataset/resultados-2024-boletim-de-urna)

## Funcionalidades

- **Health Check:** Verifica se a aplicação está em funcionamento.
- **Consulta de Candidatos:** Permite consultar candidatos com base no ano da eleição, Unidade Federativa (UF), município e cargo.

## Estrutura do Projeto

```
├── app/
│   ├── main.py          # Ponto de entrada da aplicação FastAPI
│   ├── models/          # Modelos de dados
│   │   └── candidate.py  # Modelo do candidato
│   ├── services/        # Serviços para manipulação de dados
│   │   └── consulta.py   # Funções para ler e processar dados
│   └── data/            # Pasta para armazenar os arquivos CSV
└── requirements.txt      # Dependências do projeto
```

## Endpoints

### 1. Health Check

Verifica o status da aplicação.

- **Endpoint:** `/healthcheck`
- **Método:** `GET`
- **Resposta:** 
```json
{
  "Status": "OK"
}
```

### 2. Consultar Candidatos

Consulta candidatos de acordo com os parâmetros especificados.

- **Endpoint:** `/consultar_candidatos/ano/{ano}/uf/{uf}/municipio/{municipio}/cargo/{cargo}`
- **Método:** `GET`
- **Parâmetros:**
  - `ano`: Ano da eleição (ex: 2024)
  - `uf`: Unidade Federativa (ex: AC)
  - `municipio`: Nome do município (ex: Rio Branco)
  - `cargo`: Cargo (ex: Vereador)

- **Resposta:**
```json
[
  {
    "name": "Nome do Candidato",
    "politicalParty": "Partido do Candidato",
    "electionYear": 2024,
    "municipality": "Nome do Município",
    "position": "Cargo",
    "qttVotes": 12345,
    "uf": "UF"
  },
  ...
]
```

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/brunopmendes/fastapi-tse.git
   cd fastapi-tse
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute a aplicação:
   ```bash
   fastapi dev main.py
   ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
