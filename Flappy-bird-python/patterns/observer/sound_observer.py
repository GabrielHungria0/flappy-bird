from typing import List
from patterns.event import CollisionEvent, Event, JumpEvent
from patterns.observer.abstract_game_event_observer import AbstractGameEventObserver
from patterns.service.sound_service import SoundService

class SoundObserver(AbstractGameEventObserver):
    def __init__(self, resource_facade):
        self._sound_service = SoundService()
        self._resource_facade = resource_facade

    def update(self, event: Event):
        sound_map = {
            CollisionEvent: "hit",
            JumpEvent: "wing"
        }
        sound_name = sound_map.get(type(event))
        if sound_name:
            sound_asset = self._resource_facade.get_sound(sound_name)
            if sound_asset:
                self._sound_service.play(sound_asset, sound_name)
                
    def get_event_types(self) -> List[type]:
        return [CollisionEvent, JumpEvent]