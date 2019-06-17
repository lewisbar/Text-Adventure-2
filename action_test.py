from action import Action

class La:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
		self.a = Action(
			name='action 1',
			hotkey='a',
			method=self.move_to
		)

	def move_to(self, x, y):
		print(x, y)
	
la = La(30, 44)
la.a.method(la.x, la.y+1)
