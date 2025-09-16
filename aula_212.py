class Connection:

    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def criate_with_credentials(cls, user, password):
        connection = cls()
        connection.password = password
        connection.user = user
        return connection
        

c1 = Connection()
c1 = Connection.criate_with_credentials('admin', 'admin 123')
# c1.set_user('admin')
# c1.set_password('admin 123')

print(c1.user)
print(c1.password)
