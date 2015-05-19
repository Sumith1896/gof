from Player import Player

class GoalKeeper(Player):
	"""ConcreteComponent : GaolKeeper class
	This is a concrete component. Later, we can add additional responsibilities
	to this class if required."""

	"""A constructor to accept the name of the player"""
	def __init__(self, *args, **kwargs):
		Player.__init__(self, *args, **kwargs)

	"""Operation: Overriding the base class operation"""
	def PassBall(self):
		print " GoalKeeper (%s) - passed the ball" %self.Name
