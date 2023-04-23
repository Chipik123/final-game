from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 

     class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()

        if keys[K_w] :
            self.rect.y -= self.speed
        if keys[K_s] :
            self.rect.y += self.speed
    
    def update_r(self):
        keys = key.get_pressed()

        if keys[K_UP] :
            self.rect.y -= self.speed
        if keys[K_DOWN] :
            self.rect.y += self.speed    

player1 = Player("car.png", 20, 200, 50, 200, 5)
