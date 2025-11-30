from typing import List
from entities.moving_pipe import MovingPipe
from entities.pipe import Pipe
from patterns.factory.abstract_factory import ObstacleFactory


class MovingPipeFactory(ObstacleFactory):
    def __init__(self, movement_range=40, movement_speed=2):
        super().__init__()
        self._movement_range = movement_range
        self._movement_speed = movement_speed
    
    def create_obstacle(self, xpos, resource_facade) -> List[Pipe]:
        size = self._generate_random_size()
        gap = self._config.PIPE_GAP
        
        pipe_bottom = self._create_moving_pipe(False, xpos, size, resource_facade)
        pipe_top = self._create_moving_pipe(
            True, xpos, self._config.SCREEN_HEIGHT - size - gap, resource_facade
        )
        
        pair_id = self._create_pipe_pair_id()
        self._assign_pair_id([pipe_bottom, pipe_top], pair_id)
        
        return [pipe_bottom, pipe_top]
    
    def _create_moving_pipe(self, inverted, xpos, ysize, resource_facade):
        return MovingPipe(
            inverted, xpos, ysize, resource_facade,
            self._movement_range, self._movement_speed
        )