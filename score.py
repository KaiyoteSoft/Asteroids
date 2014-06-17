import pygame

class Score():
    def __init__(self):
        self.WHITE = ((255, 255, 255))
        self.font = pygame.font.Font("fonts/animeace2_reg.ttf", 20)
        self.points = 0
        self.update()

    def update(self):
        self.score_surface = self.font.render("SCORE: " + str(self.points), True, self.WHITE)


