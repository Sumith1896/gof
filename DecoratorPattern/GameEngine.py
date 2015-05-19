from Player import Player
from FieldPlayer import FieldPlayer
from GoalKeeper import GoalKeeper
from PlayerRole import PlayerRole
from Forward import Forward
from MidFielder import MidFielder
from Defender import Defender

class GameEngine:
	"""Putting it all together"""

	"""-- Step 1:
	Create few players (concrete components)
	Create few field Players"""
	owen = FieldPlayer("Owen")
	beck = FieldPlayer("Beckham")
	"""Create a goal keeper"""
	khan = GoalKeeper("Khan")

	"""-- Step 2:
	Just make them pass the ball
	(during a warm up session)"""
	print " > Warm up Session... "
	owen.PassBall()
	beck.PassBall()
	khan.PassBall()

	"""-- Step 3: 
	Create and assign the responsibilities
	(when the match starts)"""
	print " > Match is starting.. "
	"""Set owen as our first forward"""
	forward1 = Forward()
	forward1.AssignPlayer(owen)
	"""Set Beckham as our midfielder"""
	midfielder1 = MidFielder()
	midfielder1.AssignPlayer(beck)
	"""Now, use these players to do actions
	specific to their roles
	Owen can pass the ball"""
	forward1.PassBall()
	"""Beckham can dribble"""
	midfielder1.Dribble()
	"""Beckham can pass ball too"""
	midfielder1.PassBall()
	"""And Owen can shoot as well"""
	forward1.ShootGoal()

	"""-- Step 4: 
	Now, changing responsibilities
	(during a substitution)"""
	"""Assume that owen got injured, and we need a new player
	to play as our forward1"""
	print " > OOps, Owen got injured."
	print "Jerrard replaced Owen.. "
	"""Create a new player"""
	jerrard = FieldPlayer("Jerrard")
	"""Ask Jerrard to play in position of Owen"""
	forward1.AssignPlayer(jerrard)
	forward1.ShootGoal()

	"""-- Step 5:
	Adding multiple responsibilities
	(When a player need to handle multiple roles)
	We already have Beckham as our midfielder.
	Let us ask him to play as an additional forward"""
	onemoreForward = Forward()
	onemoreForward.AssignPlayer(beck)
	print " > Beckham has multiple responsibilities.. "
	"""Now Beckham can shoot"""
	onemoreForward.ShootGoal()
	"""And use his earlier responsibility to dribble too"""
	midfielder1.Dribble()
	"""According to our design, you can attach the responsibility of
	a forward to a goal keeper too, but when you actually
	play football, that's rarely the case"""

	print "Press any key to continue..."
	raw_input()

GameEngine()