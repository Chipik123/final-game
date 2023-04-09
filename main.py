from pygame import *
from button import Button

window = display.set_mode((700,800))
FPS = 60

game = True

btn1 = Button("start_btn.png", 100,100,100,50)




display.update()
clock.tick(FPS)