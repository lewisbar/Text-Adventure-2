class Content:
	def __init__(self, name, pre_description, post_description):
		self.name = name
		self.pre_description = pre_description
		self.post_description = post_description
		self.is_explored = False
		self.is_done = False
	
	def description(self):
		if not self.is_done:
			return self.pre_description
		else:
			return self.post_description

class Monster(Content):
	def __init__(self, name, pre_description, post_description, hp, damage, loot_effect=None):
		super().__init__(name, pre_description, post_description)
		self.hp = hp
		self.damage = damage
		self.effect = loot_effect
	
	def attack(self, player):
		player.hp -= self.damage

class Item(Content):
	def __init__(self, name, pre_description, post_description, action=None, effect=None):
		super().__init__(name, pre_description, post_description)
		self.action = action
		self.effect = effect

class Weapon(Item):
	def __init__(self, name, pre_description, post_description, damage, prefix='', boost=0, action=None, effect=None):
		super().__init__(name, pre_description, post_description, action, effect)
		self.damage = damage
		self.prefix = prefix
		self.boost = boost
	
	def damage_with_boost(self):
		return self.damage + self.boost

	def name_with_prefix(self):
		return self.prefix + self.name

class Door(Content):
	def __init__(self, name, pre_description, post_description, direction):
		super().__init__(name, pre_description, post_description)
		self.direction = direction
