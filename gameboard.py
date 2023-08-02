class GameBoard:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.board = [[' ' for _ in range(width)] for _ in range(height)]

    def draw(self):
        for row in self.board:
            print(' '.join(row))

    def clear(self):
        self.board = [[' ' for _ in range(self.width)] for _ in range(self.height)]

