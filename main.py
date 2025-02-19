import time
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk


class FlashFocus:
    def __init__(self):
        self.executando = False
        self.indice_atual = 0
        self.velocidade = 0.3

        self.window = ThemedTk(theme="equilux")
        self.window.title("Flash Focus")
        self.window.state("zoomed")

        self.window.configure(bg="#444444")

        self.label_palavra = tk.Text(self.window, height=2, font=("Helvetica", 24))
        self.label_palavra.pack(pady=20)
        self.label_palavra.tag_configure("central", font=("Helvetica", 24, "bold"), foreground="red")
        self.label_palavra.tag_configure("center", justify='center')

        self.caixa_texto = tk.Text(self.window, height=10, width=30)
        self.caixa_texto.insert(tk.END, "Você pode ler mais rápido do que imagina!")
        self.caixa_texto.pack()

        self.slider_velocidade = ttk.Scale(self.window, from_=100, to=900, orient=tk.HORIZONTAL,
                                           command=self.ajustar_velocidade)
        self.slider_velocidade.set(700)
        self.slider_velocidade.pack(pady=10)

        self.frame_botoes = ttk.Frame(self.window)
        self.frame_botoes.pack(pady=10)

        self.botao_iniciar = ttk.Button(self.frame_botoes, text="Iniciar", command=self.iniciar)
        self.botao_iniciar.grid(row=0, column=0, padx=5)

        self.botao_pausar = ttk.Button(self.frame_botoes, text="Pausar", command=self.pausar)
        self.botao_pausar.grid(row=0, column=1, padx=5)

        self.botao_continuar = ttk.Button(self.frame_botoes, text="Continuar", command=self.continuar)
        self.botao_continuar.grid(row=0, column=2, padx=5)

        self.window.mainloop()

    def encontrar_letra_central(self, palavra):
        tamanho = len(palavra)
        if tamanho == 0:
            return ""
        return palavra[tamanho // 2]

    def exibir_palavras(self):
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

            self.window.update()
            time.sleep(self.velocidade)
            self.indice_atual += 1

    def iniciar(self):
        self.executando = True
        self.indice_atual = 0
        self.exibir_palavras()

    def pausar(self):
        self.executando = False

    def continuar(self):
        self.executando = True
        self.exibir_palavras()

    def ajustar_velocidade(self, value):
        self.velocidade = 1 - (float(value) - 100) / 900


FlashFocus()
