import os
from datetime import datetime, timedelta

def nomear_arquivo_para_segunda_feira(data):
    # Verificar se hoje é segunda-feira, se não for, encontrar a próxima segunda-feira
    if data.weekday() != 0:  # 0 é segunda-feira
        dias_para_segunda = (7 - data.weekday()) % 7
        data += timedelta(days=dias_para_segunda)

    # Formatar a data para usar no nome do arquivo
    nome_arquivo = data.strftime("%Y-%m-%d") + ".xls"

    # Caminho para a pasta onde deseja salvar o arquivo
    pasta_destino = "destino"  # Substitua pelo caminho correto

    # Renomear o arquivo
    arquivo_atual = r"C:\Users\paulo\Desktop\rpa\arquivo\Ficha Cadastral Pessoa Física (Bolsista).xls"  # Nome do arquivo que você baixou
    caminho_atual = os.path.join(pasta_destino, arquivo_atual)
    caminho_novo = os.path.join(pasta_destino, nome_arquivo)
    os.rename(caminho_atual, caminho_novo)

# Obter data da próxima segunda-feira
data_proxima_semana = datetime.now() + timedelta(weeks=1)
print("Data próxima semana:", data_proxima_semana)

# Chamando a função para renomear o arquivo com a data da próxima semana
nomear_arquivo_para_segunda_feira(data_proxima_semana)
