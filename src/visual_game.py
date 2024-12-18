import pygame

pygame.init()

pygame.display.set_caption("Yahtzee")
screen = pygame.display.set_mode((420,720))

clock = pygame.time.Clock()

pygame.draw.rect(screen, (40, 40, 40), (10, 10, 1), 1)

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    screen.fill("purple")  # Fill the display with a solid color

    # Render the graphics here.

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)