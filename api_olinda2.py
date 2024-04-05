import requests
import pandas as pd
import matplotlib.pyplot as plt

# Função para obter os dados da API Olinda do Banco Central
def get_exchange_rate(start_date, end_date):
    url = f'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial=\'{start_date}\'&@dataFinalCotacao=\'{end_date}\'&$format=json'
    response = requests.get(url)
    data = response.json()
    return data['value']

# Consulta dos últimos 6 meses
six_months_ago = pd.Timestamp.now() - pd.DateOffset(months=6)
six_months_data = get_exchange_rate(six_months_ago.strftime('%d-%m-%Y'), pd.Timestamp.now().strftime('%d-%m-%Y'))

# Consulta dos últimos 9 meses
nine_months_ago = pd.Timestamp.now() - pd.DateOffset(months=9)
nine_months_data = get_exchange_rate(nine_months_ago.strftime('%d-%m-%Y'), pd.Timestamp.now().strftime('%d-%m-%Y'))

# Consulta dos últimos 12 meses
twelve_months_ago = pd.Timestamp.now() - pd.DateOffset(months=12)
twelve_months_data = get_exchange_rate(twelve_months_ago.strftime('%d-%m-%Y'), pd.Timestamp.now().strftime('%d-%m-%Y'))

# Organizando os dados em DataFrames
df_six_months = pd.DataFrame(six_months_data)
df_nine_months = pd.DataFrame(nine_months_data)
df_twelve_months = pd.DataFrame(twelve_months_data)

# Plotando os gráficos
plt.figure(figsize=(10, 6))

plt.plot(df_six_months['dataHoraCotacao'], df_six_months['cotacaoCompra'], label='Últimos 6 meses')
plt.plot(df_nine_months['dataHoraCotacao'], df_nine_months['cotacaoCompra'], label='Últimos 9 meses')
plt.plot(df_twelve_months['dataHoraCotacao'], df_twelve_months['cotacaoCompra'], label='Últimos 12 meses')

plt.title('Cotação do dólar nos últimos meses')
plt.xlabel('Data')
plt.ylabel('Cotação de compra')
plt.legend()
plt.grid(True)

plt.show()
