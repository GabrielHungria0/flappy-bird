from pygame import K_RETURN, K_SPACE, KEYDOWN
import pygame
from patterns.state import GameState


class GameOverState(GameState):
    def __init__(self):
        self._font_large = pygame.font.Font(None, 74)
        self._font_medium = pygame.font.Font(None, 48)
        self._font_small = pygame.font.Font(None, 36)
    
    def handle_input(self, game_context, event):
        if event.type == KEYDOWN and self._is_restart_key(event.key):
            game_context.reset_game()
            game_context.set_menu()
    
    def _is_restart_key(self, key):
        return key in (K_SPACE, K_RETURN)
    
    def update(self, game_context):
        pass
    
    def render(self, game_context, screen):
        self._render_background(game_context, screen)
        self._render_game_over_text(screen)
        self._render_score(game_context, screen)
        self._render_instructions(screen)
    
    def _render_background(self, game_context, screen):
        screen.blit(game_context.background, (0, 0))
        game_context.sprite_manager.draw_group("bird", screen)
        game_context.sprite_manager.draw_group("pipes", screen)
        game_context.sprite_manager.draw_group("ground", screen)
    
    def _render_game_over_text(self, screen):
        text = self._font_large.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text, (50, 200))
    
    def _render_score(self, game_context, screen):
        score = game_context.score_observer.get_score()
        text = self._font_medium.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(text, (120, 280))
    
    def _render_instructions(self, screen):
        text = self._font_small.render("Press SPACE to restart", True, (255, 255, 255))
        screen.blit(text, (60, 350))