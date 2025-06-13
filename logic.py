import random
import pygame
from player import Player
from food import Food

class Game:
    def __init__(self, width, height, assets_path):
        self.width = width
        self.height = height
        self.assets_path = assets_path

        # Initialize player at the bottom center of the screen
        self.player = Player(width // 2, height - 50, 80, assets_path)

        # List to hold falling food items
        self.food_items = []

        # Initial values
        self.score = 0
        self.lives = 3
        self.game_over = False

        # Font for UI text
        self.font = pygame.font.SysFont(None, 48)

        # Start with some food on screen
        self.spawn_food()

    def spawn_food(self):
        """Spawns 3 food items (randomly shrimp, fish, or toxin)."""
        types = ['shrimp', 'fish', 'toxin']
        self.food_items.clear()  # Clear existing items
        for _ in range(3):
            ftype = random.choice(types)
            food = Food(ftype, self.assets_path, self.width)
            self.food_items.append(food)

    def update(self, direction):
        """Updates game logic: player movement, food falling, collisions, lives & score."""
        if self.game_over:
            return

        # Move player left or right
        if direction == "LEFT":
            self.player.move(-10)
        elif direction == "RIGHT":
            self.player.move(10)

        # Update each food item
        for food in self.food_items:
            food.fall()

            # Check collision between player and food
            if food.rect.colliderect(self.player.rect):
                if food.type == 'toxin':
                    self.lives -= 1
                    if self.lives <= 0:
                        self.game_over = True  # End game if lives are 0
                else:
                    self.score += 1  # Collecting good food increases score

                # Respawn food at random position above screen
                food.x = random.randint(20, self.width - 20)
                food.y = -50
                food.rect.center = (food.x, food.y)

            # If food falls off screen, respawn it from the top
            elif food.y > self.height + 20:
                food.x = random.randint(20, self.width - 20)
                food.y = -50
                food.rect.center = (food.x, food.y)

    def draw(self, screen):
        """Draws the entire game state: background, player, food, score, lives, game over screen."""
        # Draw background
        bg = pygame.image.load(f"{self.assets_path}/background.jpg")
        bg = pygame.transform.scale(bg, (self.width, self.height))
        screen.blit(bg, (0, 0))

        # Draw food items
        for food in self.food_items:
            food.draw(screen)

        # Draw player
        self.player.draw(screen)

        # Draw UI (score and lives)
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        lives_text = self.font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 60))

        # If game is over, show end screen text
        if self.game_over:
            over_text = self.font.render("GAME OVER", True, (255, 20, 147))
            rect = over_text.get_rect(center=(self.width // 2, self.height // 2 - 30))
            screen.blit(over_text, rect)

            msg_text = self.font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
            msg_rect = msg_text.get_rect(center=(self.width // 2, self.height // 2 + 30))
            screen.blit(msg_text, msg_rect)
