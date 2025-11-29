from config import GameConfig
from entities.ground import Ground


class GroundManager:
    def __init__(self, sprite_manager):
        self._config = GameConfig()
        self._sprite_manager = sprite_manager
    
    def update_ground(self, resource_facade):
        grounds = self._sprite_manager.get_sprites("ground")
        if not grounds:
            return
        
        left_ground = min(grounds, key=lambda g: g.rect[0])
        
        if self._is_off_screen(left_ground):
            self._sprite_manager.remove_from_group("ground", left_ground)
            self._add_new_ground(resource_facade)
    
    def _is_off_screen(self, sprite):
        return sprite.rect[0] < -(sprite.rect[2])
    
    def _add_new_ground(self, resource_facade):
        new_ground = Ground(self._config.GROUND_WIDTH - 20, resource_facade)
        self._sprite_manager.add_to_group("ground", new_ground)