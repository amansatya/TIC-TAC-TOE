# TIC-TAC-TOE 🎮

A simple and interactive Tic-Tac-Toe game built with Python and Tkinter. Play against the computer with a clean graphical user interface!

## 📋 Table of Contents
- [Description](#description)
- [Features](#features)
- [File Structure](#file-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [How to Play](#how-to-play)

## 📝 Description

This is a classic Tic-Tac-Toe game where you can play against the computer. The game features a symbol selection screen where you can choose to play as 'X' or 'O', followed by the main game board with an intuitive GUI built using Python's Tkinter library.

## ✨ Features

- **Symbol Selection**: Choose whether you want to play as 'X' or 'O'
- **Player vs Computer**: Play against a computer opponent with random move selection
- **Interactive GUI**: Clean and user-friendly interface using Tkinter
- **Game State Detection**: Automatic detection of wins, losses, and draws
- **Real-time Updates**: Immediate visual feedback for moves

## 📁 File Structure

```
TIC-TAC-TOE/
├── main.py           # Entry point of the application
├── ui.py             # User interface components and game UI logic
├── game_logic.py     # Core game logic and rules
├── config.py         # Configuration settings and constants
├── utils.py          # Utility functions (board printing)
└── README.md         # Project documentation
```

### 📄 File Details

| File | Purpose | Description |
|------|---------|-------------|
| **main.py** | Entry Point | Initializes and starts the symbol selection UI |
| **ui.py** | User Interface | Contains `SymbolSelectorUI` for symbol selection and `TicTacToeUI` for the main game interface |
| **game_logic.py** | Game Logic | Implements the `GameLogic` class with move validation, winner detection, draw checking, and computer AI |
| **config.py** | Configuration | Stores game constants like board size and player/computer symbols |
| **utils.py** | Utilities | Contains helper functions like `print_board()` for console output |

### 🔧 Key Components

- **SymbolSelectorUI**: Initial screen for choosing X or O
- **TicTacToeUI**: Main game board with 3x3 grid of buttons
- **GameLogic**: Handles game rules, move validation, and win conditions
- **Computer AI**: Random move selection for computer opponent

## 📋 Prerequisites

Before running this game, make sure you have:

- **Python 3.6+** installed on your system
- **Tkinter** (usually comes pre-installed with Python)

To check if you have Python installed:
```bash
python --version
```

To check if Tkinter is available:
```bash
python -c "import tkinter; print('Tkinter is available')"
```

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/amansatya/TIC-TAC-TOE.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd TIC-TAC-TOE
   ```

3. **Verify all files are present**:
   ```bash
   ls -la
   ```
   You should see: `main.py`, `ui.py`, `game_logic.py`, `config.py`, `utils.py`

## 🎯 How to Run

1. **Open terminal/command prompt** in the project directory

2. **Run the game**:
   ```bash
   python main.py
   ```

## 🎮 How to Play

1. **Launch the game** by running `python main.py`

2. **Choose your symbol**: A window will appear asking you to choose between 'X' and 'O'

3. **Make your move**: Click on any empty cell in the 3x3 grid to place your symbol

4. **Computer's turn**: The computer will automatically make its move after yours

5. **Win conditions**: 
   - Get three of your symbols in a row (horizontally, vertically, or diagonally)
   - The game will automatically detect wins, losses, and draws

6. **Game over**: A message will appear announcing the result, and the window will close

## 🎯 Game Rules

- Players take turns placing their symbols (X or O) on a 3x3 grid
- The first player to get three symbols in a row wins
- If all 9 cells are filled without a winner, the game is a draw
- You cannot place a symbol in an already occupied cell

## 🔧 Technical Details

- **Language**: Python 3.6+
- **GUI Framework**: Tkinter
- **Architecture**: Object-oriented design with separate UI and logic layers
- **AI Strategy**: Random move selection for computer opponent

---

**Enjoy playing Tic-Tac-Toe! 🎉**

For any issues or suggestions, please feel free to open an issue on GitHub.