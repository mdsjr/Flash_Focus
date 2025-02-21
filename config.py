import os
class Config:
    API_KEY = os.environ.get("API_KEY")
    DEFAULT_TEXT = "Você pode ler mais rápido do que imagina!"
    BG_COLOR = "#0f1924"
    BUTTON_COLOR = "#155b74"