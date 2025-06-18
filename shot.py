from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        
    def draw(self, screen):
        return pygame.draw.circle(screen, radius=self.radius, width=2, color='blue', center=self.position)
    
    def update(self, dt):
        self.position += self.velocity * dt 