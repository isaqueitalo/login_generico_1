
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(self.nome, 'já está filmando')
            return

        print(f'{self.nome} está filmando')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(self.nome, 'não está filmando')
            return

        print(f'{self.nome} está parando de filmar')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar enquanto filma')
            return

        print(f'{self.nome} está fotografando')


camera_1 = Camera('canon')
camera_2 = Camera('sony')
camera_1.filmar()
camera_1.filmar()
print(camera_1.filmando)
camera_1.fotografar()
camera_1.parar_filmar()
camera_1.fotografar()
