import pygame
import math
from pygame.locals import *
from cutscene import CutSceneManager, CutSceneOne



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




class gun:
    def __init__(self,x ,y):
        self.x = x
        self.y = y
        self.image = player_weapon
    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

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


        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        player_weapon_copy = pygame.transform.rotate(player_weapon, angle)
        win.blit(player_weapon_copy, (self.x + 15 - int(player_weapon_copy.get_width() / 2), self.y + 25-int(player_weapon_copy.get_height()/2)))


    def update(self, cut_scene_manager):
        keys = pygame.key.get_pressed()
        if cut_scene_manager.cut_scene is None:
            if keys[pygame.K_LEFT] or keys[pygame.K_q] and self.x > self.vel:
                self.x -= self.vel
                self.left = True
                self.right = False
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and self.x < x1 - self.width - self.vel:
                self.x += self.vel
                self.right = True
                self.left = False
            else:
                self.right = False
                self.left = False
                self.walkCount = 0

            if not (self.isJump):
                if keys[pygame.K_SPACE]:
                    self.isJump = True
                    self.right = False
                    self.left = False
                    self.walkCount = 0
            else:
                if self.jumpCount >= -10:
                    neg = 1
                    if self.jumpCount < 0:
                        neg = -1
                    self.y -= (self.jumpCount ** 2) * 0.35 * neg
                    self.jumpCount -= 1
                else:
                    self.isJump = False
                    self.jumpCount = 10
            if npc1.x - self.x <= 45 and npc1.x - self.x >= -45:
                self.is_onnpc = True
                if self.is_onnpc:
                    cut_scene_manager.start_cut_scene(CutSceneOne(self))


            if self.x == gun1.x:
                self.is_onitem = True
                if self.is_onitem:
                    self.handle_weapons(win)

            else:
                print(self.is_onitem)

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
    cut_scene_manager.draw()

    pygame.display.update()


man = player(0, 700, 64, 64)
npc1 = npc_(500, 700)
gun1 = gun(400, 700)
cut_scene_manager = CutSceneManager(win)
arme = man.handle_weapons(win)
run = True
while run:
    clock.tick(23)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    man.update(cut_scene_manager)
    cut_scene_manager.update()
    npc1.update(man)
    npc1.draw(win)
    redrawGameWindow()

pygame.quit()