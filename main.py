import pygame
import math
from pygame.locals import *


pygame.init()
true_scroll = [0,0]
win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Project March")

x1 = win.get_width()
y1 = win.get_height()


walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png')]
bg = pygame.image.load('background_image.png')
bg =pygame.transform.scale(bg, (800, 800))
char = pygame.image.load('idle outline.gif')
npc = pygame.image.load('npc_2.png')
npc_left = pygame.image.load('npc_left.png')
npc_right = pygame.image.load('npc_right.png')
jumpima = pygame.image.load('jump outline.png')
player_weapon = pygame.image.load('Diana Raptor 4.png')
player_weapon = pygame.transform.scale(player_weapon, (32, 32))


clock = pygame.time.Clock()



def draw_speech_bubble(win, text, text_colour, bg_colour, pos, size):

    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, text_colour)
    text_rect = text_surface.get_rect(midbottom=pos)

    # background
    bg_rect = text_rect.copy()
    bg_rect.inflate_ip(10, 10)

    # Frame
    frame_rect = bg_rect.copy()
    frame_rect.inflate_ip(4, 4)

    pygame.draw.rect(win, text_colour, frame_rect)
    pygame.draw.rect(win, bg_colour, bg_rect)
    win.blit(text_surface, text_rect)



class player:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.is_onnpc = False
        self.is_onitem = False
        self.walkCount = 0
        self.jumpCount = 10
        self.rect = char.get_rect()


    def handle_weapons(self, win):
        mouse_x, mouse_y = pygame.mouse.get_pos()


        rel_x, rel_y = mouse_x - man.x, mouse_y - man.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        player_weapon_copy = pygame.transform.rotate(player_weapon, angle)
        win.blit(player_weapon_copy, (self.x + 15 - int(player_weapon_copy.get_width() / 2), self.y + 25-int(player_weapon_copy.get_height()/2)))




    def draw(self, win):
        if self.walkCount + 1 >= 23:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.isJump :
            win.blit(jumpima, (self.x, self.y))
        else:
            win.blit(char, (self.x, self.y))





class npc_ :
    def __init__(self, x ,y):
        self.x = x
        self.y = y
        self.rect = npc.get_rect(topleft=(400, win.get_height()))
        self.speaking = False
        self.image = pygame.Surface(npc_left.get_size(), pygame.SRCALPHA)
    def update(self, man):



        if abs(man.x - self.x) < 100:
            self.speaking = True
        else:
            self.speaking = False

        if man.x < self.x:
            self.image = npc_left

        else:
            self.image = npc_right


    def draw(self, win):

        win.blit(self.image, (self.x, self.y))




def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    npc1.draw(win)


    pygame.display.update()


man = player(0, 700, 64, 64)
npc1 = npc_(500, 700)
run = True
while run:
    clock.tick(23)

    true_scroll[0] += (man.x - true_scroll[0] - 152) / 20
    true_scroll[1] += (man.y - true_scroll[1] - 106) / 20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_q] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT]or keys[pygame.K_d] and man.x < x1 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0

    if not (man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.35 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    if npc1.x - man.x  <=45 and npc1.x - man.x >= -45:
        man.is_onnpc = True
        draw_speech_bubble(win, "Hello Player", (255, 255, 0), (175, 175, 0), npc1.rect.midtop, 25)
        print("1")


    npc1.update(man)
    npc1.draw(win)
    redrawGameWindow()

pygame.quit()