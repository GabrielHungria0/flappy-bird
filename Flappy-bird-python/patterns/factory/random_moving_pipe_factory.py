import random
from typing import List
from entities.pipe import Pipe
from patterns.factory.moving_pipe_factory import MovingPipeFactory


class RandomMovingPipeFactory(MovingPipeFactory):
    def __init__(self):
        movement_range = random.randint(30, 70)
        movement_speed = random.uniform(1.5, 3.5)
        super().__init__(movement_range, movement_speed)