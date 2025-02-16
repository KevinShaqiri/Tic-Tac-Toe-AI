from terminalGame import ai_move,check_winner, model
import tkinter as tk
from tkinter import messagebox
board_state=[0]*9
buttons=[]
root=tk.Tk()
root.title('Tic-Tac-Toe')
root.geometry('1920x780')
root.configure(bg='khaki4')
board_frame=tk.Frame(root,bg='DarkOliveGreen4')
board_frame.pack(expand=True)

result_label = tk.Label(board_frame, text="", font=("Arial", 24), bg="DarkOliveGreen4", fg="black")
result_label.grid(row=4, column=0, columnspan=3, pady=10)



for row in range(3):
    for col in range(3):
     cell_index=row*3 +col +1
     btn=tk.Button(board_frame,text='',font=('Arial',28),width=5,height=3,command=lambda idx=cell_index:buttonClick(idx-1),bg='DarkOliveGreen3')
     btn.grid(row=row,column=col,padx=5,pady=5)
     buttons.append(btn)


def restart_game():
   global board_state
   board_state=[0]*9
   for btn in buttons:
      btn.config(text='',state='normal',bg='DarkOliveGreen3')
   restartButton.grid_remove() 
   result_label.config(text='') 
restartButton=tk.Button(board_frame,text='Play again',font=('Arial',24),width=8,height=1,bg='lightgreen',command=restart_game)
restartButton.grid(row=3,column=0,columnspan=3,pady=5)
restartButton.grid_remove() 



def buttonClick(index):
   global board_state,buttons
   if board_state[index]==0:
     board_state[index]=1
     buttons[index].config(text='X',state='disabled',fg='red',disabledforeground='red',bg='yellow')
     result=check_winner(board_state)

     if result is not None:
        if result==1:
           result_label.config(text='You won!')
        elif result==-1:
           result_label.config(text='The AI won!')  
        elif result==0:
           result_label.config(text='Draw!')
        restartButton.grid()
       
     root.after(100,ai_turn)
     
def ai_turn():
   if check_winner(board_state) is not None:
      return
   ai_index=ai_move(board_state,model)
   board_state[ai_index]=-1
   buttons[ai_index].config(text='O',state='disabled',fg='blue',disabledforeground='blue',bg='lightblue')

   result=check_winner(board_state)
   if result is not None:
        if result==1:
           result_label.config(text='You won!')
        elif result==-1:
           result_label.config(text='The AI won!')  
        elif result==0:
           result_label.config(text='Draw!')
        restartButton.grid()
root.mainloop()
