import pygame

# Constants
GRAVITY = 0.7
FLAP_STRENGTH = -10

class Player:
    def __init__(self):
        self.image = pygame.image.load('./assets/player.png').convert_alpha()
        self.rect = self.image.get_rect(center=(50, 300))  # Centered vertically on the screen
        self.velocity = 0

    def jump(self):
        self.velocity = FLAP_STRENGTH

    def apply_gravity(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

    def draw(self, screen):
        screen.blit(self.image, self.rect)