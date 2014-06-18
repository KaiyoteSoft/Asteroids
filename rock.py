import pygame
import random

class Rock(pygame.sprite.Sprite):
    def __init__(self, safe_rect, size, screen_size, speed):
        pygame.sprite.Sprite.__init__(self)

        self.size = size
        self.speed = speed
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.center = [self.size / 2, self.size / 2]
        self.screen_size = screen_size
        self.buffer = 300
        self.safe_rect = safe_rect
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.set_position()

        self.draw()



        self.direction = random.choice(["right", "left", "up", "down",
                                        "up_right", "up_left",
                                        "down_right", "down_left"])

    def draw(self):
        pygame.draw.circle(self.image, (0, 255, 0), (self.center), self.size / 2, 1)
        pygame.draw.circle(self.image, (62, 199, 238), (self.center), int(.8 * self.size / 2), 1)
        pygame.draw.circle(self.image, (255, 40, 89), (self.center), int(.5 * self.size / 2), 1)

        # if (self.rect.centerx < 400 + self.buffer
        #     and self.rect.centerx > 400 - self.buffer
        #     and self.rect.centery < 300 + self.buffer
        #     and self.rect.centery > 300 - self.buffer):
        #     self.draw()

        # print (self.rect.center, self.safe_rect)
        #print(self.center)

    def set_position(self):
        self.rand_x = random.randint(0, 1280)
        self.rand_y = random.randint(0, 770)

        self.rect.center = (self.rand_x, self.rand_y)
        if self.safe_rect.collidepoint(self.rect.center):
            print ("BREACH at {} with ship at {}".format(self.rect.center, self.safe_rect))
            self.set_position()


    def update(self):
        if self.direction == "right":
            self.rect.centerx += self.speed
        if self.direction == "left":
            self.rect.centerx -= self.speed
        if self.direction == "up":
            self.rect.centery -= self.speed
        if self.direction == "down":
            self.rect.centery += self.speed
        if self.direction == "up_right":
            self.rect.centery -= self.speed
            self.rect.centerx += self.speed
        if self.direction == "up_left":
            self.rect.centery -= self.speed
            self.rect.centerx -= self.speed
        if self.direction == "down_right":
            self.rect.centery += self.speed
            self.rect.centerx += self.speed
        if self.direction == "down_left":
            self.rect.centery += self.speed
            self.rect.centerx -= self.speed

        if self.rect.centerx > self.screen_size[0]:
            self.rect.centerx = 0
        if self.rect.centerx < 0:
            self.rect.centerx = self.screen_size[0]
        if self.rect.centery > self.screen_size[1]:
            self.rect.centery = 0
        if self.rect.centery < 0:
            self.rect.centery = self.screen_size[1]