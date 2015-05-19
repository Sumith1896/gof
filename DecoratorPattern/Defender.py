from PlayerRole import PlayerRole

class Defender(PlayerRole):
	"""ConcreteDecorator: Defender class is a Concrete implementation
	of the PlayerRole (Decorator) class"""
	def __init__(self, *args, **kwargs):
		PlayerRole.__init__(self, *args, **kwargs)

	"""Added Behavior: This is a responsibility exclusively for the Defender"""
	def Defend(self):
		print " Defender ({0}) - defended the ball" %self.player.Name
