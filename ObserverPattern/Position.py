class Position:
    """Position: This is a data structure to hold the position of the ball"""
    def __init__(self, X = None, Y = None, Z = None):
        if X is None:
            X = 0
        self.X = X
        if Y is None:
            Y = 0
        self.Y = Y
        if Z is None:
            Z = 0
        self.Z = Z
