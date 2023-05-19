import random
import pygame


from .button import Button
from global_varies import *

score = 0
best_score = 0
matches = 0

def run():
    global matches
    global spaces
    global options_list
    global used
    global correct
    
    running = True
    new_board = True
    first_guess = False
    second_guess = False
    game_over = False
    first_guess_num = 0
    second_guess_num = 0


    while running:
        timer.tick(fps)
        screen.fill('White')

        if new_board:
            generate_board()
            new_board = False

        menu_background = pygame.image.load('images/menu_background.jpg')
        start_button = Button(300, 70)
        theme_button = Button(300, 70)
        exit_button = Button(300, 70)
        menu_button = Button(80, 50)

        while show_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            screen.blit(menu_background, (0, 0))
            start_button.draw(160, 130, 'start game', quit_menu())
            theme_button.draw(160, 210, f'theme: {theme_now}', theme())
            exit_button.draw(160, 290, 'exit', quit)
            pygame.display.update()

        """create background"""
        if red_theme:
            restart = draw_backgrounds(red_back, red)
        elif blue_theme:
            restart = draw_backgrounds(blue_back, blue)
        else:
            restart = draw_backgrounds(black_back, black)

        """create board"""
        board = draw_board()

        if first_guess and second_guess:
            check_guesses(first_guess_num, second_guess_num)
            pygame.time.delay(500)
            first_guess = False
            second_guess = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(board)):
                    button = board[i]
                    if not game_over:
                        if button.collidepoint(event.pos) and not first_guess:
                            first_guess = True
                            first_guess_num = i
                        if button.collidepoint(event.pos) and not second_guess and first_guess and i != first_guess_num:
                            second_guess = True
                            second_guess_num = i
                if restart.collidepoint(event.pos):
                    options_list = []
                    used = []
                    spaces = []
                    new_board = True
                    score = 0
                    matches = 0
                    first_guess = False
                    second_guess = False
                    correct = [[0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0]]
                    game_over = False

        if not show_menu:
            menu_button.draw(50, 530, 'menu', get_menu())

        if matches == rows * cols // 2:
            game_over = True
            winner = pygame.draw.rect(screen, yellow, [10, HEIGHT - 300, WIDTH - 20, 80])
            winner_text = title_font.render(f'You won in {score} moves!', True, black)
            screen.blit(winner_text, (10, HEIGHT - 290))
            if best_score > score or best_score == 0:
                best_score = score

        if first_guess:
            piece_text = font.render(f'{spaces[first_guess_num]}', True, red)
            location = (first_guess_num // rows * 75 + 18, (first_guess_num - (first_guess_num // rows * rows)) * 65 + 120)
            screen.blit(piece_text, location)

        if second_guess:
            piece_text = font.render(f'{spaces[second_guess_num]}', True, red)
            location = (second_guess_num // rows * 75 + 18, (second_guess_num - (second_guess_num // rows * rows)) * 65 + 120)
            screen.blit(piece_text, location)

        pygame.display.flip()


def generate_board():
    """Generate board for game"""
    global options_list
    global spaces
    global used
    for item in range(rows * cols // 2):
        options_list.append(item)
    for item in range(rows * cols):
        piece = options_list[random.randint(0, len(options_list) - 1)]
        spaces.append(piece)
        if piece in used:
            used.remove(piece)
            options_list.remove(piece)
        else:
            used.append(piece)


def draw_backgrounds(color_back, color):
    """background and formalization"""
    top_menu = pygame.draw.rect(screen, color_back, [0, 0, WIDTH, 100])
    title_text = title_font.render('memory match', False, black)
    screen.blit(title_text, (150, 20))
    board_space = pygame.draw.rect(screen, color, [0, 100, WIDTH, HEIGHT - 200])
    bottom_menu = pygame.draw.rect(screen, color_back, [0, HEIGHT - 100, WIDTH, 100])
    restart_button = pygame.draw.rect(screen, color_back, [210, 520, 180, 100])
    restart_text = title_font.render('restart', False, black)
    screen.blit(restart_text, (210, 520))
    score_text = font.render(f'score: {score}', False, black)
    screen.blit(score_text, (430, 510))
    best_score_text = font.render(f'best: {best_score}', False, black)
    screen.blit(best_score_text, (430, 550))
    return restart_button


def draw_board():
    """draw board"""
    global rows
    global cols
    global correct
    # global spaces
    board_list = []
    for i in range(cols):
        for j in range(rows):
            piece = pygame.draw.rect(screen, black_back, [i * 75 + 12, j * 65 + 112, 50, 50])
            board_list.append(piece)
    for r in range(rows):
        for c in range(cols):
            if correct[r][c] == 1:
                piece = pygame.draw.rect(screen, (0, 255, 0), [c * 75 + 10, r * 65 + 110, 54, 54])
                piece_text = font.render(f'{spaces[c * rows + r]}', False, black)
                screen.blit(piece_text, (c * 75 + 18, r * 65 + 120))
    return board_list


def check_guesses(first, second):
    '''checking correct tap'''
    global spaces
    global correct
    global score
    global matches
    if spaces[first] == spaces[second]:
        col1 = first // rows
        col2 = second // rows
        row1 = first - (first // rows * rows)
        row2 = second - (second // rows * rows)
        if correct[row1][col1] == 0 and correct[row2][col2] == 0:
            correct[row1][col1] = 1
            correct[row2][col2] = 1
            score += 1
            matches += 1
    else:
        score += 1


def quit_menu():
    '''function to quit from menu'''
    global show_menu
    mouse_menu = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if mouse_click[0] == 1:
        if 160 < mouse_menu[0] < 460 and 130 < mouse_menu[1] < 200:
            show_menu = False


def get_menu():
    '''go to the menu'''
    global show_menu
    mouse_menu = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if mouse_click[0] == 1:
        if 50 < mouse_menu[0] < 130 and 530 < mouse_menu[1] < 580:
            show_menu = True


def theme():
    '''change theme'''
    global theme_now
    global red_theme
    global blue_theme
    global black_theme
    mouse_menu = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if mouse_click[0] == 1:
        if 160 < mouse_menu[0] < 460 and 210 < mouse_menu[1] < 280:
            if red_theme:
                red_theme = False
                blue_theme = True
                black_theme = False
                theme_now = 'blue'
                pygame.time.delay(100)
            elif blue_theme:
                red_theme = False
                blue_theme = False
                black_theme = True
                theme_now = 'black'
                pygame.time.delay(100)
            else:
                red_theme = True
                blue_theme = False
                black_theme = False
                theme_now = 'red'
                pygame.time.delay(100)

