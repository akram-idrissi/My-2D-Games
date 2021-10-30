import pygame
import random
import sys


class General:

    def __init__(self, screen, settings, text_box, help_box, score_box):
        self.sc = screen
        self.st = settings

        self.text_b = text_box
        self.help_b = help_box
        self.score_b = score_box

        self.text = ""

        self.price = random.randint(80, 150)

        self.messages = {
            '-1': ' ',
            '0': f'The price is between {self.price - 10} and {self.price + 10}',
            '1': 'Congrats!!, You\'ve guessed my price',
            '2': 'It\'s to high, Try again',
            '3': 'It\'s to low, Try again'
        }

    def mouse_text_collision(self):
        if self.text_b.rect.collidepoint(pygame.mouse.get_pos()):
            self.st.write = True
            self.text_b.color = self.st.color_active
        else:
            self.st.write = False
            self.text_b.color = self.st.color_passive

    def help_text_collision(self):
        if self.help_b.rect.collidepoint(pygame.mouse.get_pos()):
            self.st.help_user = True
            self.st.score -= 1
        else:
            self.st.help_user = False

    @staticmethod
    def close_window():
        pygame.quit()
        sys.exit()

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_window()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_text_collision()
                self.help_text_collision()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.close_window()
                if self.st.write:
                    if event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]

                    else:
                        self.text += str(event.unicode)

        return self.text

    def check_input(self):
        if self.st.help_user:
            return self.messages['0']

        try:
            text_copy = int(self.text)
            if text_copy == self.price:
                return self.messages['1']
            elif text_copy > self.price:
                return self.messages['2']
            else:
                return self.messages['3']
        except Exception:
            return " "
