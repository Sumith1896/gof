from Player import Player

class FieldPlayer(Player):
	"""ConcreteComponent : Field Player class
	This is a concrete component. Later, we will add additional responsibilities
	like Forward, Defender etc to a field player."""
	
	"""A constructor to accept the name of the player"""
	def __init__(self, *args, **kwargs):
		Player.__init__(self, *args, **kwargs)

	"""Operation: Overrides PassBall operation"""
	def PassBall(self):
		print " Fieldplayer (%s) - passed the ball" %self.Name
