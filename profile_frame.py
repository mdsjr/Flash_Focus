# profile_frame.py
import tkinter as tk
import customtkinter

class ProfileFrame(customtkinter.CTkFrame):
    def __init__(self, parent, edit_password_callback, logout_callback):
        super().__init__(parent, fg_color="#0f1924")
        self.edit_password_callback = edit_password_callback
        self.logout_callback = logout_callback

        label_title = customtkinter.CTkLabel(self, text="Seu Perfil", font=("Helvetica", 20))
        label_title.pack(pady=20)

        self.profile_info = customtkinter.CTkLabel(self, text="", font=("Helvetica", 16), justify="left")
        self.profile_info.pack(pady=10)

        self.entry_new_password = customtkinter.CTkEntry(self, placeholder_text="Nova Senha", show="*")
        self.entry_new_password.pack(pady=10)

        btn_edit_password = customtkinter.CTkButton(self, text="Alterar Senha", command=self.edit_password, fg_color="#155b74")
        btn_edit_password.pack(pady=5)

        btn_logout = customtkinter.CTkButton(self, text="Logout", command=self.logout, fg_color="#155b74")
        btn_logout.pack(pady=5)

        btn_voltar = customtkinter.CTkButton(self, text="Voltar", command=lambda: parent.show_frame("main"), fg_color="#155b74")
        btn_voltar.pack(pady=5)

    def update_profile_display(self, user, message=None, message_color="white"):
        progresso = user["progresso"]
        info = (f"Usuário: {user['username']}\n"
                f"Perguntas Acertadas: {progresso['perguntas_acertadas']}\n"
                f"Total de Leituras: {len(progresso['leituras'])}")
        if message:
            info += f"\n{message}"
        self.profile_info.configure(text=info, text_color=message_color)

    def edit_password(self):
        new_password = self.entry_new_password.get()
        self.edit_password_callback(new_password)

    def logout(self):
        self.logout_callback()