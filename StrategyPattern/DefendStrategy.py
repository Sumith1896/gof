from TeamStrategy import TeamStrategy

class DefendStrategy(TeamStrategy):
	"""ConcreteStrategy: The DefendStrategy class
	This class is a concrete implementation of the
	strategy class."""
	def __init__(self, *args, **kwargs):
		TeamStrategy.__init__(self, *args, **kwargs)

	"""Overrides the Play function.
	Let us go defensive"""
	def Play(self):
		"""Algorithm to defend"""
		print " Playing in defending mode"
