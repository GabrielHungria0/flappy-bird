import pygame
from config import GameConfig


class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos, resource_facade):
        pygame.sprite.Sprite.__init__(self)
        
        self._config = GameConfig()
        self._setup_image(resource_facade)
        self._setup_position(xpos)
    
    def _setup_image(self, resource_facade):
        self.image = resource_facade.get_image("ground")
        self.image = pygame.transform.scale(
            self.image, 
            (self._config.GROUND_WIDTH, self._config.GROUND_HEIGHT)
        )
        self.mask = pygame.mask.from_surface(self.image)
    
    def _setup_position(self, xpos):
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = self._config.ground_y_position
    
    def update(self):
        self.rect[0] -= self._config.GAME_SPEED