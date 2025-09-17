class Connection:

    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        if self.is_valid_password(password):
            self.password = password
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

        

# Usando o método de classe
user_1 = Connection.create_with_credentials('admin', 'admin 123')

print(user_1.user)      # admin
print(user_1.password)  # admin 123
Connection.login_message(user_1.user, 'logado com sucesso!')

