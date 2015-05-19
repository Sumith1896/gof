from PlayerRole import PlayerRole

class Forward(PlayerRole):
	"""ConcreteDecorator: Forward class is a Concrete implementation
	of the PlayerRole (Decorator) class"""
	def __init__(self, *args, **kwargs):
		PlayerRole.__init__(self, *args, **kwargs)

	"""Added Behavior: This is a responsibility exclusively for the Forward"""
	def ShootGoal(self):
		print " Forward (%s) - Shooted the ball to goalpost" %self.player.Name
