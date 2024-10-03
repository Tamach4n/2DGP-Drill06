from pico2d import *
from random import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
HAND_WIDTH2, HAND_HEIGHT2 = 25, 26  #   밑변/2, 높이/2
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
hand = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

def randomHand():
    global hx, hy
    
    hx = randint(0 + HAND_WIDTH2, TUK_WIDTH - HAND_WIDTH2)
    hy = randint(0 + HAND_HEIGHT2, TUK_HEIGHT - HAND_HEIGHT2)

def handle_events():
    global running
    global x, y

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def mukai():
    global x, y, hx, hy, oldX, oldY, touchaku

    sx, sy = hx - HAND_WIDTH2, hy + HAND_HEIGHT2
    dx, dy = (sx - oldX) / 100, (sy - oldY) / 100

    x += dx
    y += dy

    if(round(x) == sx and round(y) == sy):
        touchaku = True
        print(round(x), round(y), "도착")


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hx, hy = 0, 0
oldX, oldY = 0, 0
frame = 0
touchaku = True

hide_cursor()

while running:
    clear_canvas()
    
    if(touchaku):
        randomHand()
        oldX, oldY = x, y
        touchaku = False

    mukai()

    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    hand.draw(hx, hy)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

    delay(0.01)

close_canvas()