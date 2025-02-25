import os
class Config: # Classe para armazenar as configurações do programa
    API_KEY = os.environ.get("API_KEY") # Chave de API da OpenAI
    DEFAULT_TEXT = "A leitura convencional, aliada ao FlashFocus, pode aprimorar sua capacidade, velocidade e absorção de conteúdo. Para melhores resultados, foque na letra destacada em vermelho e use sua visão periférica para captar o restante de cada palavra. Pratique regularmente e surpreenda-se com seu progresso!" # Texto padrão exibido na caixa de texto
    BG_COLOR = "#0f1924" # Cor de fundo da janela
    BUTTON_COLOR = "#155b74" # Cor dos botões