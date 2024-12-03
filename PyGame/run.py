import sys
import pygame

from scripts.utils import load_image
from scripts.player import PlayerPhysics

# pygame setup
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((320, 240))
        self.clock = pygame.time.Clock()
        self.dt = 0

        pygame.display.set_caption('Starter Game')
            
        self.movement = [False, False]
        self.velocity = [0, 0]

        self.assets = {
            'player': load_image('player.png')
        }

        self.player = PlayerPhysics(self, 'player', (200,200))

    def run(self):
        while True:
            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill((110, 30, 30))

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.velocity[1] = -18
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            self.clock.tick(60)

Game().run()