import os
class Config: # Classe para armazenar as configurações do programa
    API_KEY = os.environ.get("API_KEY") # Chave de API da OpenAI
    DEFAULT_TEXT = "Você pode ler mais rápido do que imagina!" # Texto padrão exibido na caixa de texto
    BG_COLOR = "#0f1924" # Cor de fundo da janela
    BUTTON_COLOR = "#155b74" # Cor dos botões