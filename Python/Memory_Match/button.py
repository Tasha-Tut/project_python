from print_text import *


class Button:
    """Button"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (240, 179, 175)
        self.active_color = (212, 55, 44)

    def draw(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(screen, self.active_color, (x, y, self.width, self.height))
            if click[0] == 1 and action is not None:
                if action == quit:
                    pygame.quit()
                    quit()
                else:
                    action()
        else:
            pygame.draw.rect(screen, self.inactive_color, (x, y, self.width, self.height))

        print_text(message=message, x=x + 7, y=y + 7)