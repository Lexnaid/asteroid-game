from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
        
    def draw(self, screen):
        return pygame.draw.circle(screen, radius=self.radius, width=2, color='red', center=self.position)
    
    def update(self, dt):
        self.position += self.velocity * dt 
    
    def split(self,):
        self.kill()
        if ASTEROID_MIN_RADIUS >= self.radius:
            return
        else:
            rand = random.uniform(20,50)
            angle1 = self.velocity.rotate(-rand)
            angle2 = self.velocity.rotate(rand)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_velocity1 = pygame.Vector2(angle1) * 1.2
            new_velocity2 = pygame.Vector2(angle2) * 1.2
            Asteroid(self.x, self.y, new_radius, new_velocity1)
            Asteroid(self.x, self.y, new_radius, new_velocity2)