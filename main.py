import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import random
import sys

def main():
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
 
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	all_shots = pygame.sprite.Group()
 
	Asteroid.containers = (asteroids, updatable, drawable)
	Player.containers = (updatable, drawable)	
	AsteroidField.containers = (updatable,)
	Shot.containers = (all_shots, updatable, drawable)

	player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, radius=PLAYER_RADIUS, all_shots=all_shots)
	asteroidfield = AsteroidField()

	dt = 0
	clock = pygame.time.Clock()	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	color = (0,0,0)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(color)
		for x in drawable:
			x.draw(screen)
		updatable.update(dt)
		
		for z in asteroids:
			if z.collision(player):
				print('Game over!')
				sys.exit()
		for y in all_shots:
			y.update(dt)
			y.draw(screen)
		
		for x in all_shots:
			for z in asteroids:
				if x.collision(z):
					z.split()
					z.kill()
					x.kill()
    
    
		pygame.display.flip()	
		dt = clock.tick(60) / 1000

  
if __name__ == "__main__":
	main()
