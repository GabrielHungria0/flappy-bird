from abc import ABC, abstractmethod
from patterns.factory import (
    PipeFactory,
    MovingPipeFactory,
    NarrowPipeFactory,
    AlternatingMovingPipeFactory
)


class DifficultyLevel(ABC):
    def __init__(self):
        self._next_level = None
    
    def set_next(self, level):
        self._next_level = level
        return level
    
    @abstractmethod
    def get_threshold(self):
        pass
    
    @abstractmethod
    def create_factory(self):
        pass
    
    def handle(self, score, current_factory):
        if score >= self.get_threshold():
            if self._next_level:
                return self._next_level.handle(score, current_factory)
            return self._get_factory_if_different(current_factory)
        
        return self._get_factory_if_different(current_factory)
    
    def _get_factory_if_different(self, current_factory):
        new_factory = self.create_factory()
        if not isinstance(current_factory, type(new_factory)):
            return new_factory
        return current_factory


class Level1(DifficultyLevel):
    def get_threshold(self):
        return 0
    
    def create_factory(self):
        return PipeFactory()


class Level2(DifficultyLevel):
    def get_threshold(self):
        return 3
    
    def create_factory(self):
        return MovingPipeFactory()


class Level3(DifficultyLevel):
    def get_threshold(self):
        return 6
    
    def create_factory(self):
        return NarrowPipeFactory()


class Level4(DifficultyLevel):
    def get_threshold(self):
        return 10
    
    def create_factory(self):
        return AlternatingMovingPipeFactory()


class DifficultyManager:
    def __init__(self):
        self._last_score = 0
        self._chain = self._build_chain()
    
    def _build_chain(self):
        level1 = Level1()
        level2 = Level2()
        level3 = Level3()
        level4 = Level4()
        
        level1.set_next(level2).set_next(level3).set_next(level4)
        return level1
    
    def get_factory_for_score(self, score, current_factory):
        if score == self._last_score:
            return current_factory
        
        self._last_score = score
        return self._chain.handle(score, current_factory)