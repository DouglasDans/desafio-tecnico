from sqlalchemy import create_engine, text

from typing import Union
from fastapi import FastAPI

engine = create_engine("mysql+pymysql://root:password@0.0.0.0:3306/yourdb")



app = FastAPI()

@app.get("/operadoras")
def read_root():
  with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM TB_OPERADORAS LIMIT 10"))
    operadoras = []

    for row in result:
      operadoras.append(row._asdict())
    
    return operadoras 