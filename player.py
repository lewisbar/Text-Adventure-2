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
		if effect.weapon:
			self.weapon = effect.weapon
		if effect.weapon_prefix:
			self.weapon.prefix = effect.weapon_prefix
		if effect.weapon_boost:
			self.weapon.boost = effect.weapon_boost
		if effect.key:
			self.keys.append(effect.key)
	
	def is_alive(self):
		return self.hp > 0
	
	def attack(self, monster):
		monster.hp -= self.weapon.damage_with_boost()
