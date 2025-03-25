import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import zipfile

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
zip_filename = 'arquivos.zip'
arrLinks = []

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
linksHTML = soup.find_all('a', class_ = "internal-link")


for link in linksHTML:
    if "Anexo I" in link.get_text():
        arrLinks.append(link['href'])

arrLinks = list(filter(lambda item: ".xlsx" not in item, arrLinks))

for i, pdf in enumerate(arrLinks):
  urlretrieve(pdf, f"anexo_{str(i + 1)}.pdf")
  print(f"Baixado: anexo_{str(i + 1)}.pdf")


with zipfile.ZipFile(zip_filename, 'w') as zipf:
  for i, pdf in enumerate(arrLinks):
    zipf.write(f"anexo_{str(i + 1)}.pdf")
    print(f"anexo_{str(i + 1)}.pdf adicionado ao {zip_filename}")
