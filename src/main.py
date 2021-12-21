import pygame
from player import Player
from utils import load_image, log


class Game:
    def __init__(self):
        log.info("Game Init!")
        pygame.init()
        self.win = pygame.display.set_mode((0, 0))
        pygame.display.set_caption("Project March")
        self.screen_width = self.win.get_width()
        self.screen_height = self.win.get_height()
        self.bg = load_image("Background.png")
        self.bg = pygame.transform.scale(self.bg, (1920, 1080))
        self.clock = pygame.time.Clock()
        self.running = True
        self.man = Player(100, 970, 64, 64)

    def process_game_events(self):
        events = pygame.event.get()
        log.debug(f"events: {events!r}")
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.man.x > self.man.vel:
            self.man.x -= man.vel
            self.man.left = True
            self.man.right = False
        elif keys[pygame.K_RIGHT] and self.man.x < self.screen_width - self.man.width - self.man.vel:
            self.man.x += self.man.vel
            self.man.right = True
            self.man.left = False
        else:
            self.man.right = False
            self.man.left = False
            self.man.walkCount = 0

        if not self.man.isJump:
            if keys[pygame.K_SPACE]:
                self.man.isJump = True
                self.man.right = False
                self.man.left = False
                self.man.walkCount = 0
        else:
            if self.man.jumpCount >= -10:
                neg = 1
                if self.man.jumpCount < 0:
                    neg = -1
                self.man.y -= (self.man.jumpCount ** 2) * 0.35 * neg
                self.man.jumpCount -= 1
            else:
                self.man.isJump = False
                self.man.jumpCount = 10

    def redrawGameWindow(self):
        log.debug("window update")
        self.win.blit(self.bg, (0, 0))
        self.man.draw(self.win)
        pygame.display.update()

    def run(self):
        log.info("Start running")
        self.running = True
        while self.running:
            self.clock.tick(23)
            self.process_game_events()
            self.redrawGameWindow()
        log.info("Stop Game")
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
