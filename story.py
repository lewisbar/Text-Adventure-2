from content import *
from effect import Effect

# Start and End
class Start(Content):
	def __init__(self):
		super().__init__(
			name='Start',
			pre_description='''
Here it starts.
''',
			post_description='''
This is where it started.
''',
		)

class End(Content):
	def __init__(self):
		print('End not implemented properly')
		super().__init__(
			name='End',
			pre_description='''
Here it ends.
''',
			post_description='''
Here it ended.
'''
		)
		
# Paths
class Path1(Content):
	def __init__(self):
		super().__init__(
			name='Path',
			pre_description='''
You cross a narrow bridge.
''',
			post_description=None
		)
class Path2(Content):
	def __init__(self):
		super().__init__(
			name='Path',
			pre_description='''
You follow a wild path through a little forest.
''',
			post_description=None
		)
class Path3(Content):
	def __init__(self):
		super().__init__(
			name='Path',
			pre_description='''
You pass through a rocky gorge.
''',
			post_description=None
		)

# Doors
class DoorS(Door):
	def __init__(self):
		super().__init__(
			name='Door',
			pre_description='''
To the south, there\'s a massive looking door in the rock face. It\'s locked.
''',
	post_description='''
To the south, there\'s a massive looking door in the rock face. It\'s locked.
But you have a key. With shaking hands, you turn the key. Now you can go south.
''',
	direction='south'
		)

# Weapons
class Fists(Weapon):
	def __init__(self):
		super().__init__(
			name='Fists',
			pre_description='Your bare fists.',
			post_description=None,
			damage=4,
		)
class Knife(Weapon):
	def __init__(self):
		super().__init__(
			name='Knife',
			pre_description='''
There is someone hiding behind those logs. It\'s a boy.
''',
		post_description='''
The boy is gone. Hopefully he\'s hiding somewhere.
''',
			damage=12,
			action='Talk to boy',
			effect=Effect(
				description='''
You:
	Hello, boy! Are you okay?

Boy:
	The monsters are all over the island. They killed my parents. Somebody must help us.

You:
	Do you know where those monsters come from?

Boy:
	No. It started this summer. At first, there were only a few, but they are getting more and more.

You:
	I will help, if I can.
	
Boy:
	Do you have a weapon?

You:
	No.

Boy:
	Take this knife. I took it from my father after the monsters ... (tries not to cry). You can make better use of it, I guess.

New weapon: Knife.
''',
				weapon=self
			)
		)
class Axe(Weapon):
	def __init__(self):
		super().__init__(
			name='Axe',
			pre_description='''
There\'s a small loghouse. In front of it, you see a heavy axe with a broad blade sticking in a block of wood.
''',
			post_description=None,
			damage=28,
			action='Pick up axe',
			effect=Effect(
				description='''
New weapon: Axe
''',
				weapon=self
			)
		)
class NewSword(Weapon):
	def __init__(self):
		super().__init__(
			name='Sword',
			pre_description='A new sword.',
			post_description=None,
			damage=60
		)
	
# Healing
class Spring(Item):
	def __init__(self):
		super().__init__(
			name='Spring',
			pre_description='''
There is fresh water coming out from under a rock.
''',
			post_description='''
There is something dead lying in the water. You shouldn\'t drink here.
''',
			action='Drink water',
			effect=Effect(
				description='''
You refresh yourself with the clear water. You gain 10 HP.
''',
				hp=10
			)
		)

# Monsters
class Spider1(Monster):
	def __init__(self):
		super().__init__(
			name='Spider',
			pre_description='''
You notice a movement on the ceiling. A giant spider jumps at you!
''',
			post_description='''
A giant dead spider is lying on the ground.
''',
			hp=9,
			damage=2,
		)
		
class Wasp2(Monster):
	def __init__(self):
		super().__init__(
			name='Wasp',
			pre_description='''
Over there in that dark corner, there is someone.

You: Hello?

No answer. The only thing you hear is a strange deep, humming noise.
As you\'re getting closer, you see that the person is hunched over something. NO! That\'s not a person! It looks like a giant ... wasp! It\'s eating ... something that\'s lying on the floor. Now it has seen you! Its humming gets furious as it comes flying at you with speed.
''',
			post_description='''
A giant wasp rots on the ground beneath the remainders of ... something else.
''',
			hp=12,
			damage=4,
			loot_effect=Effect(
				description='''Out of the wasp\'s shell, you make yourself armor for your legs. You gain 25 HP.
''',
				hp=25
			)
		)

class Snake3(Monster):
	def __init__(self):
		super().__init__(
			name='Snake',
			pre_description='''
You feel a touch on your shoulder. Next thing you know, you\'re rolling on the ground, sqeezed by a big snake.
''',
			post_description='''
The corpse of a big snake is lying on the ground.
''',
			hp=15,
			damage=6,
			loot_effect=Effect(
				description='''From the snake\'s skin, you obtain a grayish substance said to heal all kinds of illness. You drink this healing potion. You gain 25 HP.
''',
				hp=25
			)
		)

class Ant4(Monster):
	def __init__(self):
		super().__init__(
			name='Ant',
			pre_description='''
What kind of island is this? A single ant, as tall as a child, is coming at you!
''',
			post_description='''
There\'s a dead super ant lying on the ground.
''',
			hp=18,
			damage=8
		)

