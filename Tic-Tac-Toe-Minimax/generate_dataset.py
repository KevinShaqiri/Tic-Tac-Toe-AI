import random
import numpy as np
import pandas as pd

 

def check_winner(board): #Returns 1 if X wins, -1 if O wins, 0 if draw, None if game is ongoing.
      winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    
      for a,b,c in winning_combinations:
       if board[a]==board[b]==board[c] and board[a]!=0:
        return board[a] #Returns 1 if X won,-1 if O won
      if 0 not in board: #Draw
        return 0  
      return None #Game is still ongoing    

#Create a 1D list that represents the 3x3 board
#1 means X,-1 is O,0 is empty
if __name__ == "__main__":
 def create_empty_board():
  return [0]*9
  #Value at index i represents position i on the board,left to right



  
 #The AI wants to minimize,the player wants to maximize
 #The best possible move for the AI(O (-1)):
 def minimax(board, is_maximizing): #If is_maximizing is True,then its the players turn,if false then its the AI's turn
 #Returns a tuple (score,move)
 #For terminal states,move will be None
  winner=check_winner(board)
  if winner is not None: #If the game is over,return a score
   return winner,None #1 if X won,-1 if O wins,0 if draw
 
  if is_maximizing:   #X turn(human,maximizing)
   best_score=float('-inf') #X starts with lowest possible score
   best_move=None
   for i in range(9):
     if board[i]==0:
       board[i]=1
       score,_=minimax(board,False) #Now its O's turn
       board[i]=0 #Undoing the move so it  doesnt affect other calculations
       if score>best_score:
         best_score=score
         best_move=i
   return best_score,best_move
  else:  #O turn(AI,minimizing)
   best_score=float('inf') #O starts with the highest possible value
   best_move=None
   for i in range(9):
     if board[i]==0:
       board[i]=-1
       score,_=minimax(board,True) #Now its X's turn
       board[i]=0 #Unduing the move so it doesnt affect other calculations
       if score<best_score:
         best_score=score
         best_move=i
   return best_score,best_move      


 def simulate_game(num_moves):
  
     """
     Simulates a Tic-Tac-Toe game with proper move order.
     X always starts, and moves alternate.
     Returns the board state after num_moves.
    
     To make sure it's O's turn (our AI's turn), choose num_moves to be odd.
     For example: 1, 3, 5..
     """
     board=create_empty_board()
     current_player=1 #X starts
     for i in range(num_moves):
       empty_positions=[]
       for j in range(9):
         if board[j]==0:
           empty_positions.append(j)
       if len(empty_positions)==0:
           break
       move=random.choice(empty_positions)
       board[move]=current_player
       #Switch plater
       current_player=-current_player
     return board



 def generate_dataset(num_samples,filename='dataset.csv'):
   #Only states where its the AI's turn are used

   data=[]
   possible_moves=[1,3,5,7,9] #Odd numbers such that its the AI's turn
   for sample_index in range(num_samples):
     num_moves=random.choice(possible_moves)
     board=simulate_game(num_moves)
     #For this generated board,we compute the minimax evaluation assuming its O's turn which it is since num_moves is odd
     minimax_score,_=minimax(board,is_maximizing=False)

     row=[]
     for i in range(9):
       row.append(board[i])
     row.append(minimax_score)
     data.append(row)
   columns=[]
   for i in range(9):
     columns.append(f'Cell_{i}')
   columns.append('minimax_score') 
   df=pd.DataFrame(data,columns=columns)
   df.to_csv(filename,index=False)
   print(f"✅ Dataset saved as {filename} with {num_samples} samples.")
 if __name__ == "__main__":  
  num_samples = 10000  # Increase this for more data
  generate_dataset(num_samples)
       









