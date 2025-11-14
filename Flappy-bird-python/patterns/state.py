"""
Padrão STATE - Gerenciamento de estados do jogo
"""
from abc import ABC, abstractmethod
from enum import Enum
import pygame
from pygame.locals import *
import time
from entities.ground import Ground
from utils.helpers import is_off_screen
from config import SCREEN_WIDHT, GROUND_WIDHT, PIPE_WIDHT


class GameStateEnum(Enum):
    MENU = 1
    PLAYING = 2
    GAME_OVER = 3


class GameState(ABC):
    """Interface para estados do jogo"""
    
    @abstractmethod
    def handle_input(self, game_context, event):
        pass
    
    @abstractmethod
    def update(self, game_context):
        pass
    
    @abstractmethod
    def render(self, game_context, screen):
        pass


class MenuState(GameState):
    """Estado de Menu inicial"""
    
    def handle_input(self, game_context, event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_UP:
                game_context.event_system.notify("JUMP")
                game_context.set_state(PlayingState())
    
    def update(self, game_context):
        game_context.bird.begin()
        game_context.ground_group.update()
        
        if is_off_screen(game_context.ground_group.sprites()[0]):
            game_context.ground_group.remove(game_context.ground_group.sprites()[0])
            new_ground = Ground(GROUND_WIDHT - 20)
            game_context.ground_group.add(new_ground)
    
    def render(self, game_context, screen):
        screen.blit(game_context.background, (0, 0))
        screen.blit(game_context.begin_image, (120, 150))
        game_context.bird_group.draw(screen)
        game_context.ground_group.draw(screen)


class PlayingState(GameState):
    """Estado de jogo ativo"""
    
    def __init__(self):
        self.pipes_passed = set()
    
    def handle_input(self, game_context, event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_UP:
                game_context.bird.bump()
                game_context.event_system.notify("JUMP")
    
    def update(self, game_context):
        game_context.bird_group.update()
        game_context.ground_group.update()
        game_context.pipe_group.update()
        
        # Gerencia ground
        if is_off_screen(game_context.ground_group.sprites()[0]):
            game_context.ground_group.remove(game_context.ground_group.sprites()[0])
            new_ground = Ground(GROUND_WIDHT - 20)
            game_context.ground_group.add(new_ground)
        
        # Gerencia pipes
        if is_off_screen(game_context.pipe_group.sprites()[0]):
            game_context.pipe_group.remove(game_context.pipe_group.sprites()[0])
            game_context.pipe_group.remove(game_context.pipe_group.sprites()[0])
            
            pipes = game_context.obstacle_factory.create_obstacle(SCREEN_WIDHT * 2)
            game_context.pipe_group.add(pipes[0])
            game_context.pipe_group.add(pipes[1])
        
        # Detecta pipes passados para pontuação
        for pipe in game_context.pipe_group:
            if pipe.rect[0] + PIPE_WIDHT < game_context.bird.rect[0] and id(pipe) not in self.pipes_passed:
                self.pipes_passed.add(id(pipe))
                game_context.event_system.notify("PIPE_PASSED")
        
        # Detecta colisões
        if (pygame.sprite.groupcollide(game_context.bird_group, game_context.ground_group, 
                                       False, False, pygame.sprite.collide_mask) or
            pygame.sprite.groupcollide(game_context.bird_group, game_context.pipe_group, 
                                      False, False, pygame.sprite.collide_mask)):
            game_context.event_system.notify("COLLISION")
            game_context.event_system.notify("GAME_OVER")
            time.sleep(1)
            game_context.set_state(GameOverState())
    
    def render(self, game_context, screen):
        screen.blit(game_context.background, (0, 0))
        game_context.bird_group.draw(screen)
        game_context.pipe_group.draw(screen)
        game_context.ground_group.draw(screen)


class GameOverState(GameState):
    """Estado de Game Over"""
    
    def handle_input(self, game_context, event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_RETURN:
                game_context.reset_game()
                game_context.set_state(MenuState())
    
    def update(self, game_context):
        pass
    
    def render(self, game_context, screen):
        screen.blit(game_context.background, (0, 0))
        game_context.bird_group.draw(screen)
        game_context.pipe_group.draw(screen)
        game_context.ground_group.draw(screen)
        
        # Texto de Game Over
        font = pygame.font.Font(None, 74)
        text = font.render('GAME OVER', True, (255, 0, 0))
        screen.blit(text, (50, 250))
        
        font_small = pygame.font.Font(None, 36)
        text_restart = font_small.render('Press SPACE to restart', True, (255, 255, 255))
        screen.blit(text_restart, (60, 320))