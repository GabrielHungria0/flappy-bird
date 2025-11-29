from typing import Dict
from patterns.loader.sound import SoundAsset

class SoundService:
    def __init__(self):
        self._sounds: Dict[str, SoundAsset] = {}
        
    def play(self, sound_asset: SoundAsset, tag: str):
        if tag not in self._sounds:
            self._sounds[tag] = sound_asset
        self._sounds[tag].play()