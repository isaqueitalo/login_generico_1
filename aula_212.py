class Connection:

    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self._password = None
        self.connected = False  # estado da conexão

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        if self.is_valid_password(password):
            self._password = password
        else:
            raise ValueError("Senha inválida! A senha deve ter mais de 8 caracteres.")

    @classmethod
    def create_with_credentials(cls, user, password):
        connection = cls()
        connection.set_user(user)
        connection.set_password(password)
        return connection
    
    @staticmethod
    def is_valid_password(password):
        return len(password) > 8
    
    @staticmethod
    def login_message(user, msg):
        print(f'login: {user}, {msg}')

    def connect(self):
        if self.user and self._password:
            self.connected = True
            self.login_message(self.user, "conectado com sucesso!")
        else:
            raise ValueError("Usuário ou senha não definidos!")

    def disconnect(self):
        if self.connected:
            self.connected = False
            print("Conexão encerrada.")
        else:
            print("Nenhuma conexão ativa.")

    def __str__(self):
        status = "Conectado" if self.connected else "Desconectado"
        return f"Connection(user={self.user}, host={self.host}, status={status})"
        

# =====================
# Exemplo de uso
# =====================
user_1 = Connection.create_with_credentials("admin", "admin 123")

print(user_1)              # Mostra info da conexão (desconectado)
user_1.connect()           # Conecta
print(user_1)              # Mostra info (conectado)
user_1.disconnect()        # Desconecta
print(user_1)              # Mostra info (desconectado)
