from pygame import *
from sprite import Sprite
from button import Button
#створи вікно гри
window = display.set_mode((700, 500))
display.set_caption('гонки')

background_image = image.load("background.png")

background = transform.scale(background_image, (700, 500))

background_width = background.get_width()
background_height = background.get_height()

tiles = 2 

scroll = 0

car1 = Sprite(100, 100, 150, 100, "car1.png", 5)
car2 = Sprite(100, 350, 150, 100, "car2.png", 5)

btn1 = Button('start_btn.png',  100, 100, 100, 50)
btn2 = Button('exit_btn.png', 100,300, 100, 50)


game = True

clock = time.Clock()

while game:
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
        
    car1.draw(window)
    car1.move1()
    car2.draw(window)
    car2.move2()

    display.update()
    clock.tick(60)

