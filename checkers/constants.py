import pygame

#Stałe kolory - RGB
RED = (255, 0, 0)
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
GREEN = (0, 252, 0)
GRAY = (125, 125, 125)
YELLOW = (255, 255, 0)
ORANGE=(219, 150, 11)

#Stałe wielkości używane w programie
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS


#Czcionki
pygame.init()
SMALL_FONT = pygame.font.SysFont("Arial", 20)
MEDIUM_FONT = pygame.font.SysFont("Arial", 30)
HUGE_FONT = pygame.font.SysFont("Arial", 60)
D_FONT = pygame.font.Font('assets/SyneMono-Regular.ttf', 60)


#Obrazy importowane z zewnątrz
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))