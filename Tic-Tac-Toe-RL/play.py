#Human is X,O is AI

import torch
from rl_agent import DQNAgent
from enviroment import TicTacToeEnv

def play_game():
    env=TicTacToeEnv()
    state=env.reset()

    human_turn=True
    agent=DQNAgent(epsilon=0.0)

    agent.model.load_state_dict(torch.load('tic_tac_toe_rl_model.pth'))
    agent.model.eval()

    
    while True:
        winner=env.check_winner()
        if winner is not None:
            if winner==1:
                env.display_board()
                print('You won!')
            elif winner==-1:
                env.display_board()
                print('The AI won')
            else:
                env.display_board()
                print('Draw')
            break
        if human_turn:
            env.display_board()
            valid_move=False
            while not valid_move:
                try:
                    move=int(input('Enter your move (1-9): \n'))-1 
                    if move not in env.get_available_actions():
                        print('Invalid Move') 
                    else:
                        valid_move=True
                except ValueError:
                    print('Please enter a number between 1 and 9')
            state,reward,done=env.step(move,1)  
        else:
            available=env.get_available_actions()
            move=agent.select_action(state,available)
            state,reward,done=env.step(move,-1)             
        human_turn=not human_turn
if __name__=='__main__':
    play_game()                                  