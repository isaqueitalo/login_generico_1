class Connection:
    # Credenciais fixas (somente esses usuários são aceitos)
    _valid_users = {
        "admin_master": "senha_super123",
        "guest_user": "guest_password456"
    }

    def __init__(self, host='localhost'):
        self.host = host
        self._user = None
        self._password = None
        self.connected = False

    # ===== Getter e Setter para user =====
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value: str):
        if not value or not value.strip():
            raise ValueError("Usuário não pode ser vazio!")
        if value not in self._valid_users:
            raise ValueError(f"Usuário '{value}' não é permitido!")
        self._user = value

    # ===== Getter e Setter para password =====
    @property
    def password(self):
        if self._password:
            return "*" * len(self._password)   # esconde a senha real
        return None

    @password.setter
    def password(self, value: str):
        if not value:
            raise ValueError("Senha não pode ser vazia!")
        if not self.is_valid_password(value):
            raise ValueError("Senha inválida! A senha está incorreta.")
        self._password = value

    # ===== Métodos de classe e utilidades =====
    @classmethod
    def create_with_credentials(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def is_valid_password(password):
        return len(password) > 8
    
    @staticmethod
    def login_message(user, msg):
        print(f"login: {user}, {msg}")

    # ===== Conexão =====
    def connect(self):
        if self._user and self._password:
            if self._valid_users[self._user] == self._password:
                self.connected = True
                self.login_message(self._user, "conectado com sucesso!")
            else:
                raise ValueError("Senha incorreta!")
        else:
            raise ValueError("Usuário ou senha não definidos!")

    def disconnect(self):
        if self.connected:
            self.connected = False
            print("Conexão encerrada.")
        else:
            print("Nenhuma conexão ativa.")

    # ===== Representação =====
    def __str__(self):
        status = "Conectado" if self.connected else "Desconectado"
        return f"Connection(user={self._user}, host={self.host}, status={status})"

# =====================
# Login interativo
# =====================
try:
    login = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    user = Connection.create_with_credentials(login, senha)
    user.connect()
    print(user)   # Mostra status conectado

except Exception as e:
    print(f"Erro: {e}")

 # Loop até o usuário digitar "sair"
# Loop até o usuário digitar "sair"
try:
    while True:
        comando = input("\nDigite 'sair' para encerrar o sistema: ").strip().lower()
        if comando == "sair":
            user.disconnect()
            print("Sistema encerrado.")
            break
        else:
            print("Comando inválido. Digite 'sair' para sair.")
except Exception as e:
    print(f"Erro: {e}")
