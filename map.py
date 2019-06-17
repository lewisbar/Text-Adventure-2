from story import *

class Map:
	def __init__(self):
		self.map = [
			[Start(),		Spider1(),Wasp2(),  Knife(), 		None		],
			[None, 			Chest1(),	None, 		Snake3(), Ant4()	],
			[Key1(),		None, 		Spring(), Chest1(), Crow5()	],
			[Beetle6(),	None, 		None, 		None, 		BrPlate()	],
			[Axe(), 		None, 		Chest2(),	Path2(), 	Path1()	],
			[DoorS(), 	Path3(), 	Spring(), None, 		None		],
			[Ape7(),		None, 		None, 		None,			None		],
			[Spring(),	Spider8(),Spider1(),None, 		End()		],
		]
	
	def content_at(self, x, y):
		return self.map[y][x]
	
	def is_valid(self, x, y):
		width = len(self.map[0])
		height = len(self.map)
		return (0 <= x < width) and (0 <= y < height) and (self.map[y][x] != None)
	
	def possible_directions_from(self, x, y):
		directions = []
		if self.is_valid(x, y-1):
			directions.append('north')
		if self.is_valid(x, y+1):
			directions.append('south')
		if self.is_valid(x-1, y):
			directions.append('west')
		if self.is_valid(x+1, y):
			directions.append('east')
			
		content = self.content_at(x, y)
		if isinstance(content, Door) and not content.is_done:
			directions.remove(content.direction)
			
		return directions
	
	def __str__(self):
		return self.map_str()
	
	def map_str(self, x=None, y=None, mode='explore'):
		'''
		There are three modes:
		- 'explore': Default mode. Only shows what the player has already explored.
		- 'outline': Cheat. Same as 'explore', but shows all walls.
		- 'reveal': Cheat. Shows the whole map.
		'''
		map_str = '\n'
		for i, row in enumerate(self.map):
			for j, content in enumerate(row):
				if not content:
					if self.has_explored_neighbors(j, i) or mode == 'outline' or mode == 'reveal':
						map_str += '####### '
					else:
						map_str += '??????? '
				else:
					display = type(content).__name__
					display = display + ((8-len(display))*' ')
					if i == y and j == x:
						display = 'YOU     '
					elif not content.is_explored and not mode == 'reveal':
						display = '??????? '
					else:
						display = type(content).__name__
						display = display + ((8-len(display))*' ')
					map_str += display
			map_str += '\n'
		return map_str
		
	def has_explored_neighbors(self, x, y):
		for i in range(y-1, y+2):
			for j in range(x-1, x+2):
				if self.is_valid(j, i):
					if self.map[i][j].is_explored:
						return True
		return False
