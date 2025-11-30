import pygame
from config import AssetPaths

class ResourceManager:
    def __init__(self):
        self._image_cache = {}
        self._sound_cache = {}

    def load_bird_sprites(self):
        if "bird_sprites" not in self._image_cache:
            self._image_cache["bird_sprites"] = [
                self._load_image(AssetPaths.BIRD_UP_SPRITE),
                self._load_image(AssetPaths.BIRD_MID_SPRITE),
                self._load_image(AssetPaths.BIRD_DOWN_SPRITE)
            ]
        return self._image_cache["bird_sprites"]
    
    def load_pipe_sprite(self):
        return self._get_cached_image("pipe", AssetPaths.PIPE_SPRITE)
    
    def load_ground_sprite(self):
        return self._get_cached_image("ground", AssetPaths.GROUND_SPRITE)
    
    def load_background_sprite(self):
        return self._get_cached_image("background", AssetPaths.BACKGROUND_SPRITE)
    
    def load_message_sprite(self):
        return self._get_cached_image("message", AssetPaths.MESSAGE_SPRITE)
    
    def get_sound_path(self, sound_name):
        sound_map = {
            "wing": AssetPaths.WING_SOUND,
            "hit": AssetPaths.HIT_SOUND
        }
        return sound_map.get(sound_name)
    
    def _get_cached_image(self, key, path):
        if key not in self._image_cache:
            self._image_cache[key] = self._load_image(path)
        return self._image_cache[key]
    
    def _load_image(self, path):
        return pygame.image.load(path).convert_alpha()