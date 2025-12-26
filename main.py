# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteriod import Asteroid
from asteriodfield import AsteroidField
from shot import Shot
from constants import *
from logger import log_state, log_event
from player import *
from sys import exit

def main():
    FPS = 60

    # Initialize the pygame library
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # create containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)
    # end of initialization

    # Game loop
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collide_with(asteroid):
                log_event("player_hit")
                print("Game Over!")
                exit()
            for shot in shots:
                if shot.collide_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)

        dt = clock.tick(FPS)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        pygame.display.flip()

        # limit the framerate to 60 FPS
        # dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()