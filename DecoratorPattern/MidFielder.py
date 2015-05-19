from PlayerRole import PlayerRole

class MidFielder(PlayerRole):
	"""ConcreteDecorator: MidFielder class is a Concrete implementation
	of the PlayerRole (Decorator) class"""
	def __init__(self, *args, **kwargs):
		PlayerRole.__init__(self, *args, **kwargs)

	"""Added Behavior: This is a responsibility exclusively for the Midfielder"""
	def Dribble(self):
		print " Midfielder (%s) - dribbled the ball" %self.player.Name
