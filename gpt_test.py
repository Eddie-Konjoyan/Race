import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FONT_SIZE = 36
FONT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Lap Timer")

# Load font
font = pygame.font.Font(None, FONT_SIZE)

# Countdown variables
countdown_values = [3, 2, 1]
countdown_index = 0
countdown_timer = pygame.time.get_ticks()
countdown_interval = 1000  # 1 second

# Lap timer variables
timer_running = False
start_time = 0
lap_times = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not timer_running:
                    # Start the countdown
                    countdown_index = 0
                    countdown_timer = pygame.time.get_ticks()
                else:
                    # Stop the timer and record lap time
                    timer_running = False
                    lap_time = pygame.time.get_ticks() - start_time
                    lap_times.append(lap_time)

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    if not timer_running and countdown_index < len(countdown_values):
        # Display countdown
        current_time = pygame.time.get_ticks()
        if current_time - countdown_timer >= countdown_interval:
            countdown_timer = current_time
            countdown_index += 1

        if countdown_index < len(countdown_values):
            countdown_text = str(countdown_values[countdown_index])
            countdown_text_render = font.render(countdown_text, True, FONT_COLOR)
            countdown_rect = countdown_text_render.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(countdown_text_render, countdown_rect)

    elif timer_running:
        # Display current lap time if the timer is running
        current_time = pygame.time.get_ticks() - start_time
        current_text = font.render(f"Current Lap: {current_time / 1000:.2f} seconds", True, FONT_COLOR)
        screen.blit(current_text, (10, SCREEN_HEIGHT - FONT_SIZE - 10))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()