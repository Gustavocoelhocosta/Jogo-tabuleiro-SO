from game2dboard import Board

def mouse_click(button, linha, coluna):
	print("{0}:{1}".format(linha, coluna))

tabuleiro = Board(10, 10)
tabuleiro.on_mouse_click = mouse_click
tabuleiro.show()

def colocar_ficha(ficha):
	ficha.alternar_posicao()
	tabuleiro[ficha.linha][ficha.coluna] += str(ficha.id)

def remover_ficha(ficha):
	tabuleiro[ficha.linha][ficha.coluna] = ""

ficha1 = Ficha(1)
colocar_ficha(ficha1)