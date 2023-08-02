from typing import Tuple
import pygame
import time
import random
import sys

from gameboard import GameBoard
from snake import Snake
from food import Food

BLOCK_SIZE = 40
START_SCREEN_DELAY = 2000  # in milliseconds


class GameController:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.game_board = GameBoard(width, height)
        self.snake = Snake((height // 2, width // 2), 3)
        self.food = self.generate_food()
        self.game_over_flag = False

    def start_game(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width * BLOCK_SIZE, self.height * BLOCK_SIZE))
        pygame.display.set_caption("Snake Game")

        # Ask for speed before starting the game
        speed = self.select_speed(screen)

        clock = pygame.time.Clock()

        self.draw_start_screen(screen)
        pygame.display.update()
        pygame.time.delay(START_SCREEN_DELAY)

        speed_dict = {'slow': 6, 'medium': 14 , 'fast': 25}  # These are inversely proportional, faster speed = less delay
        delay = 1 / speed_dict[speed]

        # Set initial direction to right
        direction = (1, 0)

        while True:
            pygame.time.delay(int(delay * 1000))  # Delay converted to milliseconds
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    direction = self.handle_input(event)

            self.snake.move(direction)
            if self.snake.check_collision(self.width, self.height):
                self.game_over(screen)
                self.game_over_flag = True

            if self.game_over_flag:
                break

            self.update(screen)
            pygame.display.update()  # Use the selected speed


    def select_speed(self, screen):
        font = pygame.font.Font(None, 24)
        text = font.render("Select speed: 1 - Slow, 2 - Medium, 3 - Fast", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        print('slow')
                        speed = 1
                        return 'slow'
                    elif event.key == pygame.K_2:
                        print('medium')
                        speed = 2
                        return 'medium'
                    elif event.key == pygame.K_3:
                        print('fast')
                        speed = 3
                        return 'fast'

    def draw_start_screen(self, screen):
        screen.fill((0, 0, 0))
        # Draw the snake
        for x, y in self.snake.body:
            pygame.draw.rect(screen, (0, 255, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        # Draw the food
        pygame.draw.rect(screen, (255, 0, 0), (self.food.pos[0] * BLOCK_SIZE, self.food.pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def handle_input(self, event) -> str:
        if event.key == pygame.K_UP:
            return 'left'
        elif event.key == pygame.K_DOWN:
            return 'right'
        elif event.key == pygame.K_LEFT:
            return 'up'
        elif event.key == pygame.K_RIGHT:
            return 'down'
        elif event.key == pygame.K_w:
            return 'up'
        elif event.key == pygame.K_s:
            return 'down'
        elif event.key == pygame.K_a:
            return 'left'
        elif event.key == pygame.K_d:
            return 'right'

    def update(self, screen) -> bool:
        screen.fill((0, 0, 0))  # clear the screen
        # Draw the snake
        for x, y in self.snake.body:
            pygame.draw.rect(screen, (0, 255, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        # Draw the food
        pygame.draw.rect(screen, (255, 0, 0), (self.food.pos[0] * BLOCK_SIZE, self.food.pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        if self.snake.body[0] == self.food.pos:
            self.snake.grow()
            self.food = self.generate_food()

    def game_over(self, screen):
        score = self.snake.length
        self.game_over_flag = True
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 24)  # Adjust the font size as desired
        text = font.render(f"Game Over! Score: {score}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        print(f"Game Over! Score: {score}")
        time.sleep(5)  # Pause for 5 seconds

        
    def generate_food(self) -> Food:
        while True:
            # Generate a random position for the food
            food_pos = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))

            # Ensure that the position is not occupied by the snake
            if food_pos not in self.snake.body:
                break

        # Return a new Food object with the generated position
        return Food(food_pos)
