# Minesweeper

A terminal-based Minesweeper game written in Python. The game generates a board with randomly placed bombs, calculates the number of bombs surrounding each cell, and recursively reveals safe areas as the player digs through the board.

## Features

- Random bomb placement for a different board each game
- Numbered cells showing the count of adjacent bombs
- Recursive revealing of connected empty cells
- Row and column labels for coordinate-based input
- Input boundary validation
- Win and loss detection
- Full-board reveal after a bomb is selected

## Technologies Used

- Python 3
- Python standard library (`random` and `re`)

No external packages are required.

## Getting Started

### Prerequisites

Install Python 3 and confirm that it is available:

```bash
python3 --version
```

### Run the Game

1. Clone or download the repository.
2. Open a terminal in the project folder.
3. Run the program:

```bash
python3 MineSweeper.py
```

On Windows, depending on your installation, you may instead use:

```bash
python MineSweeper.py
```

## How to Play

The default game uses a 10-by-10 board containing 10 bombs. Enter the row and column of the cell you want to uncover, separated by a comma:

```text
Where would you like to dig? Input as row,col: 3,4
```

You may also include a space after the comma:

```text
3, 4
```

After a safe cell is uncovered:

- A positive number indicates how many bombs are present in the surrounding eight cells.
- A `0` indicates that no bombs are adjacent. Its neighboring safe cells are uncovered automatically.
- Selecting a bomb ends the game and reveals the complete board.

You win after uncovering every cell that does not contain a bomb.

## Project Structure

```text
MineSweeper.py   # Board generation, game logic, display, and main game loop
```

## How It Works

The `Board` class is responsible for:

- Creating the two-dimensional game board
- Planting bombs at unique random positions
- Calculating adjacent-bomb counts for safe cells
- Tracking uncovered coordinates in a set
- Recursively uncovering neighboring cells when an empty cell is selected
- Producing the terminal representation of the visible board

The `play()` function creates the board, accepts and validates player coordinates, performs each dig, and determines whether the player has won or selected a bomb.

## Customizing the Board

The `play` function accepts the board size and number of bombs:

```python
play(dimension_size=10, num_bombs=10)
```

Change these values at the bottom of `MineSweeper.py` to adjust the difficulty. The number of bombs should be less than the total number of cells on the board.

## Technical Highlights

- Uses a two-dimensional list to represent the board.
- Uses a set of `(row, column)` tuples for efficient tracking of uncovered cells.
- Converts a random one-dimensional position into row and column coordinates.
- Handles board edges with bounded neighbor ranges.
- Applies recursion to reveal connected regions containing no adjacent bombs.

## Future Improvements

- Add flags for suspected bomb locations
- Validate non-numeric and incorrectly formatted input
- Allow players to choose the board size and bomb count at startup
- Add difficulty presets
- Build a graphical user interface

## Author

Abdelrahman Abdelaal
