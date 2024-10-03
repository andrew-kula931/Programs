import pygame

class PlayerPhysics:
    def __init__(self, game, image, pos):
        self.game = game
        self.type = image
        self.pos = list(pos)
        self.velocity = [0, 0]

    def update(self, movement=(0,0)):

        if (self.pos[1] < 750):
            self.velocity[1] = min(30, self.velocity[1] + .7)
        else:
            self.velocity[1] = 0
            self.pos[1] = 750

        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]


    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)