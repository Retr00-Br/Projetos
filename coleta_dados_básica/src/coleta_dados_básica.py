import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de exemplo com TABELA HTML real
url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/"

print("Requisitando página")
response = requests.get(url)

# Verifica se a página respondeu corretamente
if response.status_code != 200:
    raise Exception(f"Erro ao acessar a página: {response.status_code}")

print("Página carregada com sucesso!")

# Parser
soup = BeautifulSoup(response.text, "html.parser")

# Localiza a tabela pelo seletor CSS
tabela_html = soup.find("table")

# Verifica se encontrou tabela
if tabela_html is None:
    raise Exception("Nenhuma tabela encontrada na página.")

# Converte automaticamente com pandas
df = pd.read_html(str(tabela_html))[0]

import os

OUTPUT_PATH = "../data/raw/dados_bancos.csv"

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")

print(f"CSV gerado com sucesso em: {OUTPUT_PATH}")
print("Tabela extraída com sucesso!")
print(df.head())
