import os
from datetime import datetime, timedelta

def nomear_arquivo_para_segunda_feira():
    # Obter data atual
    data_atual = datetime.now()

    # Encontrar a data da última segunda-feira
    dias_para_segunda = (data_atual.weekday() - 1) % 7  # Se hoje é segunda-feira, será 0
    data_segunda_feira = data_atual - timedelta(days=dias_para_segunda)

    # Formatar a data da última segunda-feira para usar no nome do arquivo
    nome_arquivo = data_segunda_feira.strftime("%Y-%m-%d") + ".xls"

    # Caminho para a pasta onde deseja salvar o arquivo
    pasta_destino = "/caminho/para/sua/pasta"  # Substitua pelo caminho correto

    # Renomear o arquivo
    arquivo_atual = "arquivo.xls"  # Nome do arquivo que você baixou
    caminho_atual = os.path.join(pasta_destino, arquivo_atual)
    caminho_novo = os.path.join(pasta_destino, nome_arquivo)
    os.rename(caminho_atual, caminho_novo)

nomear_arquivo_para_segunda_feira()
