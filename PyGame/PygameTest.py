import sys
import pygame

# pygame setup
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1600, 900))
        self.clock = pygame.time.Clock()
        self.dt = 0

        pygame.display.set_caption('Starter Game')
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
            
        self.test_image = pygame.image.load("images/test2.png")
        self.image_pos = [100, 200]

    def run(self):
        while True:
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("purple")

            self.screen.blit(self.test_image, self.image_pos)

            pygame.draw.circle(self.screen, "red", self.player_pos, 40)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player_pos.y -= 300 * dt
                self.image_pos[1] -= 300 * dt
            if keys[pygame.K_s]:
                self.player_pos.y += 300 * dt
                self.image_pos[1] += 300 * dt
            if keys[pygame.K_a]:
                self.player_pos.x -= 300 * dt
                self.image_pos[0] -= 300 * dt
            if keys[pygame.K_d]:
                self.player_pos.x += 300 * dt
                self.image_pos[0] += 300 * dt

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = self.clock.tick(60) / 1000

Game().run()