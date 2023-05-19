import pygame
from global_varies import *
from src import scene


def main():
    # pygame.init()
    bg_sound.play()
    scene.run()
    pygame.quit()


if __name__ == "__main__":
    main()
