"""
Padrão FACTORY METHOD - Criação de obstáculos
"""
from abc import ABC, abstractmethod
import random
from entities.pipe import Pipe
from config import SCREEN_HEIGHT, PIPE_GAP


class ObstacleFactory(ABC):
    """Factory abstrata para criar obstáculos"""
    
    @abstractmethod
    def create_obstacle(self, xpos):
        pass


class PipeFactory(ObstacleFactory):
    """Factory concreta para criar pipes normais"""
    
    def create_obstacle(self, xpos):
        size = random.randint(100, 300)
        pipe_bottom = Pipe(False, xpos, size)
        pipe_top = Pipe(True, xpos, SCREEN_HEIGHT - size - PIPE_GAP)
        return [pipe_bottom, pipe_top]


class NarrowPipeFactory(ObstacleFactory):
    """Factory concreta para criar pipes com gap menor (mais difícil)"""
    
    def create_obstacle(self, xpos):
        size = random.randint(100, 300)
        narrow_gap = PIPE_GAP - 30
        pipe_bottom = Pipe(False, xpos, size)
        pipe_top = Pipe(True, xpos, SCREEN_HEIGHT - size - narrow_gap)
        return [pipe_bottom, pipe_top]