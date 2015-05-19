from Ball import Ball
from Position import Position

class Football(Ball):
    """ConcreteSubject : The Ball Class"""
    def __init__(self, myPosition=None, *args, **kwargs):
        Ball.__init__(self, *args, **kwargs)
        if myPosition is None:
            myPosition = Position()
        """State: The position of the ball"""
        self.myPosition = myPosition
    def GetBallPosition(self):
        """This function will be called by observers to get current position"""
        return self.myPosition
    def SetBallPosition(self, myPosition):
        """Some external client will call this to set the ball's position"""
        self.myPosition = myPosition
        """Once the position is updated, we have to notify observers"""
        self.NotifyObservers()
