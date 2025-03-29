### Desafio Técnico Intuitive Care
Desafio técnico realizado conforme oo que foi pedido previamente.

Vou indicar aqui como executar cada um dos testes e como foi realizado cada um deles


### Observação
**Necessário Python e Node e Postgres Intalados para execução.**

Cada um dos projetos devem ser executados sequencialmente.

---

Para testes em Linux é necessário fazer as seguintes etapas para execução de cara um dos testes em python.

```sh
python3 -m venv venv 

source venv/bin/activate
```

### Teste 1 - Web Scrapping
Utilizei as libs BeautifulSoup e requests para realizar o web scrapping e fazer download dos pdfs solicitados.


**Para executar o projeto**
```sh
pip install -r requirements.txt

python main.py
```

### Teste 2 - Transoformação dos dados
Utilizei as libs pandas e pdfplumber para conversão das tabelas do PDF em CSV.

**Para executar o projeto**
```sh
pip install -r requirements.txt

python main.py
```

### Teste 3 - Transformação do CSV em banco de dados
Utilizei as libs sqlalchemy e pandas para a transformação dos dados para o SQL.

**Para executar o projeto**
```sh
# Para execução do Postgres eu já deixei um banco de dados configurado para utilizar com Docker
docker compose up --build

pip install -r requirements.txt

# Criação do Banco e importação dos dados
python main.py

# Consulta dos dados
python queries.py
```

### Teste 4 API e Interface em VueJS
Utilizei as libs sqlalquemy e fastapi em python para a criação da API e consultar os dados no banco de dados.

Utilizei VueJS em Typescript para execução da interface de usuário.

Exportei a coleção Postman como JSON.

**Para executar o projeto**
```sh
# Backend
pip install -r requirements.txt
fastapi dev main.py

#Frontend
cd vue-ui
npm install
npm run dev
```

Os serviços podem ser acessados pelas URLs:
- API Backend: http://localhost:8000
- UI Frontend: http://localhost:5173