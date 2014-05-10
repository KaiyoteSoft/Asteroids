import pygame
import math
import random

class Bullet(pygame.sprite.Sprite):
    def __init__(self, radian_angle, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((4, 4))
        self.rect = self.image.get_rect()
        self.rect.center = center
        pygame.draw.circle(self.image, (255, 255, 255), (2, 2), 2)
        self.radian_angle = radian_angle
        self.radius = 30
        self.bullet_center = [center[0], center[1]]
        self.original_center = center

        ### flags
        self.pass_boundary = False
        self.pass_boundary_neg_x = False


        self.pass_boundary_pos_y = False
        self.pass_boundary_neg_y = False

    def update(self):
        length_x_fire = math.cos(self.radian_angle) * self.radius
        length_y_fire = math.sin(self.radian_angle) * self.radius
        x_fire = int(self.bullet_center[0] + length_x_fire)
        y_fire = int(self.bullet_center[1] - length_y_fire)
        self.rect.center = [x_fire, y_fire]
        #print (self.rect)

        self.radius = self.radius + 13

        if self.rect.centerx > 800:
            #self.new_x_pos = self.bullet_center
            self.bullet_center[0] = 0
            self.rect.centerx = self.bullet_center[0]
            self.radius = 0
            self.pass_boundary = True
            #self.exceed_pos_x = False

        if self.rect.centerx < 0:
            self.bullet_center[0] = 790
            self.rect.centerx = self.bullet_center[0]
            self.radius = 0
            self.pass_boundary_neg_x = True
            #self.exceed_neg_x = False

        if self.rect.centery > 600:
            self.bullet_center[1] = 0
            self.rect.centery = self.bullet_center[1]
            self.radius = 0
            self.pass_boundary_pos_y = True
            #self.exceed_pos_y = False

        if self.rect.centery < 0:
            self.bullet_center[1] = 600
            self.rect.centery = self.bullet_center[1]
            self.radius = 0
            self.pass_boundary_neg_y = True