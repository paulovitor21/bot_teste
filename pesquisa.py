from botcity.web import WebBot, Browser, By

def inbox_email(webbot, employee_user, search_query):
    webbot.navigate_to("http://geusazns51.lge.com/mail8/(J.nsf/MBeFirstFrame?ReadForm".format(employee_user))
    file_list = 'all'
    webbot.wait(4000)
    information = {}
    i = 1

    while True:  # Executa indefinidamente até uma condição de parada
        iframe = webbot.find_element("Main", By.Name)
        webbot.enter_iframe(iframe)
        webbot.wait(500)
        webbot.find_element('id_search_field_UI_INSTANCE_171', By.ID).send_keys(search_query)
        webbot.enter()
        webbot.wait(4000)

        email = webbot.find_element('cls_list_new_document', By.CLASS_NAME)

        while email is not None:
            information[str(i)] = {}
            email.click()
            webbot.wait(3000)

            iframe = webbot.find_element("id_tab_mng_iframe_UI_INSTANCE_171", By.ID)
            webbot.enter_iframe(iframe)
            iframe = webbot.find_element('docWinContent', By.ID)
            webbot.enter_iframe(iframe)
            webbot.wait(2000)
            webbot.find_element("files_list", By.ID).click()
            webbot.wait(1000)
            list1 = webbot.find_elements('chk_list_item', By.CLASS_NAME)

            for j in range(len(list1)):
                if file_list == 'all':
                    list1[j].find_element_by_class_name('attach_filename').click()
                    webbot.wait(5000)

            # Após processar um email, volta para a caixa de entrada
            webbot.go_back()
            webbot.go_back()
            webbot.go_back()
            webbot.wait(3000)
            
            email = webbot.find_element('cls_list_new_document', By.CLASS_NAME)

        if not email:
            print("Não tem mais emails com este termo de busca.")
            break  # Sai do loop quando não há mais emails

        # Aqui você pode definir um novo termo de pesquisa
        novo_termo_de_pesquisa = "novo termo"
        search_query = novo_termo_de_pesquisa
