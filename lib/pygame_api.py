import pygame
from lib.numpy_api import getRandomChoice


class Game:
    def __init__(self, width: int, height: int, columns: int, rows: int) -> None:
        self.width = width
        self.height = height
        self.state = getRandomChoice(columns, rows)
        self.isPaused = False

    def start(self):
        pygame.init()
        self.surface = pygame.display.set_mode((self.width, self.height))

    def getFont(self):
        return pygame.font.Font(None, 36)

    def quit(self):
        pygame.quit()
