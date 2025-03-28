import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:password@0.0.0.0:3306/yourdb")

# 🔹 Query para carregar os dados
query = """
SELECT REGISTRO_OPERADORA, DATA_CONTABIL, VALOR_SALDO_FINAL, DESCRICAO
FROM TB_CONTA_CONTABIL
WHERE DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
"""

# 🔹 Carregar os dados em um DataFrame
df = pd.read_sql(query, con=engine)

# 🔹 Converter DATA_CONTABIL para datetime (se necessário)
df["DATA_CONTABIL"] = pd.to_datetime(df["DATA_CONTABIL"], errors="coerce")

# 🔹 Remover possíveis valores nulos em DATA_CONTABIL
df = df.dropna(subset=["DATA_CONTABIL"])

# 🔹 Obter datas de referência
ultimo_trimestre = pd.Timestamp.today() - pd.DateOffset(months=3)
ultimo_ano = pd.Timestamp.today() - pd.DateOffset(years=1)

# 🔹 Filtrar por trimestre e ano
df_trimestre = df[df["DATA_CONTABIL"] >= ultimo_trimestre]
df_ano = df[df["DATA_CONTABIL"] >= ultimo_ano]

# 🔹 Agrupar por operadora e somar despesas
top_10_trimestre = (
    df_trimestre.groupby("REGISTRO_OPERADORA")["VALOR_SALDO_FINAL"]
    .sum()
    .nlargest(10)
    .reset_index()
)

top_10_ano = (
    df_ano.groupby("REGISTRO_OPERADORA")["VALOR_SALDO_FINAL"]
    .sum()
    .nlargest(10)
    .reset_index()
)

# 🔹 Exibir resultados
print("🔹 Top 10 operadoras - Último trimestre")
print(top_10_trimestre)

print("\n🔹 Top 10 operadoras - Último ano")
print(top_10_ano)
