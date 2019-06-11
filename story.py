from content import *

contents = {
	# Emptiness
	'000': 'Wall'
	
	# Monsters
	'm01': Monster(
		name='Spider',
		description='You notice a movement on the ceiling. A giant spider jumps at you!'
		hp=9,
		damage=2,
		item=Coin(11)
	),
	'm08': Monster(
		name='Poisonous Spider',
		description='There are thick cobwebs all over the walls. Then, all of a sudden, a huge spider runs directly towards you. Green poison is dripping from its fangs.',
		hp=19,
		damage=10,
		item=items[9]
	),
	
	# Friends
	'f08': FriendlyCharacter(
		name='Old man',
		text='''
Old man: When I was young, I used to fight those monsters. Now I\'m too old to fight. I can only hide from them. Take my old sword.
''',
		item=items[8]
	),
	
	# Items
	'i01': Item(
		name='Fists',
		description='Your bare fists.',
		damage=2,
	),
	'i08': Weapon(
		name='Old sword',
		description='An old sword.',
		damage=45,
		# action='Take sword'
	),
	'i05': Item(
		name='Spring',
		description='There is fresh water coming out from under a rock.',
		action='Drink water',
		effect=Effect(
			description='You refresh yourself with the clear water. You gain 10 HP',
			hp=10
		)
	)
	'i09': Item(
		name='Poison'
		description='Can be used to poison your weapon.',
		action='Use poison for weapon'
		effect=Effect(
			description='You use the poison to make your weapon poisonous.',
			weapon_prefix='Poisonous '
		)
	),
}
