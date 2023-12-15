for search_query in search_queries:
        webbot.enter_frame("Main")
        webbot.wait(500)
        webbot.find_element('id_search_field_UI_INSTANCE_171', By.ID).send_keys(search_query)
        webbot.enter()
        webbot.wait(4000)