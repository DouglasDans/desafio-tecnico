from sqlalchemy import create_engine, text
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

engine = create_engine("mysql+pymysql://root:password@0.0.0.0:3306/yourdb")

app = FastAPI()

# Add CORS middleware to allow all origins
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],  # Allow all origins
  allow_credentials=True,
  allow_methods=["*"],  # Allow all methods
  allow_headers=["*"],  # Allow all headers
)

@app.get("/operadoras")
def read_root():
  with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM TB_OPERADORAS LIMIT 10"))
    operadoras = []

    for row in result:
      operadoras.append(row._asdict())
    
    return operadoras