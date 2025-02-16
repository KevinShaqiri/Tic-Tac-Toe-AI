import torch
import numpy as np
from train_nn import TicTacToeNN
from generate_dataset import check_winner
from termcolor import colored 
model=TicTacToeNN().to('cuda')

model.load_state_dict(torch.load('tic_tac_toe_model.pth',weights_only=False))
model.eval()
def display_board(board):
    for i in range(9):
        if board[i]==1:
            print(colored('X','red'),end='')
        elif board[i]==-1:
            print(colored('O','blue'),end='')
        elif board[i]==0:
            print(f"{colored(f'{i+1}','yellow')}", end='')   
        if i==2 or i==5 or i==8:
            print('\n',end='')
            if i!=8:
             print(colored('_|_|_','white'))
            continue
        print(colored('|','white'),end='')  
    return                


def ai_move(board,model,temperature=0.5):
    possible_moves=[]
    scores=[]
    for i in range(len(board)):
        if board[i]==0:
            boardCopy=board.copy()
            boardCopy[i]=-1
            boardTensor=torch.tensor(boardCopy,dtype=torch.float32)
            boardTensor=boardTensor.unsqueeze(0)
            boardTensor=boardTensor.to('cuda')
            with torch.no_grad():
             predicted_score=model(boardTensor).item()
            possible_moves.append(i)
            scores.append(-predicted_score) #Lower scores preferable
            
            
    exp_scores=np.exp(np.array(scores)/temperature)
    probabilities=exp_scores/np.sum(exp_scores)
    best_move=np.random.choice(possible_moves,p=probabilities)
    return best_move
def play_game():
   board= [0]*9
   human_turn=True
   while check_winner(board) is None:
      result=check_winner(board)
      if result is None:
         if human_turn:
           display_board(board)
           userInput=int(input('Place X in: \n'))
           if board[userInput-1]==0:
              board[userInput-1]=1
              human_turn= not human_turn
           else:
              print('Invalid Move') 
              continue
        
         else:
          AI_Move=ai_move(board,model)
          board[AI_Move]=-1
          human_turn=not human_turn
   result=check_winner(board) 
   display_board(board)     
   if result==1:
      print('You won!')
   elif result==-1:
      print('The AI won!')
   elif result==0:
      print('Draw!') 

if __name__ == "__main__":
       
  play_game()         

         
         
         
       
