Based on the requirements and assumptions, here are the core classes, functions, and methods that will be necessary:

1. GameBoard class:
   - `__init__(self, size: int)` - Initializes the game board with a given size.
   - `place_snake(self, position: Tuple[int, int])` - Places the snake on the game board at the given position.
   - `place_food(self)` - Places food randomly on the game board.
   - `is_valid_position(self, position: Tuple[int, int])` - Checks if a given position is valid on the game board.
   - `is_food_position(self, position: Tuple[int, int])` - Checks if a given position contains food.
   - `is_snake_position(self, position: Tuple[int, int])` - Checks if a given position contains the snake.
   - `update_board(self)` - Updates the game board with the current positions of the snake and food.
   - `display_board(self)` - Displays the current state of the game board.

2. Snake class:
   - `__init__(self, position: Tuple[int, int])` - Initializes the snake with a given position.
   - `move(self, direction: str)` - Moves the snake in the specified direction.
   - `grow(self)` - Increases the length of the snake by 1 unit.
   - `get_head_position(self)` - Returns the current position of the snake's head.
   - `get_body_positions(self)` - Returns a list of positions occupied by the snake's body.

3. Game class:
   - `__init__(self, size: int)` - Initializes the game with a given size.
   - `start(self)` - Starts the game loop.
   - `handle_input(self)` - Handles user input to control the snake's movement.
   - `check_game_over(self)` - Checks if the game is over.
   - `game_over(self)` - Displays the game over message and ends the game.

Now, let's proceed with creating the necessary files and implementing the code.

1. gameboard.py

