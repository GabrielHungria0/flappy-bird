import pygame
from game.managers.resource_manager import ResourceManager
from patterns.loader.asset_loader import AssetLoader

class ResourceFacade:
    def __init__(self):
        self._resource_manager = ResourceManager()
        self._asset_loader = AssetLoader()

    def get_bird_images(self):
        return self._resource_manager.load_bird_sprites()
    
    def get_image(self, name):
        image_methods = {
            "pipe": self._resource_manager.load_pipe_sprite,
            "ground": self._resource_manager.load_ground_sprite,
            "background": self._resource_manager.load_background_sprite,
            "message": self._resource_manager.load_message_sprite
        }
        method = image_methods.get(name)
        return method() if method else None
    
    def get_sound(self, name):
        sound_path = self._resource_manager.get_sound_path(name)
        if sound_path:
            return self._asset_loader.load_sound(sound_path)
        return None