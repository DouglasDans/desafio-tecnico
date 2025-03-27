import pandas as pd
from sqlalchemy import create_engine, text
import os

operadoras_csv_to_sql = {
  "Registro_ANS": "REGISTRO_OPERADORA",
  "CNPJ": "CNPJ",
  "Razao_Social": "RAZAO_SOCIAL",
  "Nome_Fantasia": "NOME_FANTASIA",
  "Modalidade": "MODALIDADE",
  "Logradouro": "LOGRADOURO",
  "Numero": "NUMERO",
  "Complemento": "COMPLEMENTO",
  "Bairro": "BAIRRO",
  "Cidade": "CIDADE",
  "UF": "UF",
  "CEP": "CEP",
  "DDD": "DDD",
  "Fax": "FAX",
  "Telefone": "TELEFONE",
  "Endereco_eletronico": "EMAIL",
  "Representante": "REPRESENTANTE",
  "Cargo_Representante": "CARGO_REPRESENTANTE",
  "Regiao_de_Comercializacao": "REGIAO_COMERCIALIZACAO",
  "Data_Registro_ANS": "DATA_REGISTRO_ANS"
}

contabil_csv_to_sql = {
  "REG_ANS": "REGISTRO_OPERADORA",
  "CD_CONTA_CONTABIL": "COD_CONTA_CONTABIL",
  "DATA": "DATA_CONTABIL",
  "DESCRICAO": "DESCRICAO",
  "VL_SALDO_INICIAL": "VALOR_SALDO_INICIAL",
  "VL_SALDO_FINAL": "VALOR_SALDO_FINAL"
}

engine = create_engine("mysql+pymysql://root:password@0.0.0.0:3306/yourdb")

with engine.connect() as connection:
  result = connection.execute(text("SELECT 1"))
  print("Conexão bem-sucedida com o banco de dados!", result.fetchone())

  # Check if any tables exist
  existing_tables = connection.execute(text("SHOW TABLES")).fetchall()
  
  if not existing_tables:
    print("Banco de dados vazio. Criando tabelas...")
    with open("schema.sql", "r") as file:
      ddl_script = file.read()
      
      for statement in ddl_script.split(";"):
        if statement.strip():
          connection.execute(text(statement))
      connection.commit()
    print("Tabelas criadas com sucesso!")
  else:
    print("O banco de dados já contém tabelas. Esquema não aplicado.")


print("Aplicando dados da tabela TB_OPERADORAS")
df = pd.read_csv("Relatorio_cadop.csv", delimiter=";")
df.rename(columns=operadoras_csv_to_sql, inplace=True)

df.to_sql("TB_OPERADORAS", con=engine, if_exists="append", index=False)

print("Aplicando dados da tabela TB_CONTA_CONTABIL")
caminho_dos_csvs = "./data"
arquivos_csv = [f for f in os.listdir(caminho_dos_csvs) if f.endswith(".csv")]

CHUNKSIZE = 10_000  # Define um tamanho de lote (10 mil linhas por vez)

for arquivo in arquivos_csv:
    caminho_completo = os.path.join(caminho_dos_csvs, arquivo)
    
    print(f"Lendo e inserindo arquivo: {arquivo}...")

    try:
        for chunk in pd.read_csv(caminho_completo, delimiter=";", chunksize=CHUNKSIZE):
          chunk.rename(columns=contabil_csv_to_sql, inplace=True)
          colunas_numericas = ["VALOR_SALDO_INICIAL", "VALOR_SALDO_FINAL", "OUTRA_COLUNA_NUMERICA"]  

          for col in colunas_numericas:
              if col in chunk.columns:
                  chunk[col] = chunk[col].str.replace(",", ".", regex=False)
                  chunk[col] = pd.to_numeric(chunk[col], errors="coerce")
          chunk.to_sql("TB_CONTA_CONTABIL", con=engine, if_exists="append", index=False)
        
        print(f"Arquivo {arquivo} inserido com sucesso!")

    except Exception as e:
        print(f"Erro ao processar {arquivo}: {e}")