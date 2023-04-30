from pygame import *

#створи вікно гри
window = display.set_mode((700, 500))
display.set_caption('гонки')

background_image = image.load("background.png")

background = transform.scale(background_image, (700, 500))

background_width = background.get_width()
background_height = background.get_height()

tiles = 2 

scroll = 0

speed = 5

car1_image = transform.scale(
    image.load("car1.png"),
    (100, 100))
car2_image = transform.scale(
    image.load('car2.png'),
    (100, 100))

x1 = 50
y1 = 50

x2, y2 = 50, 350

game = True

clock = time.Clock()

while game:
    window.blit(background, (0,0))
    window.blit(car1_image,(x1,y1))
    window.blit(car2_image,(x2,y2))
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_LEFT:
                scroll -= 5
    
        for i in range(0, tiles):
            window.blit(background, (i * background_width + scroll, 0))
    
        if abs(scroll) > background_width:
            scroll = 0
        scroll -= 5

    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed

    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed

    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed

    if keys_pressed[K_DOWN] and y1 < 595:
        y1 += speed

    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed

    if keys_pressed[K_d] and x2 < 595:
        x2 += speed 
    
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed

    if keys_pressed[K_s] and y2 < 395:
        y2 += speed

    display.update()
    clock.tick(60)

