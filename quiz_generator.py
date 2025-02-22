import openai
from config import Config

class QuizGenerator: # Classe para gerar perguntas de múltipla escolha
    def __init__(self):
        self.client = openai.OpenAI(api_key=Config.API_KEY)

    def gerar_pergunta(self, texto): # Metodo para gerar uma pergunta de múltipla escolha
        if not texto:
            return None, None, None

        prompt = f"""
        Baseado no texto abaixo, crie uma pergunta de múltipla escolha com 3 alternativas (a, b, c) sobre a compreensão do texto. 
        Apenas uma alternativa deve ser correta. Retorne no formato:
        Pergunta: [sua pergunta]
        a) [alternativa]
        b) [alternativa]
        c) [alternativa]
        Resposta correta: [letra da alternativa correta]

        Texto: {texto}
        """

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        ) # Chama a API para gerar a pergunta
        resposta = response.choices[0].message.content.strip()

        linhas = resposta.split("\n")
        pergunta = linhas[0].replace("Pergunta: ", "")
        alternativas = [linhas[1], linhas[2], linhas[3]]
        correta = linhas[4].replace("Resposta correta: ", "").split(")")[0]

        return pergunta, alternativas, correta