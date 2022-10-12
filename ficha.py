from random import randint

class Ficha:
    def __init__(self, numero):
        self.id = numero
        self.linha = -1
        self.coluna = -1
        self.viva = True

    def trocar_posicao(self):
        self.linha = randint(0,9)
        self.coluna = randint(0,9)

    def esta_na_posicao(self, linha, coluna):
        return self.linha == linha and self.coluna == coluna

    def matar(self):
        self.viva = False
        self.linha = -1
        self.coluna = -1