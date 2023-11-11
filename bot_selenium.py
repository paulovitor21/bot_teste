from selenium import webdriver
from selenium.webdriver.ie.options import Options as IeOptions

# Caminho para o driver do Internet Explorer (IEDriverServer.exe)
msedge_driver_path = 'IEDriverServer.exe'

# Configuração do Internet Explorer Options
ie_options = IeOptions()
ie_options.add_argument("--ie=edge")  # Configura o modo de compatibilidade com o Edge
ie_options.add_argument("--silent")   # Adiciona o argumento para evitar avisos

# Cria uma instância do WebDriver do Internet Explorer
driver = webdriver.Ie(executable_path=msedge_driver_path, options=ie_options)

# Exemplo de uso: abrindo uma página
driver.get("https://learn.microsoft.com/pt-br/microsoft-edge/devtools-guide-chromium/ie-mode/")

# Restante do seu código...

# Fecha o navegador
#driver.quit()

#link de como inspecionar pagina no modo IE do edge: https://learn.microsoft.com/pt-br/microsoft-edge/devtools-guide-chromium/ie-mode/
