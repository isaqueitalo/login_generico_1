class Conection:

    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

c1 = Conection()
c1.set_user('admin')
c1.set_password('admin 123')

print(c1.user)
print(c1.password)
