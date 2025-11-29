from typing import Dict
from patterns.loader.asset_loader import AssetLoader
from patterns.loader.sound import SoundAsset


class SoundService:
    def __init__(self):
        self._sounds: Dict[str, SoundAsset] = {}
    
    def play(self, path: str, tag: str):
        sound = self._get_or_load_sound(path, tag)
        sound.play()
    
    def _get_or_load_sound(self, path: str, tag: str):
        if tag not in self._sounds:
            self._sounds[tag] = AssetLoader.load_sound(path)
        return self._sounds[tag]