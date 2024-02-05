import os
from datetime import datetime, timedelta

def nomear_arquivo_para_segunda_feira(data):
    # Obter data atual
    data_atual = datetime.now()

    # Verificar se hoje é segunda-feira, se não for, encontrar a próxima segunda-feira
    if data_atual.weekday() != 0:  # 0 é segunda-feira
        dias_para_segunda = (7 - data_atual.weekday()) % 7
        data_atual += timedelta(days=dias_para_segunda)

    # Formatar a data para usar no nome do arquivo
    nome_arquivo = data_atual.strftime("%Y-%m-%d") + ".xls"

    # Caminho para a pasta onde deseja salvar o arquivo
    pasta_destino = "destino"  # Substitua pelo caminho correto

    # Renomear o arquivo
    arquivo_atual = r"C:\Users\paulo\Desktop\rpa\arquivo\Ficha Cadastral Pessoa Física (Bolsista).xls"  # Nome do arquivo que você baixou
    caminho_atual = os.path.join(pasta_destino, arquivo_atual)
    caminho_novo = os.path.join(pasta_destino, nome_arquivo)
    os.rename(caminho_atual, caminho_novo)

# nomear_arquivo_para_segunda_feira()
    
# Testando para a próxima semana
data_atual = datetime.now()
data_proxima_semana = data_atual + timedelta(weeks=1)
print("Data próxima semana:", data_proxima_semana)
nomear_arquivo_para_segunda_feira(data_proxima_semana)
