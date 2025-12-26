from circleshape import CircleShape
from constants import ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS
from logger import log_event
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 200), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position = self.position + self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)

        a1.velocity = self.velocity.rotate(angle) * 1.2
        a2.velocity = self.velocity.rotate(-angle) * 1.2
