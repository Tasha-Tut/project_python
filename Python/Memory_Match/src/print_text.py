from global_varies import *

def print_text(message, x, y, font_color = (0, 0, 0), font_type=font):
    '''funtiont to print text'''
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))
