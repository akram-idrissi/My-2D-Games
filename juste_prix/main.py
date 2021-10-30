"""
Made By A.M.I
"""

import pygame

from box import Box
from general import General
from settings import Settings


class App:
    def __init__(self):
        pygame.init()

        self.st = Settings()
        self.sc = pygame.display.set_mode((self.st.width, self.st.height))

        self.text_box = Box(self.sc, 300, 275, 200, 50, color=self.st.color_passive)
        self.help_box = Box(self.sc, 480, 20, 310, 30, color=self.st.color_passive)
        self.score_box = Box(self.sc, 10, 20, 110, 30, color=self.st.color_passive)
        self.response_box = Box(self.sc, 0, 0, 0, 0)

        self.gn = General(self.sc, self.st, self.text_box, self.help_box, self.score_box)

        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self.sc.fill(self.st.background)

            # drawing the help_box and rendering it text
            self.help_box.text = "Stuck ?! Get some help!"
            self.help_box.draw_box()
            self.help_box.draw_text((480, 20), self.st.white)

            # drawing the score_box and rendering it text
            self.score_box.text = "Score: " + str(self.st.score)
            self.score_box.draw_box()
            self.score_box.draw_text((10, 20), self.st.white)

            # drawing the text_box and rendering the user input
            self.text_box.text = self.gn.get_input()
            self.text_box.draw_box()
            self.text_box.draw_input(self.st.white)

            # rendering the response to the user
            self.response_box.text = self.gn.check_input()
            self.response_box.draw_text((280, 350), self.st.color_passive)

            pygame.display.update()
            self.clock.tick(self.st.fps)


if __name__ == "__main__":
    app = App()
    app.run()
