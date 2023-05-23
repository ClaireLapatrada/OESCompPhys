import random
from re import X
import pygame
import time
import math

clock = pygame.time.Clock()
pygame.init()
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
yellow = (233,196,106)
orange = (244,162,97)
green = (0,200,0)
blue = [0,0,255]
turq = (175,238,238)
navy = (38,70,83)
sky = (135,206,250)
fc = (42,157,143)
# Storing display width and height in variables to use later
display_width = 800
display_height = 600
# Set up and initialize display width and height
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
VELOCITY         = 1
LERP_FACTOR      = 0.05
minimum_distance = 0
maximum_distance = 1000

class Player(pygame.sprite.Sprite):
    def __init__(self, character, teachers, x, y, pos=(display_width,display_height)):
        self.x = x
        self.y = y
        self.image = pygame.image.load(teachers[character]['img']).convert_alpha()
        self.bimage = pygame.image.load(teachers[character]['bimg']).convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.direction = pygame.math.Vector2()
        self.name = character
        self.HP = teachers[character]['HP']
        self.Attack = teachers[character]['Attack']
        self.speed = teachers[character]['Speed']
        self.Experience = teachers[character]['Exp']
        self.crit_chance = teachers[character]['Cri']
        self.wlevel = 1

class PlayerBullet:
    def __init__(self, x, y, mouse_x, mouse_y, a):
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.initx = x
        self.inity = y
        self.speed = 5
        # self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.angle = a
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
    def main(self, display, player):
        global pause
        self.initx -= int(self.x_vel)
        self.inity -= int(self.y_vel)
        gameDisplay.blit(pygame.transform.scale(player.bimage, (20,20)), (self.initx+25, self.inity+25))
    # check if bullet is in the boundary of the enemy, considering the image sprite coordinate is at the left corner.
    def check(self, display, follower, follower2, follower3):
        if round(follower[0]) < self.initx+25 and round(follower[0])+50 > self.initx+25:
            if round(follower[1]) < self.inity+25 and round(follower[1])+50 > self.inity+25:
                pygame.draw.circle(gameDisplay, red, (follower[0]+25, follower[1]+25), 9)
                return 1
        if round(follower2[0]) < self.initx+25 and round(follower2[0])+50 > self.initx+25:
            if round(follower2[1]) < self.inity+25 and round(follower2[1])+50 > self.inity+25:
                pygame.draw.circle(gameDisplay, red, (follower2[0]+25, follower2[1]+25), 9)
                return 2
        if round(follower3[0]) < self.initx+25 and round(follower3[0])+50 > self.initx+25:
            if round(follower3[1]) < self.inity+25 and round(follower3[1])+50 > self.inity+25:
                pygame.draw.circle(gameDisplay, red, (follower3[0]+25, follower3[1]+25), 9)
                return 3
                
class En():
    def __init__(self, player):
        self.initHP = 20
        self.HP = 20
        self.attack = 5
    # obtained from stack overflow FolloeMe Function, more credits in the game.
    def Enemy(self, pops, fpos, VELOCITY):
        target_vector       = pygame.math.Vector2(*pops)
        follower_vector     = pygame.math.Vector2(*fpos)
        new_follower_vector = pygame.math.Vector2(*fpos)

        distance = follower_vector.distance_to(target_vector)
        if distance > minimum_distance:
            direction_vector    = (target_vector - follower_vector) / distance
            min_step            = max(0, distance - maximum_distance)
            max_step            = distance - minimum_distance
            # step_distance       = min(max_step, max(min_step, VELOCITY))
            step_distance       = min_step + (10) * LERP_FACTOR * VELOCITY
            new_follower_vector = follower_vector + direction_vector * step_distance

        return (new_follower_vector.x, new_follower_vector.y) 