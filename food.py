from typing import List, Tuple

class Food:
    def __init__(self, pos: Tuple[int, int]):
        self.pos = pos

    def draw(self, game_board: List[List[str]]):
        x, y = self.pos
        game_board[x][y] = '*'