from pygame import *

class Sprite(sprite.Sprite):
    def __init__(self, x, y, wieght, height, image_name, speed):
        self.image = transform.scale( image.load(image_name), (wieght, height))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.speed = speed 
    def draw(self, window):
        window.blit(self.image,(self.rect.x,self.rect.y))

    def move1(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.y < 595:
            self.rect.y += self.speed

    def move2(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_s] and self.rect.y < 395:
            self.rect.y += self.speed

    

