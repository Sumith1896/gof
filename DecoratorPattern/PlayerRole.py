from Player import Player

class PlayerRole(Player):
	"""Decorator: PlayerRole is the decorator"""

	def __init__(self, player=None, *args, **kwargs):
		Player.__init__(self, *args, **kwargs)
		if player is None:
			player = []
		self.player = player


	"""This function is used to assign a player to this role
	Keep a reference to the player, to whom this
	role is given"""
	def AssignPlayer(self, player):
		self.player = player

	"""Call the base component's function"""
	def PassBall(self):
		self.player.PassBall()
