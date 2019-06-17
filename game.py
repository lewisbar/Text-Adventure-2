from narrate import narrate, list_up
from map import Map
from action import Action
from player import Player
from story import *
from content import *

class Game:
	def __init__(self):
		self.prepare_new_game()
	
	def play(self):
		# Game loop
		while self.is_playing:
			# Let monster attack
			self.get_attacked()
				
			# List up possible actions
			actions = self.possible_actions(self.player.x, self.player.y)
			list_up(*[str(a) for a in actions], char_delay=0.005, line_delay=0.1)
			
			# Add secret cheat actions
			actions.append(self.show_map_outline_action())
			actions.append(self.show_map_reveal_action())
			
			# Get input
			inpt = input().lower()
			
			# Execute selected action
			for a in actions:
				if inpt == a.hotkey:
					a.method()
					break
			else:
				print('')
			
			# Handle death
			if not self.player.is_alive():
				inpt = input('Try again? (y/n)').lower()
				if inpt == 'y':
					self.prepare_new_game()
				else:
					narrate('\nGoodbye! See you next time.')
					self.is_playing = False
		
	def prepare_new_game(self):
		self.map = Map()
		self.player = Player(
			hp=100, 
			weapon=Fists()
		)
		self.move_to(0, 0)
		self.is_playing = True
		
	def possible_actions(self, x, y):
		actions = []
		content = self.map.content_at(x, y)
		if not content.is_done:
			if isinstance(content, Item) and content.action:
				actions.append(self.pick_up_action_with_name(content.action))
			elif isinstance(content, Monster):
				actions.append(self.attack_action())
			
		directions = self.map.possible_directions_from(x, y)
		if 'north' in directions:
			actions.append(self.move_north_action())
		if 'south' in directions:
			actions.append(self.move_south_action())
		if 'west' in directions:
			actions.append(self.move_west_action())
		if 'east' in directions:
			actions.append(self.move_east_action())
		actions.append(self.show_inventory_action())
		actions.append(self.show_map_explore_action())
		actions.append(self.quit_action())
		return actions

	def show_inventory(self):
		list_up(
*'''
 
INVENTORY:
Health: {}
Weapon: {}
Damage: {}
Coins: {}
Keys: {}
 
'''
.format(self.player.hp, self.player.weapon.name_with_prefix(), self.player.weapon.damage_with_boost(), self.player.coins, ', '.join([k.name for k in self.player.keys])).split('\n'))
	
	# Moving
	def move_north(self):
		self.move_to(self.player.x, self.player.y-1)
	
	def move_south(self):
		self.move_to(self.player.x, self.player.y+1)
	
	def move_west(self):
		self.move_to(self.player.x-1, self.player.y)
	
	def move_east(self):
		self.move_to(self.player.x+1, self.player.y)
	
	def move_to(self, x, y):
		self.player.x = x
		self.player.y = y
		content = self.map.content_at(x, y)
		content.is_explored = True
		if isinstance(content, Door) and self.player.keys and not content.is_done:
			content.is_done = True
			del self.player.keys[0]
		narrate(content.description())
		if isinstance(content, End):
			if input('\nPlay again? (y/n)').lower() == 'y':
				self.prepare_new_game()
			else:
				narrate('\nGoodbye! See you next time.')
				self.is_playing = False
			
	# Interacting
	def attack(self):
		content = self.map.content_at(self.player.x, self.player.y)
		if isinstance(content, Monster):
			self.player.attack(content)
			if content.hp <= 0:
				narrate('''
You kill {} with {}!
'''.format(content.name, self.player.weapon.name))
				content.is_done = True
				if content.effect:
					self.player.apply_effect(content.effect)
					narrate(content.effect.description)
			else:
				narrate('''
You deal {0} damage to {1} with {2}. {1} has {3} HP left.
'''.format(self.player.weapon.damage_with_boost(), content.name, self.player.weapon.name, content.hp))
	
	def get_attacked(self):
		content = self.map.content_at(self.player.x, self.player.y)
		if isinstance(content, Monster) and not content.is_done:
			content.attack(self.player)
			if self.player.is_alive():
				narrate('''{0} deals {1} damage to you. You have {2} health left.
'''.format(content.name, content.damage, self.player.hp))
	
	def pick_up(self):
		item = self.map.content_at(self.player.x, self.player.y)
		# if isinstance(item, Weapon):
		# 	self.player.weapon = item
		# elif isinstance(item, Item):
		self.player.apply_effect(item.effect)
		narrate(item.effect.description)
		item.is_done = True
	
	# Quit game
	def quit(self):
		inpt = input('\nAre you sure you want to quit? All progress will be lost. Quit game? (y/n)')
		if inpt.lower() == 'y':
			narrate('\nGoodbye! See you next time.')
			self.is_playing = False
		else:
			print('')
	
	# Map
	def show_map_explore(self):
		# Default map
		print(self.map.map_str(self.player.x, self.player.y))
	
	def show_map_outline(self):
		# Cheat: Shows all walls
		print(self.map.map_str(self.player.x, self.player.y, mode='outline'))
	
	def show_map_reveal(self):
		# Cheat: Shows everything
		print(self.map.map_str(self.player.x, self.player.y, mode='reveal'))
			
	# Actions
	def show_inventory_action(self):
		return Action(
		name='Inventory',
		hotkey='i',
		method=self.show_inventory
	)
	def move_north_action(self):
		return Action(
		name='Move north',
		hotkey='n',
		method=self.move_north
	)
	def move_south_action(self):
		return Action(
			name='Move south',
			hotkey='s',
			method=self.move_south
		)
	def move_west_action(self):
		return Action(
			name='Move west',
			hotkey='w',
			method=self.move_west
		)
	def move_east_action(self):
		return Action(
			name='Move east',
			hotkey='e',
			method=self.move_east
		)
	def attack_action(self):
		return Action(
			name='Attack',
			hotkey='a',
			method=self.attack
		)
	def quit_action(self):
		return Action(
			name='Quit',
			hotkey='q',
			method=self.quit
		)
	def show_map_explore_action(self):
		return Action(
			name='Map',
			hotkey='m',
			method=self.show_map_explore
		)
	def show_map_outline_action(self):
		return Action(
			name='Map Outline',
			hotkey='mo',
			method=self.show_map_outline
		)
	def show_map_reveal_action(self):
		return Action(
			name='Map',
			hotkey='mr',
			method=self.show_map_reveal
		)
	def pick_up_action(self):
		return Action(
			name='Pick up',
			hotkey='p',
			method=self.pick_up
		)
		
	def pick_up_action_with_name(self, action_name):
		return Action(
		name=action_name,
		hotkey=action_name.lower()[0],
		method=self.pick_up
	)
	
	'''
	def action_with_name(self, action_name):
		return Action(
			name=action_name,
			hotkey=action_name.lower()[0],
			method=getattr(self, action_name.lower().replace(' ', '_'))
		)
	'''

if __name__ == '__main__':
	Game().play()
