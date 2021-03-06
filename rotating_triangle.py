import pygame, sys
import math
import random
from pygame.locals import *
from bullet import *
from rock import *
from score import *

try:
    import android
except ImportError:
    android = None

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

screen_size = (1280, 720)
windowSurface = pygame.display.set_mode(screen_size)


clock = pygame.time.Clock()
FPS = 30

forward = False
ship_min_brake = 4
ship_speed_brake = ship_min_brake

fume = False

direction = "stop"
fire = False
bullet_group = pygame.sprite.Group()

rock = Rock()
rock_group = pygame.sprite.Group()
rock_group.add(rock)

initial_rock_time = pygame.time.get_ticks()

# score = 0
score = Score()

left_circle = pygame.draw.circle(windowSurface, (255, 255, 255), (100, 520), 30, 2)
right_circle = pygame.draw.circle(windowSurface, (255, 255, 255), (200, 520), 30, 2)
forward_circle = pygame.draw.circle(windowSurface, (255, 255, 255), (150, 450), 30, 2)

shoot_circle = pygame.draw.circle(windowSurface, (255, 0, 0), (650, 520), 40, 2)

pressed = False

if android:
    android.init()
    android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        mouse_pos = pygame.mouse.get_pos()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
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
                thruster_start_time = pygame.time.get_ticks()
                ship_speed_brake = ship_min_brake
                fume = True
            if event.key == K_SPACE:
                fire = True
        if event.type == KEYUP:
            if event.key == K_UP:
                #forward = False
                fume = False
            if event.key == K_RIGHT:
                direction = "stop"
            if event.key == K_LEFT:
                direction = "stop"

        if event.type == MOUSEBUTTONDOWN:
            if left_circle.collidepoint(mouse_pos):
                direction = "left"
                pressed = True
            if right_circle.collidepoint(mouse_pos):
                direction = "right"
                pressed = True
            if forward_circle.collidepoint(mouse_pos):
                forward = True
                thruster_start_time = pygame.time.get_ticks()
                ship_speed_brake = ship_min_brake
                fume = True
            if shoot_circle.collidepoint(mouse_pos):
                fire = True
        if event.type == MOUSEBUTTONUP:
             pressed = False
             fume = False

    
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
    length_x_motion = math.cos(radian_angle) * radius / ship_speed_brake
    length_y_motion = math.sin(radian_angle) * radius / ship_speed_brake
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
    # print(elapsed_rock_time)

    score.update()
    windowSurface.blit(score.score_surface, (10, 10))

    rock_group.update()
    rock_group.draw(windowSurface)
    
    pygame.draw.line(windowSurface, WHITE, (x,y), (x_2, y_2))
    pygame.draw.line(windowSurface, WHITE, (x_2, y_2), (center))
    pygame.draw.line(windowSurface, WHITE, (center), (x_3, y_3))
    pygame.draw.line(windowSurface, WHITE, (x_3, y_3), (x, y))

    left_circle = pygame.draw.circle(windowSurface, (255, 255, 255), (100, 600), 30, 2)
    right_circle = pygame.draw.circle(windowSurface, (255, 255, 255), (200, 600), 30, 2)
    forward_circle = pygame.draw.circle(windowSurface, (255, 255, 255), (150, 520), 30, 2)

    shoot_circle = pygame.draw.circle(windowSurface, (255, 0, 0), (1100, 580), 40, 2)

    ship_rect = pygame.Rect(0, 0, radius * 1.5, radius * 1.5)
    ship_rect.center = center

    #pygame.draw.circle(windowSurface, RED, (x_motion, y_motion), size / 2)
    bullet_group.update()
    bullet_group.draw(windowSurface)


    # if left_circle.collidepoint(mouse_pos):
    #     direction = "left"
    # if right_circle.collidepoint(mouse_pos):
    #     direction = "right"


    if angle >= 360:
        angle = 0
    if direction == "left" and pressed == True:
        angle = angle + 5
        #print(angle)
    if direction == "right" and pressed == True:
        angle = angle - 5



    if forward == True:
        center = [x_motion, y_motion]
        thruster_elapsed_time = pygame.time.get_ticks() - thruster_start_time
        if thruster_elapsed_time > 3000:
            forward = False
        if thruster_elapsed_time > 1000:
            ship_speed_brake = 8
        if thruster_elapsed_time > 2000:
            ship_speed_brake = 12
        
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
        bullet = Bullet(radian_angle, center, screen_size)
        bullet_group.add(bullet)
        fire = False



    for bullet in bullet_group:
    ####### checking boundaries
        if bullet.pass_boundary == True:
            if bullet.rect.centerx > bullet.original_center[0] - 800:
                bullet_group.remove(bullet)
                #bullet.pass_boundary = False
        
        if bullet.pass_boundary_neg_x == True:
            if bullet.rect.centerx < bullet.original_center[0] + 800:
                bullet_group.remove(bullet)
                
        
        if bullet.pass_boundary_pos_y == True:
            if bullet.rect.centery > bullet.original_center[1] - 400:
                bullet_group.remove(bullet)
                
        if bullet.pass_boundary_neg_y == True:
            if bullet.rect.centery < bullet.original_center[1] + 400:
                bullet_group.remove(bullet)
        
## collision with rock & bullet     
    #pygame.sprite.groupcollide(bullet_group, rock_group, True, True)
    for rock in rock_group:
        for bullet in bullet_group:
            if bullet.rect.colliderect(rock.rect):
                bullet_group.remove(bullet)
                score.points = score.points + 1
                print (score.points)

                if rock.size > 20:
                    new_rock = Rock(rock.size / 2)
                    new_rock.rect.center = rock.rect.center
                    rock_group.add(new_rock)
                    new_rock = Rock(rock.size / 2)
                    new_rock.rect.center = rock.rect.center
                    rock_group.add(new_rock)
                
                rock_group.remove(rock)


        if ship_rect.colliderect(rock.rect):
            score.points = 0
            print ("ship hit rock")
            forward = False
            bullet_group.empty()
            rock_group.empty()
            center = (400, 300)
                
    
    
    
    #for rock in rock_group:
        
    
    
    if elapsed_rock_time > 2:
        rock = Rock()
        rock_group.add(rock)
        initial_rock_time = pygame.time.get_ticks()
    
    clock.tick(FPS)
    pygame.display.update()
    