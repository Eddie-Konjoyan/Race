import pygame
import sys
import random
import math

# Pygame setup
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Object properties
radius = 30
mass = 1
initial_speed = 5

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Physics Simulation")
clock = pygame.time.Clock()

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = pygame.Vector2(random.uniform(-initial_speed, initial_speed),
                                       random.uniform(-initial_speed, initial_speed))

    def update(self):
        self.rect.center += self.velocity
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.velocity.x *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.velocity.y *= -1

def elastic_collision(ball1, ball2):
    relative_velocity = ball2.velocity - ball1.velocity
    distance_vector = pygame.Vector2(ball2.rect.center) - pygame.Vector2(ball1.rect.center)
    distance = distance_vector.length()

    normal_vector = distance_vector.normalize()

    # Elastic collision formula
    impulse = 2 * mass * (relative_velocity.dot(normal_vector)) / (2 * mass)
    ball1.velocity += impulse * normal_vector
    ball2.velocity -= impulse * normal_vector

# Create two balls
ball1 = Ball(WIDTH // 4, HEIGHT // 2, WHITE)
ball2 = Ball(3 * WIDTH // 4, HEIGHT // 2, RED)

# Group for collision detection
all_sprites = pygame.sprite.Group()
all_sprites.add(ball1, ball2)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Check for collision
    if pygame.sprite.collide_rect(ball1, ball2):
        elastic_collision(ball1, ball2)

    # Draw
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()