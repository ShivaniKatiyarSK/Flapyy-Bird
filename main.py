import pygame
from config import *
from sprites import load_sprites, load_sounds
from game_screens import welcomeScreen, gameoverScreen
from game_logic import mainGame

if __name__ == "__main__":
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird')

    # Load sprites and sounds
    load_sprites()
    load_sounds()

    while True:
        welcomeScreen()
        mainGame()
