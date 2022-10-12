from game2dboard import Board

from ficha import Ficha

ficha_1 = Ficha(1)

tabuleiro = Board(10, 10)

def iniciar_tabuleiro():
	for linha in range(0, 10):
		for coluna in range(0, 10):
			tabuleiro[linha][coluna] = ""

def mouse_click(button, linha, coluna):
	print("{0}:{1}".format(linha, coluna))

def executar_rodada():
	remover_ficha(ficha_1)
	colocar_ficha(ficha_1)

def colocar_ficha(ficha):
	ficha.trocar_posicao()
	tabuleiro[ficha.linha][ficha.coluna] += str(ficha.id)

def remover_ficha(ficha):
	tabuleiro[ficha.linha][ficha.coluna] = ""

def iniciar():
	iniciar_tabuleiro()
	executar_rodada()
	tabuleiro.on_mouse_click = mouse_click
	tabuleiro.on_timer = executar_rodada
	tabuleiro.start_timer(2 * 1000)
	tabuleiro.show()

iniciar()
