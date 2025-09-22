from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('hero_spritesheet.png')

for x in range (0,800,5):
    clear_canvas()

    update_canvas()

close_canvas()