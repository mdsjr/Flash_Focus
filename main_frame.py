# main_frame.py
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import customtkinter
from text_processor import TextProcessor
from quiz_generator import QuizGenerator

class MainFrame(customtkinter.CTkFrame):
    def __init__(self, parent, ajustar_velocidade_callback, gerar_pergunta_callback):
        super().__init__(parent, fg_color="#0f1924")
        self.ajustar_velocidade_callback = ajustar_velocidade_callback
        self.gerar_pergunta_callback = gerar_pergunta_callback

        # Frame para botões de menu no topo esquerdo
        self.menu_frame = customtkinter.CTkFrame(self, fg_color="#0f1924")
        self.menu_frame.pack(side="top", anchor="nw", padx=10, pady=5)

        self.btn_progresso_menu = customtkinter.CTkButton(self.menu_frame, text="Progresso",
                                                          command=lambda: parent.show_frame("progress"),
                                                          fg_color="#155b74")
        self.btn_progresso_menu.pack(pady=5)

        self.btn_perfil_menu = customtkinter.CTkButton(self.menu_frame, text="Perfil",
                                                       command=lambda: parent.show_frame("profile"),
                                                       fg_color="#155b74")
        self.btn_perfil_menu.pack(pady=5)

        self.img_logo = Image.open("assets/icon.png")
        self.img_logo = ImageTk.PhotoImage(self.img_logo)
        self.logo_label = tk.Label(self, image=self.img_logo, bg="#0f1924")
        self.logo_label.pack(pady=10)

        self.label_palavra = tk.Text(self, height=1.5, font=("Helvetica", 30))
        self.label_palavra.pack(pady=40, padx=200)
        self.label_palavra.tag_configure("central", font=("Helvetica", 36, "bold"), foreground="red")
        self.label_palavra.tag_configure("center", justify='center')
        self.label_palavra.configure(bg="#0f1924", fg="white")

        self.caixa_texto = tk.Text(self, height=10, width=30)
        self.caixa_texto.insert(tk.END, "Você pode ler mais rápido do que imagina!")
        self.caixa_texto.pack()

        self.slider_velocidade = customtkinter.CTkSlider(self, from_=100, to=900, command=self.ajustar_velocidade_callback)
        self.slider_velocidade.set(700)
        self.slider_velocidade.pack(pady=10)

        self.frame_botoes = customtkinter.CTkFrame(self, fg_color="#0f1924")
        self.frame_botoes.pack(pady=10)

        self.text_processor = TextProcessor(self.label_palavra, self.caixa_texto)
        self.quiz_generator = QuizGenerator()

        self.botao_iniciar = customtkinter.CTkButton(self.frame_botoes, text="Iniciar",
                                                     command=lambda: self.text_processor.iniciar(parent.update, parent.current_user),
                                                     fg_color="#155b74")
        self.botao_iniciar.grid(row=0, column=0, padx=5)

        self.botao_pausar = customtkinter.CTkButton(self.frame_botoes, text="Pausar",
                                                    command=self.text_processor.pausar,
                                                    fg_color="#155b74")
        self.botao_pausar.grid(row=0, column=1, padx=5)

        self.botao_continuar = customtkinter.CTkButton(self.frame_botoes, text="Continuar",
                                                       command=lambda: self.text_processor.continuar(parent.update, parent.current_user),
                                                       fg_color="#155b74")
        self.botao_continuar.grid(row=0, column=2, padx=5)

        self.botao_pergunta = customtkinter.CTkButton(self.frame_botoes, text="Gerar Pergunta",
                                                      command=self.gerar_pergunta,
                                                      fg_color="#155b74")
        self.botao_pergunta.grid(row=0, column=3, padx=5)

        self.label_pergunta = customtkinter.CTkLabel(self, text="", font=("Helvetica", 20), text_color="yellow")
        self.label_pergunta.pack(pady=10)

        self.radio_var = tk.StringVar(value="")
        self.radio_buttons = []
        for i in range(3):
            rb = customtkinter.CTkRadioButton(self, text="", variable=self.radio_var, value=str(i), text_color="white")
            self.radio_buttons.append(rb)

        self.botao_verificar = customtkinter.CTkButton(self, text="Verificar Resposta",
                                                       command=lambda: self.verificar_resposta(parent.current_user),
                                                       fg_color="#155b74")
        self.botao_verificar.pack(pady=10)
        self.botao_verificar.pack_forget()

    def gerar_pergunta(self):
        texto = self.caixa_texto.get("1.0", tk.END).strip()
        pergunta, alternativas, correta = self.quiz_generator.gerar_pergunta(texto)
        if not pergunta:
            self.label_pergunta.configure(text="Digite um texto primeiro!")
            return
        self.resposta_correta = correta
        self.label_pergunta.configure(text=pergunta)
        for i, (rb, alt) in enumerate(zip(self.radio_buttons, alternativas)):
            rb.configure(text=alt)
            rb.pack(pady=5)
        self.botao_verificar.pack()

    def verificar_resposta(self, user):
        escolha = self.radio_var.get()
        if not escolha:
            self.label_pergunta.configure(text="Selecione uma alternativa!")
            return
        if self.radio_buttons[int(escolha)].cget("text").startswith(self.resposta_correta):
            self.label_pergunta.configure(text="Correto!")
            user["progresso"]["perguntas_acertadas"] += 1
        else:
            self.label_pergunta.configure(text=f"Errado! A resposta correta era {self.resposta_correta}")
        # Salvar o progresso no users.json
        self.master.save_progress()  # Chama o método do gui.py para salvar