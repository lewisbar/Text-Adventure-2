class Room:
	def __init__(self, name, description, content, actions):
		self.name = name
		self.description = description
		self.content = content # can be monster, item, friendly character or door
		self.actions = actions
	
	def intro(self):
		if self.content:
			return self.content.description()
		else:
			return self.description
	
	def effect(self):
		if self.character and self.character.effect:
			self.character.effect()
		elif self.item and self.item.effect(:
			self.item.effect()
