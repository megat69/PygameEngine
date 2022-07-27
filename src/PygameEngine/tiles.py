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
		# Checking that the color is a valid RGB color
		if any(color[i] > 255 or color[i] < 0 for i in range(len(color))):
			raise Exception(f"Invalid color on tile creation : {color}")

		self.color = color
		self.enabled = enabled
