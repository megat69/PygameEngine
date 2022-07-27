import pygame; pygame.init()  # Pygame import
from pygame.locals import *
import sys


class PygameEngine:
	def __init__(self, dimensions:tuple=(500, 500), caption:str="", display_fps:bool=True):
		# ------------- pygame/window ------------- #
		self.clock = pygame.time.Clock()
		self._caption = caption
		pygame.display.set_caption(self._caption)
		self.screen = pygame.display.set_mode(dimensions, 0, 32)
		self.display_fps = display_fps

		# Init vars
		self.clicking = False
		self.dt = 0

	def run(self, update):
		while True:
			# ------------- Background and mouse coords ------------- #
			self.screen.fill((0, 0, 0))
			self.mx, self.my = pygame.mouse.get_pos()

			# ------------- Event handling ------------- #
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit(0)

				if event.type == MOUSEBUTTONDOWN:
					if event.button == 1:
						self.clicking = True

				if event.type == MOUSEBUTTONUP:
					if event.button == 1:
						self.clicking = False

			# ------------- Client update ------------- #
			update(self)

			# ------------- Update ------------- #
			if self.display_fps is True:
				pygame.display.set_caption(f"{self._caption}{' - ' if self._caption != '' else ''}FPS : {round(self.clock.get_fps(), 1)}")
			pygame.display.update()
			self.dt = self.clock.tick(60)


if __name__ == '__main__':
	app = PygameEngine((720, 480), "Hello World !")

	def update(self):
		if self.clicking:
			pos = (100, 100)
		else:
			pos = (20, 20)
		pygame.draw.rect(self.screen, (255, 255, 255), (*pos, 200, 200))

	app.run(update)
