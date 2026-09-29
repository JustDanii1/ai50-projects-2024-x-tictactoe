# Tic-Tac-Toe

A solution to **Project 0 — Tic-Tac-Toe** from Harvard's **CS50's Introduction to Artificial Intelligence with Python**.

## About

This project implements an AI that plays Tic-Tac-Toe using the **Minimax algorithm**.

The AI analyzes possible game states and chooses an optimal move based on the current board. The project focuses on game-playing AI, search algorithms, and decision making.

## How It Works

The program represents the Tic-Tac-Toe board as a 3×3 grid.

The AI uses **Minimax** to:

* Determine whose turn it is
* Find all possible moves
* Generate resulting board states
* Detect the winner
* Determine whether the game is over
* Evaluate terminal game states
* Select an optimal move

The implemented functions include:

```text
player()
actions()
result()
winner()
terminal()
utility()
minimax()
```

The official project specification requires these functions to handle the game logic and optimal move selection.

## Minimax

Minimax is a recursive search algorithm used for decision-making in two-player games.

The algorithm considers possible future moves and assigns a utility value to terminal game states:

```text
X wins  →  1
Tie     →  0
O wins  → -1
```

The AI then chooses the move that leads to the best possible outcome for the player whose turn it is.

## Technologies

* Python
* Minimax
* Game Tree Search
* Artificial Intelligence
* Recursive Algorithms

## Running the Project

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python runner.py
```

This launches the graphical Tic-Tac-Toe game and allows you to play against the AI.

## Project Structure

```text
ai50-projects-2024-x-tictactoe/
├── tictactoe.py
└── README.md
```

`tictactoe.py` contains the game logic and AI implementation. The graphical interface is provided by the original CS50 project distribution.

## What I Learned

* How the Minimax algorithm works
* How to represent a game as a state space
* How recursive search can be used for AI
* How to evaluate game states
* How to find optimal moves
* How game-playing AI makes decisions

## Course

**CS50's Introduction to Artificial Intelligence with Python**

**Project 0 — Tic-Tac-Toe**

Course: https://cs50.harvard.edu/ai/

Project: https://cs50.harvard.edu/ai/projects/0/tictactoe/
