from typing import List
from config import AssetPaths
from patterns.event import CollisionEvent, Event, JumpEvent
from patterns.observer.abstract_game_event_observer import AbstractGameEventObserver
from patterns.service.sound_service import SoundService


class SoundObserver(AbstractGameEventObserver):
    def __init__(self):
        self._sound_service = SoundService()
    
    def update(self, event: Event):
        sound_map = {
            CollisionEvent: (AssetPaths.HIT_SOUND, "hit"),
            JumpEvent: (AssetPaths.WING_SOUND, "wing")
        }
        
        sound_data = sound_map.get(type(event))
        if sound_data:
            self._sound_service.play(*sound_data)
    
    def get_event_types(self) -> List[type]:
        return [CollisionEvent, JumpEvent]