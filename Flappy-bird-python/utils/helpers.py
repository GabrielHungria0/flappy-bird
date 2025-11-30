def is_off_screen(sprite):
    
    return sprite.rect[0] < -(sprite.rect[2])