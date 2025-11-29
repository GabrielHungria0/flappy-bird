import pygame
from config import GameConfig
from entities.bird import Bird
from entities.ground import Ground
from patterns.event import ResetEvent
from patterns.facade import ResourceFacade
from patterns.factory import PipeFactory
from game.managers import PipeManager, GroundManager
from patterns.observer import GameEventSubject, ScoreObserver, SoundObserver
from game.sprite_manager import SpriteManager
from patterns.state.game_over_state import GameOverState
from patterns.state.menu_state import MenuState
from patterns.state.playing_state import PlayingState

class GameContext:
    def __init__(self):
        self._config = GameConfig()
        self._initialize_systems()
        self._initialize_resources()
        self._initialize_entities()
        self._state = MenuState()

    def _initialize_systems(self):
        self.event_system = GameEventSubject()
        self.score_observer = ScoreObserver()
        self.sprite_manager = SpriteManager()
        self.sprite_manager.create_group("bird")
        self.sprite_manager.create_group("ground")
        self.sprite_manager.create_group("pipes")

    def _initialize_resources(self):
        self.resource_facade = ResourceFacade()
        self.sound_observer = SoundObserver(self.resource_facade)
        self.event_system.attach(self.score_observer)
        self.event_system.attach(self.sound_observer)
        bg_image = self.resource_facade.get_image("background")
        self.background = pygame.transform.scale(
            bg_image,
            (self._config.SCREEN_WIDTH, self._config.SCREEN_HEIGHT)
        )
        self.begin_image = self.resource_facade.get_image("message")

    def _initialize_entities(self):
        self._initialize_bird()
        self._initialize_ground()
        self._initialize_pipes()

    def _initialize_bird(self):
        self.bird = Bird(self.resource_facade)
        self.sprite_manager.add_to_group("bird", self.bird)

    def _initialize_ground(self):
        self.ground_manager = GroundManager(self.sprite_manager)
        for i in range(2):
            ground = Ground(self._config.GROUND_WIDTH * i, self.resource_facade)
            self.sprite_manager.add_to_group("ground", ground)

    def _initialize_pipes(self):
        obstacle_factory = PipeFactory()
        self.pipe_manager = PipeManager(self.sprite_manager, obstacle_factory)
        for i in range(2):
            self.pipe_manager.add_pair(
                self._config.SCREEN_WIDTH * i + 800,
                self.resource_facade
            )

    def _set_state(self, state):
        self._state = state

    def handle_input(self, event):
        self._state.handle_input(self, event)

    def update(self):
        self._state.update(self)

    def render(self, screen):
        self._state.render(self, screen)

    def play(self):
        self._set_state(PlayingState())

    def game_over(self):
        self._set_state(GameOverState())

    def set_menu(self):
        self._set_state(MenuState())

    def reset_game(self):
        self.event_system.notify(ResetEvent())
        self._reset_bird()
        self._reset_pipes()

    def _reset_bird(self):
        self.sprite_manager.clear_group("bird")
        self.bird = Bird(self.resource_facade)
        self.sprite_manager.add_to_group("bird", self.bird)

    def _reset_pipes(self):
        self.sprite_manager.clear_group("pipes")
        self.pipe_manager = PipeManager(self.sprite_manager, PipeFactory())
        self.pipe_manager.reset()
        for i in range(2):
            self.pipe_manager.add_pair(
                self._config.SCREEN_WIDTH * i + 800,
                self.resource_facade
            )