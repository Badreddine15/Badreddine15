import pygame
from player import Player
from utils import IMAGES_DIR
pygame.init()

win = pygame.display.set_mode((0, 0))
pygame.display.set_caption("Project March")

x1 = win.get_width()
y1 = win.get_height()

bg = pygame.image.load(str(IMAGES_DIR.joinpath('Background.png')))
bg = pygame.transform.scale(bg, (1920, 1080))

clock = pygame.time.Clock()




run = True


def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)

    pygame.display.update()


man = Player(100, 970, 64, 64)
run = True
while run:
    clock.tick(23)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < x1 - man.width - man.vel:
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

    redrawGameWindow()

pygame.quit()

