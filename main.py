# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from circleshape import CircleShape
from player import player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot





def main():
    user = input('Enter you name:')
    print('Starting asteroids!')
    print(f'welcome {user}')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.HWSURFACE | pygame.DOUBLEBUF)
    pygame.display.set_caption("Optimized Image Scaling")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,36)
    score = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots =pygame.sprite.Group()

    
    

    Asteroid.containers = (asteroids, updatable, drawable) 
    AsteroidField.containers = (updatable)   
    player.containers = (updatable,drawable)
    Shot.containers = (updatable,drawable,shots)

    Playera = player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    Asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        for asteroid in asteroids:
            if asteroid.col_check(Playera) < (Playera.radius + asteroid.radius):
                print('Game over!')
                with open('scores.txt', 'a') as file:
                    file.write(f"\n{user} = {score}")
                sys.exit()
            for shoot in shots:
                if asteroid.col_check(shoot) <= (shoot.radius + asteroid.radius):
                    asteroid.split()
                    shoot.kill()
                    score += 1
        
        screen.fill('black')

        for obj in drawable:
            obj.draw(screen)
        
        score_text = font.render(f"Score: {score}",True,'white')
        fps = font.render(f"fps:{clock}",True,'white')
        imag = [score_text,fps]
        Positions = [(10,10),(SCREEN_WIDTH/5,10)]
        for i in range(len(imag)):
            screen.blit(imag[i], Positions[i])

        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
