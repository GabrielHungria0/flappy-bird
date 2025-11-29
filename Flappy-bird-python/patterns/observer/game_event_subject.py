from typing import Dict, List
from patterns.event import Event
from patterns.observer.abstract_game_event_observer import AbstractGameEventObserver


class GameEventSubject:
    def __init__(self):
        self._observers: Dict[type, List[AbstractGameEventObserver]] = {}
    
    def attach(self, observer: AbstractGameEventObserver):
        for event_type in observer.get_event_types():
            self._ensure_observer_list_exists(event_type)
            self._observers[event_type].append(observer)
    
    def detach(self, observer: AbstractGameEventObserver):
        for event_type in observer.get_event_types():
            if self._has_observers_for_event(event_type):
                self._remove_observer(event_type, observer)
    
    def notify(self, event: Event):
        event_type = type(event)
        if self._has_observers_for_event(event_type):
            self._notify_observers(event_type, event)
    
    def _ensure_observer_list_exists(self, event_type):
        if event_type not in self._observers:
            self._observers[event_type] = []
    
    def _has_observers_for_event(self, event_type):
        return event_type in self._observers
    
    def _remove_observer(self, event_type, observer):
        if observer in self._observers[event_type]:
            self._observers[event_type].remove(observer)
    
    def _notify_observers(self, event_type, event):
        for observer in self._observers[event_type]:
            observer.update(event)