from TeamStrategy import TeamStrategy
from AttackStrategy import AttackStrategy
from DefendStrategy import DefendStrategy
from Team import Team

class GameEngine:
	"""GameEngine class for demonstration"""

	"""Let us create a team and set its strategy,
	and make the teams play the game"""
	"""Create few strategies"""
	attack = AttackStrategy()
	defend = DefendStrategy()

	"""Create our teams"""
	france = Team("France")
	italy = Team("Italy")

	print "Setting the strategies.."
	"""Now let us set the strategies"""
	france.SetStrategy(attack)
	italy.SetStrategy(defend)

	"""Make the teams start the play"""
	france.PlayGame()
	italy.PlayGame()

	print "Changing the strategies.."
	"""Let us change the strategies"""
	france.SetStrategy(defend)
	italy.SetStrategy(attack)
	
	"""Make them play again"""
	france.PlayGame()
	italy.PlayGame()

	"""Wait for a key press"""
	print "Press any key to continue..."
	raw_input()

GameEngine()