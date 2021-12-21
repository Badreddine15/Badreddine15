import pygame
from utils import IMAGES_DIR


def load_image(filename):
    return pygame.image.load(str(IMAGES_DIR.joinpath(filename)))


class Player(object):
    def __init__(self, x, y, width, height):
        self.walkRight = [load_image("R"+str(i)+".png") for i in range(1, 9)]
        self.walkLeft = [load_image("L"+str(i)+".png") for i in range(1, 9)]
        self.char = load_image('idle outline.gif')
        self.jumpima = load_image('jump outline.png')
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self, win):
        if self.walkCount + 1 >= 23:
            self.walkCount = 0

        if self.left:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.isJump:
            win.blit(self.jumpima, (self.x, self.y))
        else:
            win.blit(self.char, (self.x, self.y))
