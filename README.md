# 🎯 MasterMind

A Python implementation of the classic **MasterMind** board game, playable in the terminal.

## 🎮 How to Play

Guess the secret combination of 4 colors in 12 attempts or fewer.

After each guess, you receive a score:
- ⚫ — correct color, correct position
- ⚪ — correct color, wrong position

You win when you get ⚫⚫⚫⚫.

### Available Colors

| Letter | Color |
|--------|-------|
| R | 🔴 Red |
| O | 🟠 Orange |
| G | 🟢 Green |
| Y | 🟡 Yellow |
| B | 🔵 Blue |
| P | 🟣 Purple |

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### Run the game

```bash
python mastermind.py
```

## 🗂️ Project Structure

```
mastermind.py
│
└── class MasterMind
    ├── solution_generator()   # Generates a random secret combination
    ├── player_colors()        # Handles player input and validation
    ├── compare_color()        # Compares guess to solution and returns score
    ├── main_display()         # Displays rules and game presentation
    ├── round_display()        # Displays the history of guesses and scores
    └── play()                 # Main game loop
```

## 🧠 What I Learned

- Object-oriented programming with Python classes
- Input validation and recursive error handling
- Two-pass color comparison algorithm to handle duplicates correctly
