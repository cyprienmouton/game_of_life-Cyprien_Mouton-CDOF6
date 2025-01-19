# Game of Life

This project implements Conway's Game of Life, a cellular automaton that simulates the evolution of a grid of cells based on a set of simple rules. The simulation is written in Python and includes a clean interface for running and observing the grid's behavior over time.

## Features

- Displays a dynamic grid that evolves with each generation.
- Implements Conway's Game of Life rules:
  1. A live cell with 2 or 3 live neighbors survives.
  2. A dead cell with exactly 3 live neighbors becomes alive.
  3. All other live cells die in the next generation, and dead cells stay dead.
- Includes a setup script for easy installation.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/cyprienmouton/game_of_life-Cyprien_Mouton-CDOF6.git
   cd game_of_life-Cyprien_Mouton-CDOF6
   ```

2. Install the package:
   ```bash
   python setup.py install
   ```

## Usage

To run the simulation, execute the following command:
```bash
python game_of_life.py
```

The initial grid is hardcoded in the script. You can modify the `grid` variable in the `if __name__ == "__main__":` section to use a different initial configuration.

### Example Grid
Default configuration:
```
  #  
  #  
### 
```
This configuration represents a "blinker" oscillator, which alternates between vertical and horizontal states.

## Dependencies

This project requires Python 3.6 or later. No additional libraries are required.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements or bug fixes.

## Author

Cyprien Mouton

---

Repository: [Game of Life by Cyprien Mouton](https://github.com/cyprienmouton/game_of_life-Cyprien_Mouton-CDOF6/blob/main/setup.py)

Enjoy exploring the fascinating patterns of Conway's Game of Life!



