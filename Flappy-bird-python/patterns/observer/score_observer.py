from typing import List
from patterns.event import Event, GameOverEvent, PipePassedEvent, ResetEvent
from patterns.observer.abstract_game_event_observer import AbstractGameEventObserver


class ScoreObserver(AbstractGameEventObserver):
    def __init__(self):
        self._score = 0
    
    def update(self, event: Event):
        handlers = {
            PipePassedEvent: self._handle_pipe_passed,
            GameOverEvent: self._handle_game_over,
            ResetEvent: self._handle_reset
        }
        
        handler = handlers.get(type(event))
        if handler:
            handler(event)
    
    def _handle_pipe_passed(self, event: PipePassedEvent):
        self._score += event.score
    
    def _handle_game_over(self, event: GameOverEvent):
        print(f"Game Over Pontuação final: {self._score}")
    
    def _handle_reset(self, event: ResetEvent):
        self._score = 0
        print("Pontuação resetada!")
    
    def get_score(self):
        return self._score
    
    def get_event_types(self) -> List[type]:
        return [PipePassedEvent, GameOverEvent, ResetEvent]