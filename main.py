from game2dboard import Board

def mouse_click(button, linha, coluna):
	print("{0}:{1}".format(linha, coluna))

tabuleiro = Board(10, 10)
tabuleiro.on_mouse_click = mouse_click
tabuleiro.show()
