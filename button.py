from pygame import *

class Button(sprite.Sprite):
    def __init__(self, btn_image_name, x,y , width, height):
        self.image = image.transform(image_load(btn_image_name,),(width, height))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

        self.clicked = False

    def draw(self, window):
        action = False
        pos = mouse.get_pos()

        if self.rect.collidepoint(pos):
            if mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True

        if mouse.get_pressed()[0] == 0:
            self.clicked = False

        window.blit(self.image, (self.rect.x, self.rect))

        return action