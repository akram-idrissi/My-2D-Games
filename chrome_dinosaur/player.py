import pygame


class Player:
    def __init__(self, screen, settings):
        self.up = False
        self.screen = screen
        self.settings = settings

        # animations
        self.START = [pygame.image.load("assets/Dino/DinoStart2.png")]
        self.END = [pygame.image.load("assets/Dino/DinoDead.png")]
        self.RUN = [pygame.image.load("assets/Dino/DinoRun1.png"), pygame.image.load("assets/Dino/DinoRun2.png")]
        self.DUCK = [pygame.image.load("assets/Dino/DinoDuck1.png"), pygame.image.load("assets/Dino/DinoDuck2.png")]
        self.animation = [self.START, self.END, self.RUN, self.DUCK]

        # variables for the jump method
        self.air_timer = 0
        self.player_y_momentum = 0

        # variables for the animate method
        self.timer = 100
        self.img_frame = 0
        self.list_frame = 2
        self.last_update = pygame.time.get_ticks()

        # setting the image size
        self.image = self.animation[self.list_frame][self.img_frame]

        # getting the rect and setting its x and y coordinates
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 252

    def jump(self):
        self.rect.y += self.player_y_momentum
        self.player_y_momentum += 0.5
        if self.player_y_momentum > self.settings.up:
            self.player_y_momentum = self.settings.up

        if self.rect.y >= 252:
            self.list_frame = 2
            self.player_y_momentum = 0
            self.air_timer = 0
        else:
            self.air_timer += 1

    def animate(self):
        a = self.animation[self.list_frame]
        if len(a) > 1:
            current_update = pygame.time.get_ticks()
            self.image = a[self.img_frame]
            if current_update - self.last_update >= self.timer:
                self.img_frame += 1
                self.last_update = current_update
            if self.img_frame > 1:
                self.img_frame = 0
        else:
            self.image = a[0]

        self.image = pygame.transform.scale(self.image, (60, 60))
        self.image.set_colorkey(self.settings.white)

    def draw(self):
        self.screen.blit(self.image, self.rect)
