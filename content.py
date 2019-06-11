class Monster:
	def __init__(self, name, description, hp, damage, item):
		self.name = name
		self.description = description
		self.hp = hp
		self.damage = damage
		self.item = item
	
class FriendlyCharacter:
	def __init__(self, name, text, item):
		self.name = name
		self.text = text
		self.item = item

class Item:
	def __init__(self, name, description, action=None, effect=None):
		self.name = name
		self.description = description
		self.action = action
		self.effect = effect

class Weapon:
	def __init__(self, name, description, damage, prefix=None, effect=None):
		self.name = name
		self.description = description
		self.damage = damage
		self.prefix = prefix
		self.effect = effect
