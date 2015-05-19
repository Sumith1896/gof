class Ball:
    """Subject : The Ball Class"""
    def __init__(self, *args, **kwargs):
        """A list of observers"""
        self.observers = []
    def AttachObserver(self, obj):
        """Routine to attach an observer"""
        self.observers.append(obj)
    def DetachObserver(self, obj):
        """Routine to remove an observer"""
        self.observers.remove(obj)
    def NotifyObservers(self):
        """Routine to notify all observers"""
        for observer in self.observers:
            observer.Update()
