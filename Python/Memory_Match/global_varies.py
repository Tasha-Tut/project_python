import pygame

pygame.init()

"""materials"""
WIDTH = 600
HEIGHT = 600
pygame.display.set_caption("Matching Game")
font = pygame.font.Font('fonts/RobotoMono-Medium.ttf', 25)
title_font = pygame.font.Font('fonts/RobotoMono-Medium.ttf', 40)
bg_sound = pygame.mixer.Sound('music/lo-fi.mp3')


timer = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

"""game variables and constance"""
fps = 60
rows = 6
cols = 8
yellow = (245, 239, 56)
correct = []


options_list = []
spaces = []
used = []
correct = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]


theme_now = 'black'

show_menu = True
play_sound = True

"""theme red"""
red_theme = False
red_back = (212, 133, 133)
red = (217, 24, 24)

"""theme blue"""
blue_theme = False
blue_back = (86, 184, 214)
blue = (6, 83, 184)

"""theme black"""
black_theme = True
black_back = (230, 231, 232)
black = (0, 0, 0)

