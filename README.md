# Tic-Tac-Toe AI: Minimax vs Reinforcement Learning

## Overview

This project explores two different AI approaches to playing Tic-Tac-Toe:

1. **Supervised Learning using Minimax**: A neural network trained on Minimax-generated data.
2. **Reinforcement Learning (Deep Q-Network - DQN)**: An AI that learns to play through self-play and Q-learning.

## Comparison

- The **Minimax-based AI** tries to mimic optimal play, since it's trained on Minimax, which exhaustively searches the best move.
- The **Reinforcement Learning AI** starts off weak and improves over time, but needs extensive training to match Minimax.
- Results: Minimax-trained AI performs better out of the box, while RL AI struggles to reach the same level of play.

## Project Structure

```
Tic-Tac-Toe-AI/
│── Tic-Tac-Toe-Minimax/    # Supervised Learning (Minimax)
│   ├── dataset.csv         # Training data generated using Minimax
│   ├── generate_dataset.py # Generates Minimax training data
│   ├── terminalGame.py     # Play against the AI in the terminal
│   ├── tic_tac_toe_model.pth # Trained neural network
│   ├── train_nn.py         # Trains the NN on Minimax data
│   ├── visualGame.py       # GUI version of the game
│
│── Tic-Tac-Toe-RL/         # Deep Q-Network (DQN)
│   ├── enviroment.py       # Tic-Tac-Toe game environment
│   ├── play.py             # Play the game (terminal version)
│   ├── replay_buffer.py    # Experience replay memory
│   ├── rl_agent.py         # Deep Q-learning agent
│   ├── tic_tac_toe_rl_model.pth # Trained RL model
│   ├── train_rl.py         # Trains the RL agent
│   ├── visualGame.py       # GUI version of the game
│
│── README.md                # Project documentation
```

## How to Run

###  Minimax Supervised AI

```sh
# Generate dataset (optional as a generated dataset is already included)
python Tic-Tac-Toe-Minimax/generate_dataset.py

# Train the neural network (optional as a trained network is already included )
python Tic-Tac-Toe-Minimax/train_nn.py

# Play against the AI in terminal
python Tic-Tac-Toe-Minimax/terminalGame.py

# Play the GUI version
python Tic-Tac-Toe-Minimax/visualGame.py
```

### 2 Reinforcement Learning AI

```sh
# Train the RL agent (this may take time)
python Tic-Tac-Toe-RL/train_rl.py

# Play against the RL AI in terminal
python Tic-Tac-Toe-RL/play.py

# Play the GUI version
python Tic-Tac-Toe-RL/visualGame.py
```

## Future Improvements

- Train RL AI for more episodes (e.g., 100,000+)
- Implement a web-based UI instead of Tkinter
- Play around with the model parameters more , possibly also using a greater dataset for the Minimax AI



###




