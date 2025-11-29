import pygame
from config import GameConfig, AssetPaths


class ResourceFacade:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self._images = {}
            self._sounds = {}
            self._initialized = True
    
    def get_bird_images(self):
        if "bird_sprites" not in self._images:
            self._load_bird_images()
        return self._images["bird_sprites"]
    
    def get_image(self, name):
        key_map = {
            "pipe": AssetPaths.PIPE_SPRITE,
            "ground": AssetPaths.GROUND_SPRITE,
            "background": AssetPaths.BACKGROUND_SPRITE,
            "message": AssetPaths.MESSAGE_SPRITE
        }
        
        if name not in self._images and name in key_map:
            self._images[name] = pygame.image.load(key_map[name]).convert_alpha()
        
        return self._images.get(name)
    
    def get_sound(self, name):
        key_map = {
            "wing": AssetPaths.WING_SOUND,
            "hit": AssetPaths.HIT_SOUND
        }
        return key_map.get(name)
    
    def get_scaled_background(self, width, height):
        bg = self.get_image("background")
        return pygame.transform.scale(bg, (width, height))
    
    def _load_bird_images(self):
        self._images["bird_sprites"] = [
            pygame.image.load(AssetPaths.BIRD_UP_SPRITE).convert_alpha(),
            pygame.image.load(AssetPaths.BIRD_MID_SPRITE).convert_alpha(),
            pygame.image.load(AssetPaths.BIRD_DOWN_SPRITE).convert_alpha()
        ]