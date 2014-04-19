import pygame, sys
import math
from pygame.locals import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, radian_angle, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((4, 4))
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, (255, 255, 255), (2, 2), 2)
        self.radian_angle = radian_angle
        self.radius = 70
        self.center = center
        
    
    def update(self):
        length_x_fire = math.cos(self.radian_angle) * self.radius 
        length_y_fire = math.sin(self.radian_angle) * self.radius 
        x_fire = int(self.center[0] + length_x_fire)
        y_fire = int(self.center[1] - length_y_fire)
        self.rect.center = [x_fire, y_fire], 
        print (self.rect)
        
        self.radius = self.radius + 13
        
        #if self.rect.centerx > 800:
        #    self.rect.centerx = 0
        
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((150, 150))
        self.rect = pygame.draw.polygon(self.image, (0, 255, 0), [(100, 100),
            (150, 100), (30, 75), (80, 130)], 3)
    


pygame.init()


RED = ((255, 0, 0))
GREEN = ((0, 255, 0))
ORANGE = ((254, 158, 27))
center = [400, 300]
size = 10
angle = 0
WHITE = ((255, 255, 255))
radius = 50

screen_size = (800, 600)
windowSurface = pygame.display.set_mode(screen_size)


clock = pygame.time.Clock()
FPS = 30

forward = False
fume = False

direction = "stop"
fire = False
bullet_group = pygame.sprite.Group()

rock = Rock()
rock_group = pygame.sprite.Group()
rock_group.add(rock)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                direction = "right"
            if event.key == K_LEFT:
                direction = "left"
            if event.key == K_s:
                radius = radius - 10
            if event.key == K_l:
                radius = radius + 10
            if event.key == K_UP:
                forward = True
                fume = True
            if event.key == K_SPACE:
                fire = True
        if event.type == KEYUP:
            if event.key == K_UP:
                forward = False
                fume = False
            if event.key == K_RIGHT:
                direction = "stop"
            if event.key == K_LEFT:
                direction = "stop"
            
    
    radian_angle = math.radians(angle)
    length_x = math.cos(radian_angle) * radius
    length_y = math.sin(radian_angle) * radius
    
    x = int(center[0] + length_x)
    y = int(center[1] - length_y)
            
####
    angle_2 = math.radians(angle + 120)
    length_x_2 = math.cos(angle_2) * radius
    length_y_2 = math.sin(angle_2) * radius
    x_2 = int(center[0] + length_x_2)
    y_2 = int(center[1] - length_y_2)
    
####
    angle_3 = math.radians(angle + 240)
    length_x_3 = math.cos(angle_3) * radius
    length_y_3 = math.sin(angle_3) * radius
    x_3 = int(center[0] + length_x_3)
    y_3 = int(center[1] - length_y_3)
    
###
    length_x_motion = math.cos(radian_angle) * radius / 8
    length_y_motion = math.sin(radian_angle) * radius / 8
    x_motion = int(center[0] + length_x_motion)
    y_motion = int(center[1] - length_y_motion)
     
###
    angle_4 = math.radians(angle + 180)
    length_x_4 = math.cos(angle_4) * radius
    length_y_4 = math.sin(angle_4) * radius
    x_4 = int(center[0] + length_x_4)
    y_4 = int(center[1] - length_y_4)
    
    thrust_x = (x_2 + x_3) / 2
    thrust_y = (y_2 + y_3) / 2
    

    windowSurface.fill((0, 0, 0))
    
    #pygame.draw.circle(windowSurface, RED, center, size)
    #pygame.draw.circle(windowSurface, GREEN, (x, y), size)
    #pygame.draw.circle(windowSurface, GREEN, (x_2, y_2), size)
    #pygame.draw.circle(windowSurface, GREEN, (x_3, y_3), size)
    #
    rock_group.draw(windowSurface)
    
    pygame.draw.line(windowSurface, WHITE, (x,y), (x_2, y_2))
    pygame.draw.line(windowSurface, WHITE, (x_2, y_2), (center))
    pygame.draw.line(windowSurface, WHITE, (center), (x_3, y_3))
    pygame.draw.line(windowSurface, WHITE, (x_3, y_3), (x, y))
    
    pygame.draw.circle(windowSurface, RED, (x_motion, y_motion), size / 2)
    bullet_group.update()
    bullet_group.draw(windowSurface)
    
    
    
    
    if angle >= 360:
        angle = 0
    if direction == "left":
        angle = angle + 3
        print(angle)
    if direction == "right":
        angle = angle - 3
        
    if forward == True:
        center = [x_motion, y_motion]
        
    if fume == True:
        pygame.draw.circle(windowSurface, ORANGE, (thrust_x, thrust_y), size, 2)
        
    if center[0] > screen_size[0]:
        center[0] = 0
    if center[0] < 0:
        center[0] = screen_size[0]
    if center[1] > screen_size[1]:
        center[1] = 0
    if center[1] < 0:
        center[1] = screen_size[1]
        
    if fire == True:
        bullet = Bullet(radian_angle, center)
        bullet_group.add(bullet)
        fire = False
        
    for bullet in bullet_group:
        if bullet.rect.centerx > screen_size[0]:
            bullet_group.remove(bullet)
           # bullet.rect.centerx = 0
           #print("exceeded screen width") 
           
        if bullet.rect.centerx < 0:
            bullet_group.remove(bullet)
        if bullet.rect.centery > 600:
            bullet_group.remove(bullet)
        if bullet.rect.centery < 0:
            bullet_group.remove(bullet)
        
    pygame.sprite.groupcollide(bullet_group, rock_group, True, True)
    
    clock.tick(FPS)
    pygame.display.update()
    