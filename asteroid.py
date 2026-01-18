from circleshape import CircleShape
from constants import *
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):

        super().__init__(x, y, radius)

    def draw(self, screen):

        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):

        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:

            return
        
        log_event("asteroid_split")

        random_angle = random.uniform(20, 50)

        vector_one = self.velocity.rotate(random_angle)

        vector_two = self.velocity.rotate(-1 * random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)

        vector_one = vector_one * 1.2

        vector_two = vector_two * 1.2

        asteroid_one.velocity = vector_one

        asteroid_two.velocity = vector_two






