import pandas as pd
import matplotlib.pyplot as plt
import os


# Caminhos


RAW_FILE = "../data/raw/dados_bancos.csv"
OUTPUT_DIR = "../data/processed"


# Carga dos dados


print("Carregando dados brutos...")
df = pd.read_csv(RAW_FILE)

print(f"Linhas e colunas: {df.shape}")


# Manutenção / limpeza


print("Padronizando nomes das colunas...")
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("Verificando valores nulos:")
print(df.isnull().sum())


# Analise simples


os.makedirs(OUTPUT_DIR, exist_ok=True)

if "state" in df.columns:
    bancos_por_estado =df["state"].value_counts()

    bancos_por_estado.to_csv(
        f"{OUTPUT_DIR}/bancos_por_estado.csv",
        encoding="utf-8-sig"
    )

    bancos_por_estado.plot(
        kind="bar",
        title="Falência de Bancos por Estado"
    )

    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/bancos_por_estado.png")
    plt.close()


# Finalização


print("Processamento concluído com sucesso!")

