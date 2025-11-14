"""
Funções auxiliares do jogo
"""
def is_off_screen(sprite):
    """Verifica se um sprite saiu da tela"""
    return sprite.rect[0] < -(sprite.rect[2])