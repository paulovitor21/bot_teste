from selenium import webdriver
from selenium.webdriver.ie.options import Options as IeOptions

# Caminho para o executável do Microsoft Edge (msedgedriver.exe)
msedge_driver_path = 'IEDriverServer.exe'

# Configuração do Internet Explorer Options
ie_options = IeOptions()
ie_options.add_argument("--ie=edge")  # Configura o modo de compatibilidade com o Edge

# Cria uma instância do WebDriver do Internet Explorer
driver = webdriver.Ie(executable_path=msedge_driver_path, options=ie_options)

# Exemplo de uso: abrindo uma página
driver.get("https://www.google.com")

# Restante do seu código...

# Fecha o navegador
#driver.quit()
