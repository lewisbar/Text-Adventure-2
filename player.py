class Player:
	def __init__(self, hp, weapon, coins=0, keys=[], x=0, y=0):
		self.hp = hp
		self.weapon = weapon
		self.coins = coins
		self.keys = keys
		self.x = x
		self.y = y
	
	def apply_effect(self, effect):
		if effect.hp:
			self.hp += effect.hp
		if effect.coins:
			self.coins += effect.coins
		if effect.weapon_prefix:
			self.weapon.prefix = effect.weapon_prefix
		if effect.weapon_effect:
			self.weapon.effect = effect.weapon_effect
	
	def is_alive(self):
		return self.hp > 0
