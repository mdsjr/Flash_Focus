import time
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import customtkinter
import win32gui
import win32con
from config import Config
from text_processor import TextProcessor
from quiz_generator import QuizGenerator

class FlashFocusGUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("system") # Define o modo de aparência do sistema
        customtkinter.set_default_color_theme("dark-blue") # Define o tema de cores padrão

        self.title("Flash Focus") # Define o título da janela
        self.iconbitmap("assets/icon.ico")
        self.configure(fg_color=Config.BG_COLOR)


        self.img_logo = Image.open("assets/icon.png") # Carrega a imagem do logo
        self.img_logo = ImageTk.PhotoImage(self.img_logo)
        self.logo_label = tk.Label(self, image=self.img_logo, bg=Config.BG_COLOR)
        self.logo_label.pack(pady=10)

        self.label_palavra = tk.Text(self, height=1.5, font=("Helvetica", 30)) # Cria um campo de texto para exibir as palavras sendo lidas
        self.label_palavra.pack(pady=40, padx=200)
        self.label_palavra.tag_configure("central", font=("Helvetica", 34, "bold"), foreground="red")
        self.label_palavra.tag_configure("center", justify='center')
        self.label_palavra.configure(bg=Config.BG_COLOR, fg="white")


        self.caixa_texto = tk.Text(self, height=10, width=30) # Cria um campo de texto para que o usuario insira o texto a ser lido
        self.caixa_texto.insert(tk.END, Config.DEFAULT_TEXT)
        self.caixa_texto.pack()


        self.slider_velocidade = customtkinter.CTkSlider(
            self, from_=100, to=900, command=self.ajustar_velocidade
        ) # Cria um slider para ajustar a velocidade de leitura
        self.slider_velocidade.set(700)
        self.slider_velocidade.pack(pady=10)


        self.frame_botoes = customtkinter.CTkFrame(self, fg_color=Config.BG_COLOR) # Cria um frame para os botões
        self.frame_botoes.pack(pady=10)


        self.text_processor = TextProcessor(self.label_palavra, self.caixa_texto) # Cria uma instância da classe TextProcessor


        self.botao_iniciar = customtkinter.CTkButton(self.frame_botoes, text="Iniciar",
                                                     command=lambda: self.text_processor.iniciar(self.update),
                                                     fg_color=Config.BUTTON_COLOR)
        self.botao_iniciar.grid(row=0, column=0, padx=5)

        self.botao_pausar = customtkinter.CTkButton(self.frame_botoes, text="Pausar",
                                                    command=self.text_processor.pausar,
                                                    fg_color=Config.BUTTON_COLOR)
        self.botao_pausar.grid(row=0, column=1, padx=5)

        self.botao_continuar = customtkinter.CTkButton(self.frame_botoes, text="Continuar",
                                                       command=lambda: self.text_processor.continuar(self.update),
                                                       fg_color=Config.BUTTON_COLOR)
        self.botao_continuar.grid(row=0, column=2, padx=5)


        self.quiz_generator = QuizGenerator() # Cria uma instância da classe QuizGenerator
        self.botao_pergunta = customtkinter.CTkButton(self.frame_botoes, text="Gerar Pergunta",
                                                      command=self.gerar_pergunta,
                                                      fg_color=Config.BUTTON_COLOR)
        self.botao_pergunta.grid(row=0, column=3, padx=5)


        self.label_pergunta = customtkinter.CTkLabel(self, text="", font=("Helvetica", 20), text_color="yellow") # Cria um label para exibir a pergunta
        self.label_pergunta.pack(pady=10) # Exibe o label na janela

        self.radio_var = tk.StringVar(value="") # Variável para armazenar a alternativa escolhida
        self.radio_buttons = []
        for i in range(3):
            rb = customtkinter.CTkRadioButton(self, text="", variable=self.radio_var, value=str(i), text_color="white") # Cria um botão de rádio
            self.radio_buttons.append(rb)

        self.botao_verificar = customtkinter.CTkButton(self, text="Verificar Resposta",
                                                       command=self.verificar_resposta,
                                                       fg_color=Config.BUTTON_COLOR)
        self.botao_verificar.pack(pady=10)
        self.botao_verificar.pack_forget()


        self.maximizar_janela() # Maximiza a janela

    def maximizar_janela(self): # Metodo para maximizar a janela
        self.update()
        time.sleep(0.5)  #
        hwnd = self.winfo_id()
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

    def ajustar_velocidade(self, value): # Metodo para ajustar a velocidade de leitura
        self.text_processor.ajustar_velocidade(value)

    def gerar_pergunta(self): # Metodo para gerar uma pergunta
        texto = self.caixa_texto.get("1.0", tk.END).strip()
        pergunta, alternativas, correta = self.quiz_generator.gerar_pergunta(texto)

        if not pergunta: # Verifica se a pergunta foi gerada com sucesso
            self.label_pergunta.configure(text="Digite um texto primeiro!")
            return

        self.resposta_correta = correta # Armazena a resposta correta
        self.label_pergunta.configure(text=pergunta)
        for i, (rb, alt) in enumerate(zip(self.radio_buttons, alternativas)):
            rb.configure(text=alt)
            rb.pack(pady=5)
        self.botao_verificar.pack()

    def verificar_resposta(self): # Metodo para verificar a resposta
        escolha = self.radio_var.get()
        if not escolha:
            self.label_pergunta.configure(text="Selecione uma alternativa!")
            return
        if self.radio_buttons[int(escolha)].cget("text").startswith(self.resposta_correta):
            self.label_pergunta.configure(text="Correto!")
        else:
            self.label_pergunta.configure(text=f"Errado! A resposta correta era {self.resposta_correta})")