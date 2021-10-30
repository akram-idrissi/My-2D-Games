import pygame


class Box:

    def __init__(self, screen, x, y, w, h, color=None):
        self.screen = screen

        self.x = x
        self.y = y

        self.w = w
        self.h = h

        self.text = ""
        self.color = color

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        self.font = pygame.font.SysFont("", 38)

    @staticmethod
    def is_none(element):
        return True if element is None and type(str) else False

    def draw_box(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def draw_text(self, pos, color):
        text = self.font.render(self.text, True, color)
        self.screen.blit(text, pos)
        return text

    def draw_input(self, color):
        pos = (self.rect.x + 5, self.rect.y + 5)
        text = self.font.render(self.text, True, color)
        self.screen.blit(text, pos)
        self.w = max(200, text.get_width() + 10)
        self.rect.w = self.w
