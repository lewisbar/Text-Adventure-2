class Effect:
	def __init__(self, description, hp=None, coins=None, weapon=None, weapon_prefix=None, weapon_boost=None, key=None):
		self.description = description
		self.hp = hp
		self.coins = coins
		self.weapon = weapon
		self.weapon_prefix = weapon_prefix
		self.weapon_boost = weapon_boost
		self.key = key
