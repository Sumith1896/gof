from IObserver import IObserver
from Position import Position

class Referee(IObserver):
    """ConcreteObserver :  The Referee Class"""
    """A constructor which allows creating a reference to a ball"""
    def __init__(self, ball = None, myName = None):
        """This variable holds the current state(position) of the ball"""
        self.ballPosition = Position()
        """This is a pointer to the ball in the system"""
        self.ball = ball
        """Name of the referee"""
        self.myName = myName
    def Update(self):
        """Update() is called from Notify function in Ball class"""
        self.ballPosition = self.ball.GetBallPosition()
        print "   Referee %s say that the ball is at %d, %d, %d." %(self.myName, self.ballPosition.X, self.ballPosition.Y, self.ballPosition.Z)
