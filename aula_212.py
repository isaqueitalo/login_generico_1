class Connection:
    # Credenciais fixas (apenas esses usuários podem logar)
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
    def user(self, value):
        if not value or len(value.strip()) == 0:
            raise ValueError("Usuário não pode ser vazio!")
        self._user = value

    # ===== Getter e Setter para password =====
    @property
    def password(self):
        if self._password:
            return "*" * len(self._password)   # esconde a senha real
        return None

    @password.setter
    def password(self, value):
        if self.is_valid_password(value):
            self._password = value
        else:
            raise ValueError("Senha inválida! A senha deve ter mais de 8 caracteres.")

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
        print(f'login: {user}, {msg}')

    def connect(self):
        if self._user and self._password:
            if self._user in self._valid_users and self._valid_users[self._user] == self._password:
                self.connected = True
                self.login_message(self._user, "conectado com sucesso!")
            else:
                raise ValueError("Login ou senha incorretos!")
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
        return f"Connection(user={self._user}, host={self.host}, status={status})"
        

# =====================
# Login interativo
# =====================
try:
    login = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    user = Connection.create_with_credentials(login, senha)
    user.connect()
    print(user)      # Mostra status conectado
    #user.disconnect()

except Exception as e:
    print(f"Erro: {e}")
