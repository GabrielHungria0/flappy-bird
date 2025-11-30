from abc import ABC, abstractmethod
from typing import List
from patterns.event import Event


class AbstractGameEventObserver(ABC):
    @abstractmethod
    def get_event_types(self) -> List[type]:
        pass
    
    @abstractmethod
    def update(self, event: Event):
        pass
    
    def can_handle(self, event: Event) -> bool:
        return type(event) in self.get_event_types()