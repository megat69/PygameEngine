"""
Tile class, allows to render tiles on the screen.
"""
class Tile:
	def __init__(self, color:tuple, enabled:bool=True):
		"""
		A tile on the tilemap.
		:param color: Color of the tile, in (r, g, b) format.
		:param enabled: Whether the tile should be displayed. True by default.
		"""
		self.color = color
		self.enabled = enabled
