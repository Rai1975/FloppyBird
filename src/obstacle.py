import pygame
import random

SCROLL_SPEED = 3

class Obstacle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def move(self):
        self.rect.x -= SCROLL_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)

def create_obstacles(screen_width, screen_height):
    gap = 150
    width = 70
    height = random.randint(100, 400)

    top_obstacle = Obstacle(screen_width, 0, width, height)
    bottom_obstacle = Obstacle(screen_width, height + gap, width, screen_height - height - gap)
    
    return top_obstacle, bottom_obstacle
