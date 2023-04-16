import pygame

"""materials"""
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matching Game")
icon = pygame.image.load('images/icon.png').convert_alpha()
pygame.display.set_icon(icon)
font = pygame.font.Font('fonts/RobotoMono-Medium.ttf', 25)
title_font = pygame.font.Font('fonts/RobotoMono-Medium.ttf', 40)
bg_sound = pygame.mixer.Sound('music/lo-fi.mp3')

"""game variables and constance"""
fps = 60
timer = pygame.time.Clock()
rows = 6
cols = 8
yellow = (245, 239, 56)
correct = []
new_board = True
options_list = []
spaces = []
used = []
correct = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]
first_guess = False
second_guess = False
game_over = False
first_guess_num = 0
second_guess_num = 0
score = 0
best_score = 0
matches = 0
theme_now = 'black'
running = True
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


