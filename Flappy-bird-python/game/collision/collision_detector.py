from abc import ABC, abstractmethod
import pygame


class CollisionDetector(ABC):
    @abstractmethod
    def detect_collision(self, bird, obstacle_group):
        pass


class MaskCollisionDetector(CollisionDetector):
    def detect_collision(self, bird, obstacle_group):
        return pygame.sprite.spritecollide(
            bird, obstacle_group, False, pygame.sprite.collide_mask
        )


class DecoratorAwareCollisionDetector(CollisionDetector):
    def __init__(self):
        self._mask_detector = MaskCollisionDetector()
    
    def detect_collision(self, bird, obstacle_group):
        if hasattr(bird, "check_collision"):
            return bird.check_collision(obstacle_group)
        
        return self._mask_detector.detect_collision(bird, obstacle_group)