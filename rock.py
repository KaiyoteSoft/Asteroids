import pygame
import random

class Rock(pygame.sprite.Sprite):
    def __init__(self, size = 80):
        pygame.sprite.Sprite.__init__(self)
        rand_x = random.randint(0, 800)
        rand_y = random.randint(0, 600)
        self.size = size
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.center = [self.size / 2, self.size / 2]

        self.draw()
        self.rect.center = (rand_x, rand_y)


        self.direction = random.choice(["right", "left", "up", "down",
                                        "up_right", "up_left",
                                        "down_right", "down_left"])

    def draw(self):
        self.rect = pygame.draw.circle(self.image, (0, 255, 0), (self.center), self.size / 2, 1)
        pygame.draw.circle(self.image, (62, 199, 238), (self.center), int(.8 * self.size / 2), 1)
        pygame.draw.circle(self.image, (255, 40, 89), (self.center), int(.5 * self.size / 2), 1)


    def update(self):
        if self.direction == "right":
            self.rect.centerx += 1
        if self.direction == "left":
            self.rect.centerx -= 1
        if self.direction == "up":
            self.rect.centery -= 1
        if self.direction == "down":
            self.rect.centery += 1
        if self.direction == "up_right":
            self.rect.centery -= 1
            self.rect.centerx += 1
        if self.direction == "up_left":
            self.rect.centery -= 1
            self.rect.centerx -= 1
        if self.direction == "down_right":
            self.rect.centery += 1
            self.rect.centerx += 1
        if self.direction == "down_left":
            self.rect.centery += 1
            self.rect.centerx -= 1

        if self.rect.centerx > 800:
            self.rect.centerx = 0
        if self.rect.centerx < 0:
            self.rect.centerx = 800
        if self.rect.centery > 600:
            self.rect.centery = 0
        if self.rect.centery < 0:
            self.rect.centery = 600