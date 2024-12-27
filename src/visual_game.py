# import pygame

# pygame.init()

# pygame.display.set_caption("Yahtzee")
# screen = pygame.display.set_mode((420,720))

# clock = pygame.time.Clock()

# pygame.draw.rect(screen, (40, 40, 40), (10, 10, 1), 1)

# while True:
#     # Process player inputs.
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             raise SystemExit

#     # Do logical updates here.
#     # ...

#     screen.fill("purple")  # Fill the display with a solid color

#     # Render the graphics here.

#     # Draw a solid blue circle in the center
#     pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

#     pygame.display.flip()  # Refresh on-screen display
#     clock.tick(60)         # wait until next frame (at 60 FPS)
from game_mechanics import YahtzeeMechanics
import pygame
import sys
from typing import List

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("YahtzeeZero")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Dice positions
DICE_POSITIONS = [(10 + i * 120, 550) for i in range(5)]  # Five dice spaced out horizontally

# Score categories
CATEGORIES = ["1s", "2s", "3s", "4s", "5s", "6s", "Set", "Quads", "Fullhouse", "Straight", "Yahtzee"]
SCORE_POSITIONS = [(100, 100 + i * 40) for i in range(len(CATEGORIES))]  # Vertical list on the right

def draw_dice(dice_values: List[int]):
    """Draw dice on the screen."""
    for i, value in enumerate(dice_values):
        x, y = DICE_POSITIONS[i]
        pygame.draw.rect(screen, BLUE, (x, y, 100, 100))  # Draw dice as rectangles
        text = font.render(str(value), True, WHITE)
        text_rect = text.get_rect(center=(x + 50, y + 50))
        screen.blit(text, text_rect)

def main():
    clock = pygame.time.Clock()
    running = True

    # Create an instance of YahtzeeGame
    yahtzee_game = YahtzeeMechanics()

    # Visual dices dict for the event of holding a dice
    dices_rect = {}
    # When we click a dice we want to hold it
    dices_to_reroll = [0, 1, 2, 3, 4] # contains the indexes of the dices to reroll

    while running:
        screen.fill(WHITE)  # Clear the screen

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # Check if the "Roll Dice" button is clicked
                if roll_rect.collidepoint(mouse_x, mouse_y):
                    yahtzee_game.roll_dice(dices_to_reroll)
                # Check if the dices are clicked
                for i, value in enumerate(yahtzee_game.dices):
                    if dices_rect[i].collidepoint(mouse_x, mouse_y):
                        # Toggle between hold and allow to roll
                        if i in dices_to_reroll:
                            # Remove the index of the dices
                            dices_to_reroll.remove(i)
                        else:
                            dices_to_reroll.append(i)
                # Check if a category is clicked
                for i, (x, y) in enumerate(SCORE_POSITIONS):
                    if x <= mouse_x <= x + 200 and y <= mouse_y <= y + 30:  # Click within category area
                        category = CATEGORIES[i]
                        yahtzee_game.mark_score(category)
                        dices_to_reroll = [0, 1, 2, 3, 4] # Reset hold dices for next turn
                            
        #Draw the scoresheet on the screen
        for i, category in enumerate(CATEGORIES):
            x, y = SCORE_POSITIONS[i]
            # Draw category name
            category_text = font.render(category, True, BLACK)
            screen.blit(category_text, (x, y))

            # Draw score or placeholder
            score = yahtzee_game.score_board[i]
            if score is -1:
                score_text = font.render("0", True, GRAY)
            else:
                score_text = font.render(str(score), True, GREEN)
            screen.blit(score_text, (x + 100, y))
        
        # Draw the dice
        for i, value in enumerate(yahtzee_game.dices):
            x, y = DICE_POSITIONS[i]
            text = font.render(str(value), True, WHITE)
            dices_rect[i] = text.get_rect(center=(x + 50, y + 50))
            if i in dices_to_reroll:
                pygame.draw.rect(screen, BLUE, (x, y, 100, 100))  # Draw dice as blue rectangle
            else:
                pygame.draw.rect(screen, RED, (x, y, 100, 100))  # Draw dice as red rectangle
            screen.blit(text, dices_rect[i])

        # Render scoresheet placeholder
        scoresheet_text = font.render("Scoresheet (Coming Soon)", True, BLACK)
        screen.blit(scoresheet_text, (50, 50))

        # Render buttons placeholder
        roll_button = font.render("Roll Dice", True, BLACK)
        roll_rect = roll_button.get_rect(topleft=(50, 700))
        pygame.draw.rect(screen, RED, roll_rect.inflate(20, 10))
        screen.blit(roll_button, roll_rect)

        # Update the display
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
