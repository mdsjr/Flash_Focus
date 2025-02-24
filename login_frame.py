# login_frame.py
import tkinter as tk
import customtkinter

class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, parent, login_callback, cadastrar_callback):
        super().__init__(parent, fg_color="#0f1924")
        self.login_callback = login_callback
        self.cadastrar_callback = cadastrar_callback

        self.label_login = customtkinter.CTkLabel(self, text="Login", font=("Helvetica", 20))
        self.label_login.pack(pady=20)

        self.entry_username = customtkinter.CTkEntry(self, placeholder_text="Usuário")
        self.entry_username.pack(pady=10)

        self.entry_password = customtkinter.CTkEntry(self, placeholder_text="Senha", show="*")
        self.entry_password.pack(pady=10)

        self.btn_login = customtkinter.CTkButton(self, text="Entrar", command=self.login, fg_color="#155b74")
        self.btn_login.pack(pady=5)

        self.btn_cadastrar = customtkinter.CTkButton(self, text="Cadastrar", command=self.cadastrar, fg_color="#155b74")
        self.btn_cadastrar.pack(pady=5)

        self.label_status = customtkinter.CTkLabel(self, text="", text_color="red")
        self.label_status.pack(pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.login_callback(username, password)

    def cadastrar(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.cadastrar_callback(username, password)