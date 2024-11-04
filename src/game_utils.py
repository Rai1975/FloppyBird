def check_collision(player, obstacles, screen_height):
    # Check if the player hits the top or bottom of the screen
    if player.rect.top <= 0 or player.rect.bottom >= screen_height:
        return True
    # Check collision with obstacles
    for obstacle in obstacles:
        if player.rect.colliderect(obstacle.rect):
            return True
    return False
