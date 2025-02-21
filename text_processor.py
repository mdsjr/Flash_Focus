import time
import tkinter as tk

class TextProcessor:
    def __init__(self, label_palavra, caixa_texto):
        self.label_palavra = label_palavra
        self.caixa_texto = caixa_texto
        self.executando = False
        self.indice_atual = 0
        self.velocidade = 0.3

    def encontrar_letra_central(self, palavra):
        tamanho = len(palavra)
        if tamanho == 0:
            return ""
        return palavra[tamanho // 2]

    def exibir_palavras(self, update_callback):
        texto = self.caixa_texto.get("1.0", tk.END).strip()
        palavras = texto.split()

        while self.executando and self.indice_atual < len(palavras):
            palavra = palavras[self.indice_atual]
            letra_central = self.encontrar_letra_central(palavra)
            indice_meio = len(palavra) // 2

            parte1 = palavra[:indice_meio]
            parte2 = palavra[indice_meio + 1:]

            self.label_palavra.delete("1.0", tk.END)
            self.label_palavra.insert(tk.END, parte1, "center")
            self.label_palavra.insert(tk.END, letra_central, "central center")
            self.label_palavra.insert(tk.END, parte2, "center")

            update_callback()  # Chama a função de atualização da GUI
            time.sleep(self.velocidade)
            self.indice_atual += 1

    def iniciar(self, update_callback):
        self.executando = True
        self.indice_atual = 0
        self.exibir_palavras(update_callback)

    def pausar(self):
        self.executando = False

    def continuar(self, update_callback):
        self.executando = True
        self.exibir_palavras(update_callback)

    def ajustar_velocidade(self, value):
        self.velocidade = 1 - (float(value) - 100) / 900