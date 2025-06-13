import pygame
import random
import os

class Food:
    SPEED = 5  # Falling speed of food

    def __init__(self, food_type, assets_path, screen_width):
        self.type = food_type  # shrimp, fish, or toxin
        self.assets_path = assets_path

        # Random initial horizontal position
        self.x = random.randint(20, screen_width - 20)
        self.y = -50  # Start above the visible screen

        # Load and scale the correct image based on type
        self.load_image()

        # Create a rect for positioning and collision
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def load_image(self):
        """Load and scale the image for the given food type."""
        if self.type == 'shrimp':
            filename = 'food_shrimp.png'
        elif self.type == 'fish':
            filename = 'food_fish.png'
        elif self.type == 'toxin':
            filename = 'food_toxin.png'
        else:
            filename = 'food_fish.png'  # default fallback

        # Load and scale image to 100x100
        self.image = pygame.image.load(os.path.join(self.assets_path, filename))
        self.image = pygame.transform.scale(self.image, (100, 100))

    def fall(self):
        """Move the food down by its speed."""
        self.y += self.SPEED
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        """Draw the food item on the screen."""
        screen.blit(self.image, self.rect)
