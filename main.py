# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    FPS = 60

    # Initialize the pygame library
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # end of initialization

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        dt = clock.tick(FPS)
        pygame.display.flip()

if __name__ == "__main__":
    main()