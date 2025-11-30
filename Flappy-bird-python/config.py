class GameConfig:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        self.SCREEN_WIDTH = 400
        self.SCREEN_HEIGHT = 600
        self.SPEED = 20
        self.GRAVITY = 2.5
        self.GAME_SPEED = 15
        self.GROUND_WIDTH = 2 * self.SCREEN_WIDTH
        self.GROUND_HEIGHT = 100
        self.PIPE_WIDTH = 80
        self.PIPE_HEIGHT = 500
        self.PIPE_GAP = 150
        
    @property
    def ground_y_position(self):
        return self.SCREEN_HEIGHT - self.GROUND_HEIGHT


class LayerConfig:
    BG_LAYER = 0
    PIPE_LAYER = 1
    BIRD_LAYER = 2


class AssetPaths:
    WING_SOUND = "assets/audio/wing.wav"
    HIT_SOUND = "assets/audio/hit.wav"
    BIRD_UP_SPRITE = "assets/sprites/bluebird-upflap.png"
    BIRD_MID_SPRITE = "assets/sprites/bluebird-midflap.png"
    BIRD_DOWN_SPRITE = "assets/sprites/bluebird-downflap.png"
    PIPE_SPRITE = "assets/sprites/pipe-green.png"
    GROUND_SPRITE = "assets/sprites/base.png"
    BACKGROUND_SPRITE = "assets/sprites/background-day.png"
    MESSAGE_SPRITE = "assets/sprites/message.png"