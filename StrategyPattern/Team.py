class Team:
	"""Context: The Team class
	This class encapsulates the algorithm"""

	def __init__(self, teamName = None, *args, **kwargs):
		"""Constructor to create this class, by passing the team's
		name"""
		if teamName is None:
			teamName = []
		self.teamName = teamName

	def SetStrategy(self, strategy):
		"""ContextInterface to set the strategy"""
		self.strategy = strategy

	def PlayGame(self):
		"""Function to play
		Print the team's name"""
		print self.teamName
 		"""Play according to the strategy"""
		self.strategy.Play()
