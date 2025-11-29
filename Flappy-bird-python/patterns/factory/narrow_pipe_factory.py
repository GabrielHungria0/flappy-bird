from typing import List
from entities.pipe import Pipe
from patterns.factory.abstract_factory import PipeFactory


class NarrowPipeFactory(PipeFactory):
    def __init__(self, gap_reduction=30):
        super().__init__()
        self._gap_reduction = gap_reduction
    
    def create_obstacle(self, xpos, resource_facade) -> List[Pipe]:
        size = self._generate_random_size()
        narrow_gap = self._config.PIPE_GAP - self._gap_reduction
        
        pipe_bottom = Pipe(False, xpos, size, resource_facade)
        pipe_top = Pipe(
            True, xpos, self._config.SCREEN_HEIGHT - size - narrow_gap, resource_facade
        )
        
        pair_id = self._create_pipe_pair_id()
        self._assign_pair_id([pipe_bottom, pipe_top], pair_id)
        
        return [pipe_bottom, pipe_top]