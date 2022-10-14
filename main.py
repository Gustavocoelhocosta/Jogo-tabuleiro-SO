from threading import Thread
from game2dboard import Board
from time import sleep
from ficha import Ficha
from threading import Lock, enumerate, active_count
import PySimpleGUI as sg
from audioplayer import AudioPlayer
import os

lock_rodada = Lock()
tabuleiro = Board(10, 10)
fichas = []
tempo_restante = 0
lock_matar_ficha = Lock()

sounds_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sounds')
plim = AudioPlayer(os.path.join( sounds_dir, 'plim.mp3'))
plim.volume = 20

def iniciar_tabuleiro():
	for linha in range(0, 10):
		for coluna in range(0, 10):
			tabuleiro[linha][coluna] = ""

def mouse_click(button, linha, coluna):
	for ficha in fichas:
		if ficha.esta_na_posicao(linha, coluna):
			remover_ficha_tabuleiro(ficha)

def remover_ficha_tabuleiro(ficha):
	lock_matar_ficha.acquire()
	remover_ficha(ficha)
	fichas.remove(ficha)
	lock_matar_ficha.release()
	plim.play()
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
	if len(fichas) == 0:
		return tabuleiro.close()
	tabuleiro.print("Fichas restantes: {0}".format(len(fichas)))

def reinicia(tecla):
	if tecla == 'r':
		return tabuleiro.close()
	else:
		None

def iniciar():
	tempo_total, jogadas = tela_inicial_dificuldade()
	if tempo_total:
		iniciar_tabuleiro()
		for id in range(1, 3):
			thread = Thread(target = jogada, args = (id, tempo_total, jogadas))
			thread.start()
		tabuleiro.on_mouse_click = mouse_click
		tabuleiro.on_key_press = reinicia
		print("Threads ({0}) {1}".format(enumerate(), active_count()))
		tabuleiro.create_output()
		tempo_restante = tempo_total
		tabuleiro.on_timer = loop_do_jogo
		tabuleiro.start_timer(50)
		tabuleiro.show()
	else:
		return
	if len(fichas) == 0:
		resultado = 'venceu'
	else:
		resultado = 'perdeu'
	print(resultado)
	tela_fim_jogo(resultado)

def tela_fim_jogo(resultado):
	if resultado == 'venceu':
		mensagem = "você venceu, bora jogar denovo?"

	elif resultado == 'perdeu':
		mensagem = "infelizmente você perdeu, bora jogar denovo?"

	else:
		return
	print(mensagem)
	sg.theme('Dark Green 1')
	layout = [[sg.Text(mensagem)],
			  [sg.Button('reiniciar jogo')]]
	window2 = sg.Window('Cata Moeda', layout, location=(800, 300))

	while True:
		event, values = window2.read()
		if event == 'reiniciar jogo':
			window2.close()
			iniciar()
			break
		elif event == WIN_CLOSED:
			window2.close()
			break
		else:
			window2.close()
			break






def tela_inicial_dificuldade():
	sg.theme('Dark Green 1')
	layout = [  [sg.Text('Escolha o grau de dificuldade')],
				[sg.Button('fácil'), sg.Button('médio'), sg.Button('difícil')] ]
	window = sg.Window('Cata Moeda', layout, location=(800,300))

	while True:
		event, values = window.read()
		if event == 'fácil':
			print('facil')
			window.close()
			return 40, 30

		elif event == 'médio':
			window.close()
			return 30, 30

		elif event == 'difícil':
			window.close()
			return 20, 30

		else:
			window.close()
			return False, False


iniciar()

