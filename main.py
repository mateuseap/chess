import pygame
from classes.Board import Board

pygame.init()
pygame.display.set_caption('Chess')
pygame.display.set_icon(pygame.image.load('./assets/icon.png'))

WINDOW_SIZE = (600, 600)

screen = pygame.display.set_mode(WINDOW_SIZE)
board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

def draw(display):
	board.draw(display)
	pygame.display.update()

if __name__ == '__main__':
	running = True
	while running:
		for event in pygame.event.get():
			# Sair do jogo
			if event.type == pygame.QUIT:
				running = False
				
		draw(screen)