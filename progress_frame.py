
import tkinter as tk
import customtkinter


class ProgressFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="#0f1924")

        label_title = customtkinter.CTkLabel(self, text="Seu Progresso", font=("Helvetica", 20))
        label_title.pack(pady=20)

        self.progress_resumo = customtkinter.CTkLabel(self, text="", font=("Helvetica", 16), justify="left")
        self.progress_resumo.pack(pady=10)

        label_leituras = customtkinter.CTkLabel(self, text="Histórico de Leituras:", font=("Helvetica", 16))
        label_leituras.pack(pady=10)

        self.progress_leituras = customtkinter.CTkTextbox(self, height=150, width=500, font=("Helvetica", 12))
        self.progress_leituras.pack(pady=10)
        self.progress_leituras.configure(state="disabled")

        btn_voltar = customtkinter.CTkButton(self, text="Voltar", command=lambda: parent.show_frame("main"),
                                             fg_color="#155b74")
        btn_voltar.pack(pady=10)

    def update_progress_display(self, user):
        progresso = user["progresso"]
        resumo = f"Perguntas Acertadas: {progresso['perguntas_acertadas']}\nVelocidade Média: {progresso['velocidade_media']:.2f} segundos por palavra"
        self.progress_resumo.configure(text=resumo)

        leituras_text = ""
        for leitura in progresso["leituras"]:
            leituras_text += f"Data: {leitura['data']}\nTexto: {leitura['texto'][:50]}...\nVelocidade: {leitura['velocidade']}s\n\n"
        if not leituras_text:
            leituras_text = "Nenhuma leitura registrada ainda."

        self.progress_leituras.configure(state="normal")
        self.progress_leituras.delete("1.0", tk.END)
        self.progress_leituras.insert("1.0", leituras_text)
        self.progress_leituras.configure(state="disabled")