class Crow5(Monster):
	def __init__(self):
		super().__init__(
			name='Crow',
			pre_description='''
As you pass under a tree, you suddenly hear the sound of flapping wings above you. You look up and see a black shadow falling on your face. It\'s a crow that\'s much too big.
''',
			post_description='''
A giant black crow\'s body is lying on the ground.
''',
			hp=21,
			damage=10
		)

class Beetle6(Monster):
	def __init__(self):
		super().__init__(
			name='Beetle',
			pre_description='''
From the rim of the forest, a black beetle with the size of a pony is rapidly crawling towards you.
''',
			post_description='''
A dead beetle with a split shell is lying on its back beneath a dense forest.
''',
			hp=24,
			damage=12
		)
		
class Ape7(Monster):
	def __init__(self):
		super().__init__(
			name='Ape',
			pre_description='''
Your stepping through the door didn\'t go unnoticed. A savage looking ape is coming at you. You quickly shut the door behind you and prepare yourself for the encounter.'
''',
			post_description='''
A dead ape is lying flat on the ground.
''',
			hp=27,
			damage=14
		)

class Spider8(Monster):
	def __init__(self):
		super().__init__(
			name='Poisonous Spider',
			pre_description='''
There are thick cobwebs all over the walls. Then, all of a sudden, a huge spider runs directly towards you. Green poison is dripping from its fangs.
''',
			post_description='''
A giant dead spider is lying on the ground.
''',
			hp=30,
			damage=16,
			loot_effect=Effect(
				description='''You use the spider\'s poison to make your weapon poisonous.
''',
				weapon_prefix='Poisonous ',
				weapon_boost=15
			)
		)
	
class Dragon20(Monster):
	def __init__(self):
		super().__init__(
			name='Dragon',
			pre_description='''
Hot air hits you in the face, accompanied by an unbearable sulfurous smell. A terrible inhuman scream cuts through the thick air. And then you see the beast. And it has seen you, too. Before you know it, you\'re hit by fire.'
''',
			post_description='''
The enormous corpse of a dragon is lying on the ground. It smells terrible.
''',
			hp=70,
			damage=50,
			loot_effect=Effect(
				description='''There is some something like liquid fire pouring out of the dragon\'s neck. You use this liquid fire to make your weapon burn.
''',
				weapon_prefix='Burning ',
				weapon_boost=30
			)
		)
	

class BrPlate(Item):
	def __init__(self):
		super().__init__(
			name='Woman',
			pre_description='''
You walk into a small village. It looks abandoned. Then you notice a woman peeking out of the window of a forge. As she sees you, she disappears into the house. Shortly after, she opens the door, waving you to come to her, all the while looking anxiously left and right.
''',
		post_description='''
The woman is gone. You hope she is safely hiding in one of the houses.
''',
		action='Talk to woman',
		effect=Effect(
			description='''
Woman:
  I heard you have come to save us from those terrible beasts. I crafted this breastplate especially for you.
  
You put on the breastplate. You gain 40 HP.
''',
			hp=40
		)
	)

class OldSword(Weapon):
	def __init__(self):
		super().__init__(
			name='Old Sword',
			pre_description='''
There is a small cottage in the shade of the forest. You see an old man on the porch.
''',
			post_description='''
The old man you met before is now gone.
''',
			damage=45,
			action='Talk to old man',
			effect=Effect(
				description='''
Old man:
	When I was young, I used to fight those monsters. Now I\'m too old to fight. I can only hide from them. Take my old sword.
''',
				weapon=self
			)
		)
	
# Treasure
class Chest1(Item):
	def __init__(self):
		super().__init__(
			name='Treasure Chest',
			pre_description='''
There is a rusty chest hidden behind bush and rock.
''',
			post_description='''
You see an open chest. It\'s empty.
''',
			action='Open chest',
			effect=Effect(
				description='''
You crack the chest open. There are five coins in it. You put them in your pocket.
''',
				coins=5
			)
		)
class Chest2(Item):
	def __init__(self):
		super().__init__(
			name='Treasure Chest',
			pre_description='''
There is a rusty chest hidden behind bush and rock.
''',
			post_description='''
You see an open chest. It\'s empty.
''',
			action='Open chest',
			effect=Effect(
				description='''
You crack the chest open. There are ten coins in it. You put them in your pocket.
''',
				coins=10
			)
		)
class Chest3(Item):
	def __init__(self):
		super().__init__(
			name='Treasure Chest',
			pre_description='''
There is a rusty chest hidden behind bush and rock.''',
			post_description='''
You see an open chest. It\'s empty.
''',
			action='Open chest',
			effect=Effect(
				description='''
You crack the chest open. There are 15 coins in it. You put them in your pocket.
''',
				coins=15
			)
		)

# Keys
class Key1(Item):
	def __init__(self):
		super().__init__(
			name='Key 1',
			pre_description='''
You see a middle aged man sitting in front of a cottage.
''',
			post_description='''
The man is nowhere to be seen. He must hava gone inside.
''',
			action='Talk to man',
			effect=Effect(
				description='''
Man:
	I expected you. I appreciate your efforts for our island. I have the key to that door. Do you really want to go there?

You:
	What is behind that door?
	
Man:
	Well, I\'ve never been there, but it\'s said that behind that door is the most terrible of all those beasts.
	
You:
	I will go. I must find the source of this evil.
	
Man:
	All right. Here is the key. I hope I will see you again. And I don\'t even dare to hope that you will free us from this horror. 
	
New key added to inventory.
''',
				key=self
			)
		)
