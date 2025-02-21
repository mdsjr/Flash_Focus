import time
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import customtkinter

class FlashFocus(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.executando = False
        self.indice_atual = 0
        self.velocidade = 0.3

        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("dark-blue")

        self.title("Flash Focus")
        self.state("zoomed")
        try:
            self.iconbitmap("assets/icon.ico")  # Certifique-se de que o arquivo existe
        except:
            print("Ícone não encontrado, continuando sem ícone.")
        self.configure(fg_color="#0f1924")  # Usar fg_color em vez de bg no customtkinter

        # Carregar e exibir a imagem
        self.img_logo = Image.open("assets/icon.png")
        self.img_logo = ImageTk.PhotoImage(self.img_logo)
        self.logo_label = tk.Label(self, image=self.img_logo, bg="#0f1924")
        self.logo_label.pack(pady=20)

        # 🔹 Criar a área de exibição da palavra
        self.label_palavra = tk.Text(self, height=1.5, font=("Helvetica", 30))
        self.label_palavra.pack(pady=75, padx=200)
        self.label_palavra.tag_configure("central", font=("Helvetica", 36, "bold"), foreground="red")
        self.label_palavra.tag_configure("center", justify='center')
        self.label_palavra.configure(bg="#0f1924", fg="white")

        # 🔹 Caixa de texto de entrada
        self.caixa_texto = tk.Text(self, height=10, width=30)
        self.caixa_texto.insert(tk.END, "Você pode ler mais rápido do que imagina!")
        self.caixa_texto.pack()

        # 🔹 Slider de velocidade
        self.slider_velocidade = customtkinter.CTkSlider(
            self, from_=100, to=900, command=self.ajustar_velocidade
        )
        self.slider_velocidade.set(700)
        self.slider_velocidade.pack(pady=10)

        # 🔹 Frame para botões
        self.frame_botoes = customtkinter.CTkFrame(self, fg_color="#0f1924")
        self.frame_botoes.pack(pady=10)

        # 🔹 Botões de controle
        self.botao_iniciar = customtkinter.CTkButton(self.frame_botoes, text="Iniciar", command=self.iniciar, fg_color="#155b74")
        self.botao_iniciar.grid(row=0, column=0, padx=5)

        self.botao_pausar = customtkinter.CTkButton(self.frame_botoes, text="Pausar", command=self.pausar, fg_color="#155b74")
        self.botao_pausar.grid(row=0, column=1, padx=5)

        self.botao_continuar = customtkinter.CTkButton(self.frame_botoes, text="Continuar", command=self.continuar, fg_color="#155b74")
        self.botao_continuar.grid(row=0, column=2, padx=5)

        self.mainloop()

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

            self.update()
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

if __name__ == "__main__":
    FlashFocus()