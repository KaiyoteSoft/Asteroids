import pygame, sys
import math
import random
from pygame.locals import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, radian_angle, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((4, 4))
        self.rect = self.image.get_rect()
        self.rect.center = center
        pygame.draw.circle(self.image, (255, 255, 255), (2, 2), 2)
        self.radian_angle = radian_angle
        self.radius = 70
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
            
        
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        rand_x = random.randint(0, 800)
        rand_y = random.randint(0, 600)
        self.image = pygame.Surface((40, 40))
        self.rect = pygame.draw.circle(self.image, (0, 255, 0), (20, 20), 20, 2)
        self.rect.center = (rand_x, rand_y)
        
        self.direction = random.choice(["right", "left", "up", "down"])
    def update(self):
        if self.direction == "right":
            self.rect.centerx += 1
        if self.direction == "left":
            self.rect.centerx -= 1
        if self.direction == "up":
            self.rect.centery -= 1
        if self.direction == "down":
            self.rect.centery += 1
        
        if self.rect.centerx > 800:
            self.rect.centerx = 0
        if self.rect.centerx < 0:
            self.rect.centerx = 800
        if self.rect.centery > 600:
            self.rect.centery = 0
        if self.rect.centery < 0:
            self.rect.centery = 600
    


pygame.init()


RED = ((255, 0, 0))
GREEN = ((0, 255, 0))
ORANGE = ((254, 158, 27))
center = [400, 300]
size = 7
angle = 0
WHITE = ((255, 255, 255))
radius = 20

thruster_radius = 50

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

initial_rock_time = pygame.time.get_ticks()

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
    length_x_motion = math.cos(radian_angle) * radius / 5
    length_y_motion = math.sin(radian_angle) * radius / 5
    x_motion = int(center[0] + length_x_motion)
    y_motion = int(center[1] - length_y_motion)
     
###
    angle_4 = math.radians(angle + 180)
    length_x_4 = math.cos(angle_4) * radius
    length_y_4 = math.sin(angle_4) * radius
    x_4 = int(center[0] + length_x_4)
    y_4 = int(center[1] - length_y_4)
    
#### calculation for thruster
    angle_2 = math.radians(angle + 120)
    length_x_2 = math.cos(angle_2) * thruster_radius
    length_y_2 = math.sin(angle_2) * thruster_radius
    thrust_x_2 = int(center[0] + length_x_2)
    thrust_y_2 = int(center[1] - length_y_2)
    
#### calculation for thruster
    angle_3 = math.radians(angle + 240)
    length_x_3 = math.cos(angle_3) * thruster_radius
    length_y_3 = math.sin(angle_3) * thruster_radius
    thrust_x_3 = int(center[0] + length_x_3)
    thrust_y_3 = int(center[1] - length_y_3)
    
    thrust_x = (thrust_x_2 + thrust_x_3) / 2
    thrust_y = (thrust_y_2 + thrust_y_3) / 2
    

    windowSurface.fill((0, 0, 0))
    
    
### timer for rock
    elapsed_rock_time = (pygame.time.get_ticks() - initial_rock_time) / 1000
    print(elapsed_rock_time)
    
    rock_group.update()
    rock_group.draw(windowSurface)
    
    pygame.draw.line(windowSurface, WHITE, (x,y), (x_2, y_2))
    pygame.draw.line(windowSurface, WHITE, (x_2, y_2), (center))
    pygame.draw.line(windowSurface, WHITE, (center), (x_3, y_3))
    pygame.draw.line(windowSurface, WHITE, (x_3, y_3), (x, y))
    
    #pygame.draw.circle(windowSurface, RED, (x_motion, y_motion), size / 2)
    bullet_group.update()
    bullet_group.draw(windowSurface)
    
    
    
    
    if angle >= 360:
        angle = 0
    if direction == "left":
        angle = angle + 4
        #print(angle)
    if direction == "right":
        angle = angle - 4
        
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
    ####### checking boundaries
        if bullet.pass_boundary == True:
            if bullet.rect.centerx > bullet.original_center[0] - 400:
                bullet_group.remove(bullet)
                #bullet.pass_boundary = False
        
        if bullet.pass_boundary_neg_x == True:
            if bullet.rect.centerx < bullet.original_center[0] + 400:
                bullet_group.remove(bullet)
                
        
        if bullet.pass_boundary_pos_y == True:
            if bullet.rect.centery > bullet.original_center[1] - 300:
                bullet_group.remove(bullet)
                
        if bullet.pass_boundary_neg_y == True:
            if bullet.rect.centery < bullet.original_center[1] + 300:
                bullet_group.remove(bullet)
        
    pygame.sprite.groupcollide(bullet_group, rock_group, True, True)
    
    
    #for rock in rock_group:
        
    
    
    if elapsed_rock_time > 2:
        rock = Rock()
        rock_group.add(rock)
        initial_rock_time = pygame.time.get_ticks()
    
    clock.tick(FPS)
    pygame.display.update()
    