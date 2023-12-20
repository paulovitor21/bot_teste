import os
import pyautogui
from datetime import datetime

# Obtém o caminho da pasta "Downloads"
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

# Gera um nome de arquivo baseado na data e hora atual
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
file_name = f'screenshot_{timestamp}.png'

# Tira um print da tela inteira
screenshot = pyautogui.screenshot()

# Salva o print na pasta Downloads com o nome dinâmico
screenshot_path = os.path.join(downloads_folder, file_name)
screenshot.save(screenshot_path)
