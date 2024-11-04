import pygame
from player import Player
from obstacle import create_obstacles, Obstacle
from game_utils import check_collision

# Initialize Pygame and constants
pygame.init()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Floppy Bird")
clock = pygame.time.Clock()

# Initialize player, obstacles, and variables
player = Player()
obstacles = []
obstacle_timer = 0
score = 0
game_over = False

# Main game loop
running = True
while running:
    screen.fill(WHITE)  # Clear the screen with a white background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                player.jump()
            if event.key == pygame.K_r and game_over:  # Reset game with 'R' key
                game_over = False
                player = Player()
                obstacles.clear()
                score = 0

    if not game_over:
        # Apply gravity and move the player
        player.apply_gravity()
        player.draw(screen)

        # Generate new obstacles periodically
        if obstacle_timer > 1500:
            obstacles.extend(create_obstacles(SCREEN_WIDTH, SCREEN_HEIGHT))
            obstacle_timer = 0
            score += 1

        # Move and draw obstacles
        for obstacle in obstacles:
            obstacle.move()
            obstacle.draw(screen)

        # Remove off-screen obstacles
        obstacles = [obs for obs in obstacles if obs.rect.x > -obs.rect.width]

        # Check for collisions
        if check_collision(player, obstacles, SCREEN_HEIGHT):
            game_over = True

        # Increment timer
        obstacle_timer += clock.get_time()

    else:
        # Game over text
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over! Press R to Restart", True, BLACK)
        screen.blit(text, (50, SCREEN_HEIGHT // 2 - 20))

    # Display the score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()  # Update the display
    clock.tick(60)  # Cap the frame rate

pygame.quit()
