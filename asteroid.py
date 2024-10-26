import pygame
from constants import *
from circleshape import CircleShape
import random
image_path = 'circle.png'

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        #self.circle_image = pygame.image.load(image_path).convert_alpha()
    def draw(self, screen):
        #scaled = pygame.transform.scale(self.circle_image,(self.radius,self.radius))
        #centrum = scaled.get_rect(center=(self.position.x,self.position.y))
        #screen.blit(scaled, centrum.topleft)
        pygame.draw.circle(screen,'red',self.position,self.radius,0)
    #def move(self,dt):
        #forward = pygame.Vector2(0, 1).rotate(self.rotation)
        #self.position += forward * PLAYER_SPEED * dt
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        a = self.velocity.rotate(angle)
        b = self.velocity.rotate(-angle)
        N_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid = Asteroid(self.position.x,self.position.y,N_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x,self.position.y,N_radius)
        asteroid.velocity = b * 1.2

    

    

