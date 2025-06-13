# Import required modules
import pygame   # Library for creating games and multimedia applications
import sys      # System-specific parameters and functions (used here to quit the program)
import random   # Module to generate random numbers or selections
import os       # Operating system interfaces for file handling

# Import custom classes for player and food objects
from player import Player
from food import Food

# -------------------------
# --- GAME CONFIGURATION ---
# -------------------------

WIDTH, HEIGHT = 800, 600       # Set window size: width and height in pixels
FPS = 60                      # Frames per second (how many times the screen updates each second)
ASSETS_PATH = "assets"         # Folder where all game images and sounds are stored
FONT_COLOR = (255, 255, 255)   # White color for all text (RGB format)
FOOD_TYPES = ['shrimp', 'fish', 'toxin']  # Different types of food items in the game
HIGHSCORE_FILE = "highscore.txt"           # File to save and load the highest score

# -------------------------
# --- UTILITY FUNCTIONS ---
# -------------------------

def draw_text(screen, text, font, color, x, y, center=True):
    """
    Draws text on the screen.
    
    Parameters:
    - screen: the pygame display surface to draw on
    - text: the string to display
    - font: the font object to render the text
    - color: RGB tuple for text color
    - x, y: position coordinates on the screen
    - center: if True, position is the center of the text; if False, position is top-left corner
    """
    surface = font.render(text, True, color)   # Render the text to a new surface
    rect = surface.get_rect()                   # Get the rectangular area of the text surface
    if center:
        rect.center = (x, y)                    # Center the rectangle on (x, y)
    else:
        rect.topleft = (x, y)                   # Place the top-left corner at (x, y)
    screen.blit(surface, rect)                   # Draw the text surface onto the screen

def draw_text_with_outline(screen, text, font, text_color, outline_color, x, y, center=True):
    """
    Draws text with an outline to improve readability against any background.
    
    This function draws the text multiple times slightly offset in different directions 
    to create an outline effect, then draws the main text on top.
    """
    base = font.render(text, True, text_color)       # The main text surface
    outline = font.render(text, True, outline_color) # The outline text surface

    rect = base.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)

    # Draw outline by blitting the outline text in four directions around the main text
    for dx in [-1, 1]:
        for dy in [-1, 1]:
            outline_rect = rect.copy()
            outline_rect.move_ip(dx, dy)  # Move outline position by (dx, dy)
            screen.blit(outline, outline_rect)

    screen.blit(base, rect)  # Draw the main text on top

def load_high_score():
    """
    Reads the highest score from the highscore file.
    
    Returns:
    - The stored high score as an integer.
    - Returns 0 if the file doesn't exist or contains invalid data.
    """
    if os.path.exists(HIGHSCORE_FILE):
        try:
            with open(HIGHSCORE_FILE, "r") as file:
                return int(file.read())  # Read and convert the score to integer
        except:
            return 0  # Return 0 if the file is corrupted or data is not an integer
    return 0  # Return 0 if the file does not exist

def save_high_score(score):
    """
    Saves the new highest score to the highscore file.
    
    Parameters:
    - score: the integer score to save
    """
    with open(HIGHSCORE_FILE, "w") as file:
        file.write(str(score))  # Convert the score to string and write it

