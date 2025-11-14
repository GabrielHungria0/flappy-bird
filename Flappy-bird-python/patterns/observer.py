"""
Padrão OBSERVER - Sistema de eventos do jogo
"""
from abc import ABC, abstractmethod
import pygame
from config import HIT_SOUND, WING_SOUND


class GameEventObserver(ABC):
    """Interface para observers de eventos do jogo"""
    
    @abstractmethod
    def update(self, event_type, data=None):
        pass


class ScoreObserver(GameEventObserver):
    """Observer que gerencia a pontuação"""
    
    def __init__(self):
        self.score = 0
    
    def update(self, event_type, data=None):
        if event_type == "PIPE_PASSED":
            self.score += 1
            print(f"🎯 Pontuação: {self.score}")
        elif event_type == "GAME_OVER":
            print(f"💀 Game Over! Pontuação final: {self.score}")
            self.score = 0


class SoundObserver(GameEventObserver):
    """Observer que gerencia sons do jogo"""
    
    def update(self, event_type, data=None):
        if event_type == "COLLISION":
            pygame.mixer.music.load(HIT_SOUND)
            pygame.mixer.music.play()
        elif event_type == "JUMP":
            pygame.mixer.music.load(WING_SOUND)
            pygame.mixer.music.play()


class GameEventSubject:
    """Subject que notifica observers sobre eventos"""
    
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self, event_type, data=None):
        for observer in self._observers:
            observer.update(event_type, data)
            