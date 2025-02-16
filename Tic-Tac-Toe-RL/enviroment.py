from termcolor import colored
#X is 1,O is -1,0 is empty
#player is 1 or -1(X or O)
class TicTacToeEnv:
    def __init__(self):
         self.board=[0]*9
    def reset(self):
         self.board=[0]*9
         return self.board
    
    def step(self,action,player):
       if self.board[action]!=0:
          raise ValueError('Invalid Move!')
       self.board[action]=player      
       winner=self.check_winner()
       if winner==player:
          reward=1
          done=True
       elif winner==-player:
          reward=-1   
          done=True
       elif 0 not in self.board:
          reward=0
          done=True
       else:
          reward=0 #Game still going
          done=False   
       return self.board,reward,done 


    def get_available_actions(self):
         empty_spots=[]
         for i in range(len(self.board)):
             if self.board[i]==0:
              empty_spots.append(i)
         return empty_spots
    
    
    
    def check_winner(self): #Returns 1 if X wins, -1 if O wins, 0 if draw, None if game is ongoing.
      winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    
      for a,b,c in winning_combinations:
       if self.board[a]==self.board[b]==self.board[c] and self.board[a]!=0:
        return self.board[a] #Returns 1 if X won,-1 if O won
      if 0 not in self.board: #Draw
        return 0  
      return None #Game is still ongoing
    
    def display_board(self):
     for i in range(9):
        if self.board[i]==1:
            print(colored('X','red'),end='')
        elif self.board[i]==-1:
            print(colored('O','blue'),end='')
        elif self.board[i]==0:
            print(f"{colored(f'{i+1}','yellow')}", end='')   
        if i==2 or i==5 or i==8:
            print('\n',end='')
            if i!=8:
             print(colored('_|_|_','white'))
            continue
        print(colored('|','white'),end='')  
     return
    
   