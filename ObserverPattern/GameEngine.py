from Position import Position
from Ball import Ball
from Football import Football
from IObserver import IObserver
from Player import Player
from Referee import Referee

class GameEngine:
	"""This is the Game Engine"""

	"""Create our ball (i.e, the ConcreteSubject)"""
	ball = Football()

	"""Create few players (i.e, ConcreteObservers)"""
	Owen = Player(ball, "Owen")
	Ronaldo = Player(ball, "Ronaldp")
	Rivaldo = Player(ball, "Rivaldo")

	"""Create few referees (i.e, ConcreteObservers)"""
	Mike = Referee(ball, "Mike")
	John = Referee(ball, "John")

	"""Attach them with the ball"""
	ball.AttachObserver(Owen)
	ball.AttachObserver(Ronaldo)
	ball.AttachObserver(Rivaldo)
	ball.AttachObserver(Mike)
	ball.AttachObserver(John)
	print " After attaching the observers..."
	print "Update the position of the ball." 
	print "At this point, all the observers should be notified"

	ball.SetBallPosition(Position())
	"""Remove some observers"""
	ball.DetachObserver(Owen)
	ball.DetachObserver(John)
	print " After detaching Owen and John..."
	print "Updating the position of ball again"
	print "At this point, all the observers should be notified"

	ball.SetBallPosition(Position(10, 10, 30))
	print "Press any key to continue.."
	raw_input()

GameEngine()