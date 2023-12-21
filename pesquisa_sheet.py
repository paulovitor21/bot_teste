# Realiza a pesquisa
pesquisa_bem_sucedida = realizar_pesquisa()

if pesquisa_bem_sucedida:
    btn_download = bot.encontrar_botao_download()  # Substitua com sua lógica para encontrar o botão de download

    if btn_download is not None:
        # Clicar no botão de download
        btn_download.click()

        # Esperar pelo download
        bot.wait_for_downloads(220000)

        # Obter o mês atual
        current_month = datetime.now().strftime("%b")

        # Obter o último arquivo criado
        file = bot.get_lasted_created()
    else:
        print("Botão de download não encontrado após a pesquisa.")
else:
    print("A pesquisa não foi bem-sucedida.")
