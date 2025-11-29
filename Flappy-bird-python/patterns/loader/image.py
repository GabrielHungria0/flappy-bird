import pygame
from patterns.loader.asset import Asset


class ImageAsset(Asset):
    def __init__(self, path: str):
        self._path = path
        self._image = pygame.image.load(path).convert_alpha()
    
    @property
    def path(self):
        return self._path
    
    @property
    def image(self):
        return self._image
    
    @property
    def width(self):
        return self._image.get_width()
    
    @property
    def height(self):
        return self._image.get_height()
    
    def get_rect(self):
        return self._image.get_rect()