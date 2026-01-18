# Coleta de Dados Básica

Projeto em Python para coleta de dados via requisições HTTP e processamento inicial.
Este projeto realiza a **coleta automática**, **armazenamento** e **análise exploratória** de dados públicos, utilizando Python.

O objetivo é demonstrar um **pipeline completo de dados**, desde o scraping até a geração de arquivos processados e vizualizações.


---

## Tecnologias utilizadas 

- Python 3.12
- Requests
- Beautifulsoup
- Pandas
- Git / GitHub
- LXML
- Matplotlib
- WSL (Linux)

---

# Estrutura do Projeto

coleta_dados_básica/
|---README.md
|---requirements.txt
|---data
| |---raw
| | |---dados_bancos.csv
| |---processed
| |---bancos_por_estados.csv
| |---bancos_por_estados.png
|---src
| |---coleta_dados_básica
| |---explorando_dados.py
|----notebooks

# Informações do Projeto

## Coleta de Dados

O script 'coleta_dados_básica.py':

- Acessa uma pagina pública
- Extrai uma tabela HTML
- Converte os dados para um DataFrame
- Salva os dados brutos em CSV

Sua Saída:

data/raw/dados_bancos.csv

### Analise exploratória

O script 'explorando_dados.py':

- Carrega os dados brutos
- Agrega instuições por estado
- Gera um novo CSV processado
- Cria um gráfico com Matplotlib

Suas Saídas:

data/processed/bancos_por_estado.csv
data/processed/bancos_por_estado.png

# Como executar o projeto

## Criar ambiente virtual

'''bash
python3 -m venv .venv
source .venv/bin/activate

#### Lembre-se de instalar as dependências

pip install -r requirements.txt

### Rodar a coleta

python src/coleta_dados_básica.py

### Rodar a analise

python src/explorando_dados.py
 

---

## Funcionalidades

1. Coleta de dados via HTTP
2. Tratamento e salvamento de dados
3. Organização de dados brutos e processados
4. Preparação para ánalise exploratória em notebooks

---

## Como executar

1. Instale as dependências:
'''bash

pip install -r requeriments.txt
