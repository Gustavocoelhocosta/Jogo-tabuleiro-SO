from random import randint

class Ficha:
    def __init__(self, numero):
        self.id = numero
        self.linha = 0
        self.coluna = 0

    def trocar_posicao(self):
        self.linha = randint(0,9)
        self.coluna = randint(0,9)
