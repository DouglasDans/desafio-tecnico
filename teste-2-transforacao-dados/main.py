import zipfile
import pdfplumber
import pandas as pd
from io import BytesIO

zip_path = "../teste-1-web-scrapping/arquivos.zip"
pdf_filename = "anexo_1.pdf"
csv_output = "saida.csv"
zip_filename = "Teste_douglas.zip"
expected_columns = 13

print(f"Iniciando...")

with zipfile.ZipFile(zip_path, 'r') as zip:
  print(f"Carregado zip {zip_path}")
  with zip.open(pdf_filename) as pdf_file:
    pdf_data = BytesIO(pdf_file.read())
    print(f"Carregado pdf file {pdf_filename}")

    with pdfplumber.open(pdf_data) as pdf:
      all_tables = []
      print("Varrendo PDF...")

      for page_num in range(2, len(pdf.pages)) :
        page = pdf.pages[page_num]

        tables = page.extract_table()

        if tables: 
          clean_table = []

          for row in tables:
            cleaned_row = [cell.replace("\n", " ").strip() if cell else "" for cell in row]

            if expected_columns is None:
                expected_columns = len(cleaned_row)

            if len(cleaned_row) < expected_columns:
                cleaned_row.extend([""] * (expected_columns - len(cleaned_row)))

            elif len(cleaned_row) > expected_columns:
                cleaned_row = cleaned_row[:expected_columns]

            cleaned_row = [cell.replace("OD", "Seg. Odontológica").strip() for cell in cleaned_row]
            cleaned_row = [cell.replace("AMB", "Seg. Ambulatorial").strip() for cell in cleaned_row]

            clean_table.append(cleaned_row)

          all_tables.extend(clean_table)
      
      print("Varredura completa")

      if all_tables:
          df = pd.DataFrame(all_tables[1:], columns=all_tables[0])
          df.to_csv(csv_output, index=False, encoding="utf-8")
          print(f"CSV salvo como {csv_output}")
      else:
          print("Nenhuma tabela encontrada a partir da segunda página.")

with zipfile.ZipFile(zip_filename, 'w') as zipf:
    zipf.write(csv_output)
    print(f"{csv_output} adicionado ao {zip_filename}")
        