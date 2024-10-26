import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Optimized Image Scaling")

# Define circle properties
circle_pos = (400, 300)  # Position to display the circle
radius = 50  # Desired radius for the circle

# Load and scale the image once
circle_image = pygame.image.load('circle.png').convert_alpha()
scaled_circle_image = pygame.transform.scale(circle_image, (2 * radius, 2 * radius))

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen with a background color
    screen.fill((30, 30, 30))

    # Draw the pre-scaled circle image
    # Center it at circle_pos
    screen.blit(scaled_circle_image, (circle_pos[0] - radius, circle_pos[1] - radius))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 FPS
    clock.tick(60)

pygame.quit()
