from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):

    def __init___(self, x, y):

        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):

        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        
        self.position += self.velocity * dt
