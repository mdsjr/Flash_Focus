# user_manager.py
import json
import os

class UserManager:
    def __init__(self, file_path="users.json"):
        self.file_path = file_path
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump({"usuarios": []}, f)

    def load_users(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def save_users(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def cadastrar_usuario(self, username, password):
        data = self.load_users()
        if any(u["username"] == username for u in data["usuarios"]):
            return False  # Usuário já existe
        data["usuarios"].append({
            "username": username,
            "password": password,
            "progresso": {
                "leituras": [],
                "perguntas_acertadas": 0,
                "velocidade_media": 0.0
            }
        })
        self.save_users(data)
        return True

    def login_usuario(self, username, password):
        data = self.load_users()
        for user in data["usuarios"]:
            if user["username"] == username and user["password"] == password:
                return user
        return None

    def update_user_progress(self, username, updated_user_data):
        data = self.load_users()
        for i, user in enumerate(data["usuarios"]):
            if user["username"] == username:
                data["usuarios"][i] = updated_user_data
                self.save_users(data)
                return True
        return False