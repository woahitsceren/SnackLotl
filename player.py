import pygame
import os

class Player:
    def __init__(self, x, y, size, assets_path):
        self.x = x
        self.y = y
        self.size = size
        self.assets_path = assets_path

        # Load animation frames (4 pieces)
        self.frames = []
        for i in range(1, 5):
            image = pygame.image.load(os.path.join(assets_path, f"axolotl_{i}.png")).convert_alpha()
            image = pygame.transform.scale(image, (size, size))
            self.frames.append(image)

        self.current_frame = 0
        self.animation_triggered = False
        self.animation_counter = 0
        self.animation_speed = 10  # How many game frames does it take to change an animation frame?

        self.rect = self.frames[0].get_rect(center=(self.x, self.y))

    def move(self, dx):
        self.x += dx

        # Preserve screen borders (example: WIDTH=800)
        if self.x < self.size // 2:
            self.x = self.size // 2
        elif self.x > 800 - self.size // 2:
            self.x = 800 - self.size // 2

        self.rect.center = (self.x, self.y)

    def update(self):
        if self.animation_triggered:
            self.animation_counter += 1
            if self.animation_counter >= self.animation_speed:
                self.animation_counter = 0
                self.current_frame += 1
                if self.current_frame > 3:  # There are 0,1,2,3, the animation is over
                    self.current_frame = 0
                    self.animation_triggered = False
        else:
            self.current_frame = 0  # Idle frame

        self.rect = self.frames[self.current_frame].get_rect(center=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.frames[self.current_frame], self.rect)

    def trigger_animation(self):
        self.animation_triggered = True
        self.current_frame = 1  # Animation starts from frame 2 (index 1)
        self.animation_counter = 0
