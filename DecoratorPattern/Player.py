class Player:
	"""Component: The Player class"""

	def __init__(self, Name=None, *args, **kwargs):
		if Name is None:
			Name = []
		self.Name = Name

	def SetName(self, Name):
		self.Name = Name

	"""This is the Operation in the component
	and this will be overrided by concrete components"""
	def PassBall(self):
		pass