def how_to_play(screen, font, background, assets_path):
    """
    Displays the 'How to Play' screen explaining game controls and mechanics.
    
    The player can read instructions and press SPACE to start the game.
    """
    # Load and scale images for the player character and food items
    axolotl = pygame.image.load(os.path.join(assets_path, "axolotl_1.png"))
    shrimp = pygame.image.load(os.path.join(assets_path, "food_shrimp.png"))
    fish = pygame.image.load(os.path.join(assets_path, "food_fish.png"))
    toxin = pygame.image.load(os.path.join(assets_path, "food_toxin.png"))

    axolotl = pygame.transform.scale(axolotl, (140, 140))
    shrimp = pygame.transform.scale(shrimp, (110, 110))
    fish = pygame.transform.scale(fish, (110, 110))
    toxin = pygame.transform.scale(toxin, (110, 110))

    soft_pink = (255, 105, 180)                    # Color used for header text
    header_font = pygame.font.SysFont(None, 44)   # Font used for the header

    # Main loop to keep the instruction screen visible until user presses SPACE or closes window
    while True:
        screen.blit(background, (0, 0))  # Draw the background image

        # Draw header text centered at the top
        draw_text(screen, "HOW TO PLAY", header_font, soft_pink, WIDTH // 2, 100)

        # Draw player character and control instructions
        screen.blit(axolotl, (80, 180))
        draw_text(screen, "Use A / D or Left / Right", font, FONT_COLOR, 50, 330, center=False)
        draw_text(screen, "arrow keys to move", font, FONT_COLOR, 50, 360, center=False)

        # Draw food items and their effects
        screen.blit(shrimp, (300, 180))
        draw_text(screen, "+1 point", font, FONT_COLOR, 355, 310)

        screen.blit(fish, (440, 180))
        draw_text(screen, "+1 point", font, FONT_COLOR, 495, 310)

        screen.blit(toxin, (580, 180))
        draw_text(screen, "-1 life!", font, FONT_COLOR, 635, 310)

        # Additional instructions at the bottom
        draw_text(screen, "Collect snacks. Avoid toxins.", font, FONT_COLOR, WIDTH // 2, 440)
        draw_text(screen, "Press SPACE to START", font, FONT_COLOR, WIDTH // 2, 500)

        # *** Creator credit at bottom-left ***
        draw_text(screen, "Created by Hülya Ceren Lüleci", font, (180, 180, 180), 10, HEIGHT - 30, center=False)

        pygame.display.flip()  # Update the full display

        # Handle user events such as quitting or pressing keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit pygame properly
                sys.exit()     # Exit the program
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return  # Exit this function and start the game
# -------------------------
# --- MAIN GAME FUNCTION ---
# -------------------------

def main():
    # Initialize all imported pygame modules (graphics, sound, etc.)
    pygame.init()
    pygame.mixer.init()  # Initialize sound mixer

    # Set up the main game window with specified width and height
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SnackLotl")  # Set window title
    clock = pygame.time.Clock()  # Create a clock to control frame rate
    font = pygame.font.SysFont(None, 36)  # Default font for game text

    # Load and scale background image to fit window size
    background = pygame.image.load(os.path.join(ASSETS_PATH, "background.jpg"))
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Load background music if it exists, and start playing it on loop
    music_path = os.path.join(ASSETS_PATH, "music.ogg")
    if os.path.exists(music_path):
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(1.0)  # Max volume
        pygame.mixer.music.play(-1)  # Loop indefinitely
    else:
        print("Music file not found:", music_path)

    # Variables for the start screen
    in_start_screen = True
    title_font = pygame.font.SysFont(None, 80)  # Larger font for title
    sub_font = pygame.font.SysFont(None, 36)    # Subtitle font
    soft_pink = (255, 153, 204)                  # Soft pink color for title

    # Start screen loop — waits for player to press SPACE to continue
    while in_start_screen:
        screen.blit(background, (0, 0))  # Draw background image

        # Draw the game title with an outline and subtitles below
        draw_text_with_outline(screen, "SnackLotl", title_font, soft_pink, (0, 0, 0), WIDTH // 2, HEIGHT // 2 - 80)
        draw_text(screen, "An underwater axolotl food journey", sub_font, FONT_COLOR, WIDTH // 2, HEIGHT // 2)
        draw_text(screen, "Press SPACE to learn how to play SnackLotl!", sub_font, FONT_COLOR, WIDTH // 2, HEIGHT // 2 + 60)

         # *** Creator credit at bottom-left ***
        draw_text(screen, "Created by Hülya Ceren Lüleci", font, (180, 180, 180), 10, HEIGHT - 30, center=False)

        pygame.display.flip()  # Update display to show these changes

        # Event handling for quitting or starting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # User clicks close button
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                in_start_screen = False  # Exit start screen loop

    # Show instructions screen before game begins
    how_to_play(screen, font, background, ASSETS_PATH)

    # Initialize game objects and variables
    player = Player(WIDTH // 2, HEIGHT - 80, 160, ASSETS_PATH)  # Player starts near bottom center
    foods = []               # List to hold food objects falling from top
    score = 0                # Player's current score
    lives = 3                # Player's remaining lives
    game_over = False        # Flag to indicate game over state
    high_score = load_high_score()  # Load saved high score from file
    speed = 5                # Initial falling speed of food items
    spawn_event = pygame.USEREVENT + 1  # Custom event for spawning food
    pygame.time.set_timer(spawn_event, 1000)  # Trigger spawn_event every 1000 ms (1 second)
    last_speed_increase_score = 0  # Track when speed last increased based on score

    # Main game loop
    while True:
        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit the game window
                pygame.quit()
                sys.exit()
            if event.type == spawn_event and not game_over:
                # Spawn a random food item every second
                food_type = random.choice(FOOD_TYPES)
                food = Food(food_type, ASSETS_PATH, WIDTH)
                food.SPEED = speed
                foods.append(food)
            if event.type == pygame.KEYDOWN and game_over:
                # After game over, listen for restart or quit commands
                if event.key == pygame.K_r:
                    return main()  # Restart the game by calling main() again
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        keys = pygame.key.get_pressed()  # Get current keyboard state
        if not game_over:
            # Player movement controls: left and right arrows or A/D keys
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player.move(-10)  # Move player left by 10 pixels
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player.move(10)   # Move player right by 10 pixels

        # Draw the background image
        screen.blit(background, (0, 0))

        if not game_over:
            # Increase speed gradually every 10 points scored
            if score // 10 > last_speed_increase_score:
                speed += 0.5
                last_speed_increase_score = score // 10

            # Update and draw all food items
            for food in foods[:]:  # Iterate over a copy to allow safe removal
                food.SPEED = speed
                food.fall()          # Make food fall down the screen
                food.draw(screen)    # Draw food on the screen

                # Check collision between player and food
                if food.rect.colliderect(player.rect):
                    if food.type == 'toxin':
                        # Toxins reduce player's life
                        lives -= 1
                        foods.remove(food)
                        if lives <= 0:
                            # Trigger game over if no lives left
                            game_over = True
                            if score > high_score:
                                high_score = score  # Update high score
                                save_high_score(score)  # Save new high score
                    else:
                        # Normal food increases score
                        score += 1
                        foods.remove(food)
                        player.trigger_animation()  # Play player eating animation

                # Remove food if it falls below the screen
                elif food.y > HEIGHT:
                    foods.remove(food)

            # Update and draw the player character
            player.update()
            player.draw(screen)

            # Draw game stats on screen
            draw_text(screen, f"Score: {score}", font, FONT_COLOR, 10, 10, center=False)
            draw_text(screen, f"Lives: {lives}", font, FONT_COLOR, 10, 50, center=False)
            draw_text(screen, f"High Score: {high_score}", font, FONT_COLOR, WIDTH - 200, 10, center=False)

        else:
            # Display game over screen with final score and instructions
            draw_text(screen, "GAME OVER", font, (255, 0, 128), WIDTH//2, HEIGHT//2 - 60)
            draw_text(screen, f"Final Score: {score}", font, FONT_COLOR, WIDTH//2, HEIGHT//2 + 10)
            draw_text(screen, f"High Score: {high_score}", font, FONT_COLOR, WIDTH//2, HEIGHT//2 + 50)
            draw_text(screen, "Press R to Restart or Q to Quit", font, FONT_COLOR, WIDTH//2, HEIGHT//2 + 90)

        # *** Creator credit at bottom-left ***
            draw_text(screen, "Created by Hülya Ceren Lüleci", font, (180, 180, 180), 10, HEIGHT - 30, center=False)

        pygame.display.flip()  # Update the full display surface to the screen
        clock.tick(FPS)        # Control the game frame rate

# Standard Python idiom to call main function if this file is run directly
if __name__ == "__main__":
    main()
