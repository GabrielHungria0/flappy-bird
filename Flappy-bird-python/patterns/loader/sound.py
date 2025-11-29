import pygame
from patterns.loader.asset import Asset


class SoundAsset(Asset):
    def __init__(self, path: str):
        self._sound = pygame.mixer.Sound(path)
    
    def play(self):
        self._sound.play()