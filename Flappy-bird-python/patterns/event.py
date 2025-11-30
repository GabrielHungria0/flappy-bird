from abc import ABC, abstractmethod


class Event(ABC):
    @abstractmethod
    def execute(self):
        pass


class PipePassedEvent(Event):
    def __init__(self, score):
        self._score = score
    
    @property
    def score(self):
        return self._score
    
    def execute(self):
        pass


class GameOverEvent(Event):
    def execute(self):
        pass


class ResetEvent(Event):
    def execute(self):
        pass


class CollisionEvent(Event):
    def execute(self):
        pass


class JumpEvent(Event):
    def execute(self):
        pass