"""
Padrão FACADE - Simplifica gerenciamento de recursos
"""
import pygame
from config import *


class ResourceFacade:
    """Facade que simplifica o carregamento e gerenciamento de recursos"""
    
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self._load_resources()
    
    def _load_resources(self):
        """Carrega todos os recursos do jogo"""
        # Imagens do pássaro
        self.images['bird_up'] = pygame.image.load(BIRD_UP_SPRITE).convert_alpha()
        self.images['bird_mid'] = pygame.image.load(BIRD_MID_SPRITE).convert_alpha()
        self.images['bird_down'] = pygame.image.load(BIRD_DOWN_SPRITE).convert_alpha()
        
        # Outros recursos
        self.images['pipe'] = pygame.image.load(PIPE_SPRITE).convert_alpha()
        self.images['ground'] = pygame.image.load(GROUND_SPRITE).convert_alpha()
        self.images['background'] = pygame.image.load(BACKGROUND_SPRITE)
        self.images['message'] = pygame.image.load(MESSAGE_SPRITE).convert_alpha()
        
        # Sons
        self.sounds['wing'] = WING_SOUND
        self.sounds['hit'] = HIT_SOUND
    
    def get_bird_images(self):
        """Retorna lista de imagens do pássaro"""
        return [self.images['bird_up'], self.images['bird_mid'], self.images['bird_down']]
    
    def get_image(self, name):
        """Retorna uma imagem específica"""
        return self.images.get(name)
    
    def get_sound(self, name):
        """Retorna um som específico"""
        return self.sounds.get(name)
    
    def get_scaled_background(self, width, height):
        """Retorna background escalado"""
        return pygame.transform.scale(self.images['background'], (width, height))