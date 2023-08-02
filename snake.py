from typing import List, Tuple
import pygame


class Snake:
    def __init__(self, start_pos: Tuple[int, int], length: int):
        self.body = [start_pos]
        self.length = length
        self.direction = 'right'

    direction = 'up'
    
    def move(self, direction: str = None):
        if direction:
            if direction == 'up' and self.direction != 'down':
                self.direction = 'up'
            elif direction == 'down' and self.direction != 'up':
                self.direction = 'down'
            elif direction == 'left' and self.direction != 'right':
                self.direction = 'left'
            elif direction == 'right' and self.direction != 'left':
                self.direction = 'right'

        head = self.body[0]
        if self.direction == 'up':
            new_head = (head[0] - 1, head[1])
        elif self.direction == 'down':
            new_head = (head[0] + 1, head[1])
        elif self.direction == 'left':
            new_head = (head[0], head[1] - 1)
        elif self.direction == 'right':
            new_head = (head[0], head[1] + 1)

        self.body.insert(0, new_head)
        if len(self.body) > self.length:
            self.body.pop()
        
    def grow(self):
        self.length += 1

    def check_collision(self, width: int, height: int) -> bool:
        head = self.body[0]
        if (
            head[0] < 0 or head[0] >= height or
            head[1] < 0 or head[1] >= width or
            head in self.body[1:]
        ):
            return True
        return False

    def draw(self, game_board: List[List[str]]):
        for i, (x, y) in enumerate(self.body):
            if i == 0:
                game_board[x][y] = 'O'
            else:
                game_board[x][y] = 'X'
