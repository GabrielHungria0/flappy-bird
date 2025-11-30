from typing import List
from entities.moving_pipe import MovingPipe
from entities.pipe import Pipe
from patterns.factory.moving_pipe_factory import MovingPipeFactory


class AlternatingMovingPipeFactory(MovingPipeFactory):
    def create_obstacle(self, xpos, resource_facade) -> List[Pipe]:
        pipes = super().create_obstacle(xpos, resource_facade)
        
        if len(pipes) > 1 and isinstance(pipes[1], MovingPipe):
            pipes[1]._movement_direction = -1
        
        return pipes