from game2dboard import Board

from ficha import Ficha


ficha_1 = Ficha(1)

def mouse_click(button, linha, coluna):
	remover_ficha(ficha_1)
	colocar_ficha(ficha_1)
	print("{0}:{1}".format(linha, coluna))

tabuleiro = Board(10, 10)
tabuleiro.on_mouse_click = mouse_click

for linha in range(0, 10):
	for coluna in range(0, 10):
		tabuleiro[linha][coluna] = ""

def colocar_ficha(ficha):
	ficha.trocar_posicao()
	tabuleiro[ficha.linha][ficha.coluna] += str(ficha.id)

def remover_ficha(ficha):
	tabuleiro[ficha.linha][ficha.coluna] = ""

colocar_ficha(ficha_1)

tabuleiro.show()
