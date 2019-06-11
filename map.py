from story import contents

class Map:
	def __init__(self):
		self.rooms = [
			[00, 00, 'm20', 00, 00, 00, 00, 00],
			[00, 00, 00, 00, 00, 00, 00, 00],
			[00, 00, 00, 00, 00, 00, 00, 00],
			[00, 00, 00, 00, 00, 00, 00, 00],
			[00, 00, 00, 00, 00, 00, 00, 00],
			[00, 00, 00, 00, 00, 00, 'm01', 00],
			[00, 00, 00, 00, 00, 00, 00, 00],
			[00, 00, 00, 00, 00, 00, 00, 00],
		]
	
	def room(x, y):
		return contents[self.rooms[y][x]]
