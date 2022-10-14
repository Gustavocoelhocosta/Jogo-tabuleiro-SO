from threading import Thread
from game2dboard import Board
from time import sleep
from ficha import Ficha
from threading import Lock, enumerate, active_count
import PySimpleGUI as sg

lock_rodada = Lock()
tabuleiro = Board(10, 10)
fichas = []
tempo_restante = 0

def iniciar_tabuleiro():
	for linha in range(0, 10):
		for coluna in range(0, 10):
			tabuleiro[linha][coluna] = ""

def mouse_click(button, linha, coluna):
	print("{0}:{1}".format(linha, coluna))
	for ficha in fichas:
		if ficha.esta_na_posicao(linha, coluna):
			remover_ficha_tabuleiro(ficha)

def remover_ficha_tabuleiro(ficha):
	remover_ficha(ficha)
	ficha.matar()


def executar_rodada(ficha):
	remover_ficha(ficha)
	colocar_ficha(ficha)

def colocar_ficha(ficha):
	lock_rodada.acquire()
	ficha.trocar_posicao()
	while esta_ocupado(ficha):
		ficha.trocar_posicao()
	tabuleiro[ficha.linha][ficha.coluna] += " " + str(ficha.id)
	lock_rodada.release()

def remover_ficha(ficha):
	lock_rodada.acquire()
	tabuleiro[ficha.linha][ficha.coluna] = ""
	lock_rodada.release()

def esta_ocupado(ficha):
	return tabuleiro[ficha.linha][ficha.coluna] != ""

def jogada(id, tempo_total, jogadas):
	tempo_rodada = tempo_total / jogadas
	ficha = Ficha(id)
	fichas.append(ficha)
	while jogadas > 0 and ficha.viva:
		executar_rodada(ficha)
		sleep(tempo_rodada)
		jogadas -= 1

def loop_do_jogo():
	print("ghtytgt")
	tempo_restante -= 1
	tabuleiro.print("tempo restante: {0}".format(len(fichas)))

def iniciar(tempo_total, jogadas):
	iniciar_tabuleiro()
	for id in range(1, 10):
		thread = Thread(target = jogada, args = (id, tempo_total, jogadas))
		thread.start()
	tabuleiro.on_mouse_click = mouse_click
	print("Threads ({0}) {1}".format(enumerate(), active_count()))
	tabuleiro.create_output()
	tempo_restante = tempo_total
	tabuleiro.on_timer = loop_do_jogo
	tabuleiro.start_timer(1000)
	tabuleiro.show()
	print("Threads ({0}) {1}".format(enumerate(), active_count()))




def tela_inicial_dificuldade():
	tempo, jogadas = None, None
	sg.theme('Jogo pega moeda')
	layout = [  [sg.Text('Escolha o grau de dificuldade')],
				[sg.Button('fácil'), sg.Button('médio'), sg.Button('difícil')] ]
	window = sg.Window('Cata Moeda', layout)
	while True:
		event, values = window.read()
		if event == 'fácil':
			tempo, jogadas = 40, 30
			break
		elif event == 'médio':
			tempo, jogadas = 30, 30
			break
		elif event == 'difícil':
			tempo, jogadas = 20, 30
			break
		else:
			return

	window.close()
	iniciar(tempo, jogadas)

tela_inicial_dificuldade()
