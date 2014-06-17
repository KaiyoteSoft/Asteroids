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

if android:
    android.init()
    android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

try:
    import pygame.mixer as mixer
except ImportError:
    import android.mixer as mixer


RED = ((255, 0, 0))
GREEN = ((0, 255, 0))
ORANGE = ((254, 158, 27))
BLACK = (0, 0, 0)
PINK = (254, 15, 234)
LIGHTBLUE = (0, 255, 252)
DARKRED = (198, 46, 46)


center = [400, 300]
size = 7
angle = 0
WHITE = ((255, 255, 255))
radius = 20

thruster_radius = 50

screen_size = (1280, 770)
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

speed = 1
rock = Rock(80, screen_size, speed = 1)
rock_group = pygame.sprite.Group()
rock_group.add(rock)

initial_rock_time = pygame.time.get_ticks()

# score = 0
score = Score()

left_circle = pygame.draw.circle(windowSurface, (255, 255, 255), (100, 600), 30, 2)
right_circle = pygame.draw.circle(windowSurface, (255, 255, 255), (200, 600), 30, 2)
forward_circle = pygame.draw.circle(windowSurface, (255, 255, 255), (150, 520), 30, 2)

shoot_circle = pygame.draw.circle(windowSurface, (255, 0, 0), (1100, 580), 40, 2)

pressed = False

#### sound
fire_snd = mixer.Sound("snd/fire.wav")
big_rock_snd = mixer.Sound("snd/banglarge.wav")
medium_rock_snd = mixer.Sound("snd/bangmedium.wav")

gameOn = True

### Create a rectangle for Play Again = Yes
yes_font = pygame.font.Font("fonts/ASTONISH.TTF", 80)
yes_text = yes_font.render("YES!!!", True, GREEN)
yes_rect = pygame.Rect(150, 300, 150, 60)

## Create a rectangle for the "Player DEAD :)
endFont = pygame.font.Font("fonts/BLOODY.ttf", 130)
endText = endFont.render("DEAD", True , RED)
endText_rect = pygame.Rect(600, 10, 200, 200)

### Create a rectangle for Play Again
playAgain_font = pygame.font.Font("fonts/ASTONISH.TTF", 80)
playAgain_text = playAgain_font.render("Play Again? ", True, LIGHTBLUE)
playAgain_rect = pygame.Rect(500, 150, 480, 180)

### Create a rectangle for Play Again = No
no_font = pygame.font.Font("fonts/BLOODY.ttf", 85)
no_text = no_font.render("No...", True, DARKRED)
no_rect = pygame.Rect(800, 300, 150, 60)




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
            if shoot_circle.collidepoint(mouse_pos) and gameOn == True:
                fire = True

            if no_rect.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()
            if yes_rect.collidepoint(mouse_pos):
                gameOn = True
                score.points = 0
                score = Score()

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

    left_circle = pygame.draw.circle(windowSurface, (255, 255, 255), (100, 620), 60, 2)
    right_circle = pygame.draw.circle(windowSurface, (255, 255, 255), (300, 620), 60, 2)
    forward_circle = pygame.draw.circle(windowSurface, (255, 255, 255), (200, 480), 60, 2)

    shoot_circle = pygame.draw.circle(windowSurface, (255, 0, 0), (1100, 580), 70, 2)

    rock_group.update()
    rock_group.draw(windowSurface)
    
    pygame.draw.line(windowSurface, WHITE, (x,y), (x_2, y_2))
    pygame.draw.line(windowSurface, WHITE, (x_2, y_2), (center))
    pygame.draw.line(windowSurface, WHITE, (center), (x_3, y_3))
    pygame.draw.line(windowSurface, WHITE, (x_3, y_3), (x, y))

    ship_rect = pygame.Rect(0, 0, radius * 1.5, radius * 1.5)
    ship_rect.center = center

    #pygame.draw.circle(windowSurface, RED, (x_motion, y_motion), size / 2)
    bullet_group.update()
    bullet_group.draw(windowSurface)


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
        fire_snd.play()



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
                big_rock_snd.play()
                print (score.points)

                if rock.size > 20:
                    new_rock = Rock(rock.size / 2, screen_size, speed + 1)
                    new_rock.rect.center = rock.rect.center
                    rock_group.add(new_rock)
                    new_rock = Rock(rock.size / 2, screen_size, speed + 1)
                    new_rock.rect.center = rock.rect.center
                    rock_group.add(new_rock)
                
                rock_group.remove(rock)
                medium_rock_snd.play()

        if ship_rect.colliderect(rock.rect):

            print ("ship hit rock")
            forward = False
            bullet_group.empty()
            rock_group.empty()
            center = (400, 300)
            gameOn = False

    
    
    #for rock in rock_group:
        
    
    
    if elapsed_rock_time > 2:
        rock = Rock(80, screen_size, 1)
        rock_group.add(rock)
        initial_rock_time = pygame.time.get_ticks()


    if gameOn == False:
        windowSurface.fill((0, 0, 0))
        windowSurface.blit(endText, endText_rect)
        windowSurface.blit(playAgain_text, playAgain_rect)
        windowSurface.blit(no_text, no_rect)
        windowSurface.blit(yes_text, yes_rect)
        fire = False
###### score
        file_score = open("high_score.txt", "r+")
        file_points = file_score.read()

        try:
            file_points = int(file_points)
        except:
            file_points = 0

        if score.points > file_points:
            print("High Score")
            file_score.seek(0)
            print(score.points)
            file_score.write(str(score.points))
        else:
            print("Lower Score")
            print(score.points)
            file_score.close()

        ### Scores
        score_font = pygame.font.Font("fonts/animeace2_reg.ttf", 80)
        high_score_text = score_font.render("High Score is : " + str(file_points), True, GREEN)
        high_score_rect = pygame.Rect(10, 600, 200, 200)

        score_text = score_font.render("Your Score is : " + str(score.points), True, RED)
        score_rect = pygame.Rect(50, 450, 200, 200)

        windowSurface.blit(high_score_text, high_score_rect)
        windowSurface.blit(score_text, score_rect)
### comment

    clock.tick(FPS)
    pygame.display.update()
    