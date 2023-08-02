from typing import Tuple

from gameboard import GameBoard
from snake import Snake

class Game:
    def __init__(self, size: int):
        self.board = GameBoard(size)
        self.snake = Snake((0, 0))

    def start(self):
        self.board.place_snake(self.snake.get_head_position())
        self.board.place_food()
        self.board.display_board()
        while True:
            self.handle_input()
            self.board.update_board()
            self.board.display_board()
            if self.check_game_over():
                self.game_over()
                break

    def handle_input(self):
        # Code to handle user input to control the snake's movement
        pass

    def check_game_over(self) -> bool:
        head_position = self.snake.get_head_position()
        if not self.board.is_valid_position(head_position):
            return True
        if self.board.is_snake_position(head_position):
            return True
        return False

    def game_over(self):
        print("Game Over")

game = Game(10)
game.start()
