
# Game of Life - Thomas CDOF1

This project implements **Conway's Game of Life**, a famous cellular automaton devised by mathematician John Horton Conway. The game simulates the evolution of a grid of cells that can either be alive or dead, according to simple rules.


## How the Game Works

The Game of Life operates on a grid where each cell is either alive (`#`) or dead (space). The game follows these simple rules:

1. **Underpopulation**: A living cell with fewer than 2 live neighbors dies.
2. **Survival**: A living cell with 2 or 3 live neighbors continues to live.
3. **Overpopulation**: A living cell with more than 3 live neighbors dies.
4. **Reproduction**: A dead cell with exactly 3 live neighbors becomes a live cell.

## Installation

To install and set up the project, follow these steps:

1. Clone the repository from GitHub:

    ```bash
    git clone https://github.com/Thoomasdkzh/Game_of_life_Thomas_CDOF1.git
    cd Game_of_life_Thomas_CDOF1
    ```

2. Install the project using `setup.py`:

    ```bash
    python setup.py install
    ```

3. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Game Manually

After installation, you can run the game manually in two ways:

1. **Directly run the game script**:

    ```bash
    python Game_of_Life/game_of_life.py
    ```

2. **Run it as a Python module** after installation:

    ```bash
    python -m Game_of_Life.game_of_life
    ```

## Example Output

The game will print a grid to the console where `#` represents live cells, and spaces represent dead cells. The grid evolves over time following the rules of Conway's Game of Life.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

