import os
import pandas as pd
import datetime

# Supõe que DATA_SEGUNDA_FEIRA é uma variável previamente definida que contém uma data.
DATA_SEGUNDA_FEIRA = datetime.datetime.now()  # exemplo, ajuste conforme sua necessidade
output_path = "/caminho/para/seu/diretorio"  # ajuste conforme sua necessidade

date_str = DATA_SEGUNDA_FEIRA.strftime("%Y-%m-%d")
filename_xls = f"{date_str}_onhand_inquiry.xls"
filename_csv = f"{date_str}_onhand_inquiry.csv"
filepath_xls = os.path.join(output_path, filename_xls)
filepath_csv = os.path.join(output_path, filename_csv)

# Aqui você deverá simular a criação de um arquivo Excel para este exemplo funcionar
# Neste exemplo, assumimos que o arquivo .xls já existe.

# Converter de Excel (.xls) para CSV
def convert_excel_to_csv(filepath_xls, filepath_csv):
    df = pd.read_excel(filepath_xls)  # Lê o arquivo Excel
    df.to_csv(filepath_csv, index=False)  # Salva como CSV

# Chamando a função de conversão
convert_excel_to_csv(filepath_xls, filepath_csv)

# Supondo que você esteja usando `bot.kb_type` para digitar o caminho do arquivo convertido
bot.kb_type(filepath_csv)
