import pygame; pygame.init()  # Pygame import
from pygame.locals import *
import sys

from tiles import Tile


class PygameEngine:
	def __init__(self, dimensions:tuple=(500, 500), caption:str="", display_fps:bool=True, tile_map:dict=None, tile_size:int=20):
		# ------------- pygame/window ------------- #
		self.clock = pygame.time.Clock()
		self._caption = caption
		pygame.display.set_caption(self._caption)
		self.screen = pygame.display.set_mode(dimensions, 0, 32)
		self.display_fps = display_fps
		self.tile_map = tile_map if tile_map is not None else {}
		self.tile_size = tile_size

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

			# ------------- Tiles rendering ---------------------------------------------------------------------------------- #
			self.render_tiles()

			# ------------- Client update ------------- #
			update(self)

			# ------------- Update ------------- #
			if self.display_fps is True:
				pygame.display.set_caption(f"{self._caption}{' - ' if self._caption != '' else ''}FPS : {round(self.clock.get_fps(), 1)}")
			pygame.display.update()
			self.dt = self.clock.tick(60) / 1000

	def render_tiles(self):
		"""
		Renders all the tile on the screen.
		"""
		# Fetches all tiles in the tilemap
		for tile_pos, tile in self.tile_map.items():
			# Skips the tile if it is not enabled.
			if tile.enabled is False: continue

			# Gets the tile position from the tilemap key
			tile_pos = tile_pos.split(";")
			x, y = int(tile_pos[0]), int(tile_pos[1])

			# Draws the tile onto the screen
			pygame.draw.rect(
				self.screen,
				tile.color,
				pygame.Rect(x * self.tile_size, y * self.tile_size,self.tile_size, self.tile_size)
			)


if __name__ == '__main__':
	app = PygameEngine((720, 480), "Hello World !", tile_size=20)

	WHITE = (255, 255, 255)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 255)

	tilemap = {
		"25;2": Tile(WHITE)
	}
	for i in range(12, 30):
		tilemap[str(i)+";14"] = Tile(GREEN, False)
		tilemap[str(i)+";15"] = Tile(GREEN)

	app.tile_map = tilemap

	def update(self):
		pass

	app.run(update)
