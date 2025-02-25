
import tkinter as tk
import customtkinter
import win32gui
import win32con
from login_frame import LoginFrame
from main_frame import MainFrame
from progress_frame import ProgressFrame
from profile_frame import ProfileFrame
from user_manager import UserManager

class FlashFocusGUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.user_manager = UserManager()
        self.current_user = None
        self.frames = {}
        self.title("Flash Focus")
        self.iconbitmap("assets/icon.ico")
        self.configure(fg_color="#0f1924")


        self.frames["login"] = LoginFrame(self, self.login, self.cadastrar)
        self.frames["main"] = MainFrame(self, self.ajustar_velocidade, self.gerar_pergunta)
        self.frames["progress"] = ProgressFrame(self)
        self.frames["profile"] = ProfileFrame(self, self.edit_password, self.logout)


        self.show_frame("login")


        self.after(1000, self.maximizar_janela)

    def show_frame(self, frame_name): #
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[frame_name].pack(fill="both", expand=True)
        if frame_name == "progress" and self.current_user:
            self.frames["progress"].update_progress_display(self.current_user)
        elif frame_name == "profile" and self.current_user:
            self.frames["profile"].update_profile_display(self.current_user)

    def login(self, username, password):
        user = self.user_manager.login_usuario(username, password)
        if user:
            self.current_user = user
            self.show_frame("main")
        else:
            self.frames["login"].label_status.configure(text="Usuário ou senha incorretos!")

    def cadastrar(self, username, password):
        if not username or not password:
            self.frames["login"].label_status.configure(text="Preencha todos os campos!")
            return
        if self.user_manager.cadastrar_usuario(username, password):
            self.frames["login"].label_status.configure(text="Usuário cadastrado com sucesso!", text_color="green")
        else:
            self.frames["login"].label_status.configure(text="Usuário já existe!")

    def edit_password(self, new_password):
        if new_password:
            self.current_user["password"] = new_password
            self.user_manager.update_user_progress(self.current_user["username"], self.current_user)
            self.frames["profile"].entry_new_password.delete(0, tk.END)
            self.frames["profile"].update_profile_display(self.current_user, "Senha alterada com sucesso!")
        else:
            self.frames["profile"].update_profile_display(self.current_user, "Digite uma nova senha!", "red")

    def logout(self):
        self.current_user = None
        self.show_frame("login")
        self.frames["login"].entry_username.delete(0, tk.END)
        self.frames["login"].entry_password.delete(0, tk.END)
        self.frames["login"].label_status.configure(text="")

    def maximizar_janela(self):
        hwnd = self.winfo_id()
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        self.state('zoomed')

    def ajustar_velocidade(self, value):
        self.frames["main"].text_processor.ajustar_velocidade(value)
        self.user_manager.update_user_progress(self.current_user["username"], self.current_user)

    def gerar_pergunta(self):
        self.frames["main"].gerar_pergunta()

    def save_progress(self):
        self.user_manager.update_user_progress(self.current_user["username"], self.current_user)