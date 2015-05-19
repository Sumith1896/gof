from TeamStrategy import TeamStrategy

class AttackStrategy(TeamStrategy):
	"""ConcreteStrategy: The AttackStrategy class
	This class is a concrete implementation of the
	strategy class."""
	def __init__(self, *args, **kwargs):
		TeamStrategy.__init__(self, *args, **kwargs)

	"""Overrides the Play function.
	Let us play some attacking game"""
	def Play(self):
		"""Algorithm to attack"""
		print " Playing in attacking mode"
