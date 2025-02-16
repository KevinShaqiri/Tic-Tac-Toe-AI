import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset,DataLoader
import torch.optim as optim
from sklearn.model_selection import train_test_split

class TicTacToeNN(nn.Module):
    def __init__(self):
        super(TicTacToeNN,self).__init__()
        self.input=nn.Linear(9,128)
        self.hidden1=nn.Linear(128,64)
        self.hidden2=nn.Linear(64,32)
        self.output=nn.Linear(32,1)
    def forward(self,x):
        x=torch.relu(self.input(x))
        x=torch.relu(self.hidden1(x))
        x=torch.relu(self.hidden2(x))  
        x=torch.tanh(self.output(x))
        return x  

if __name__ == "__main__":
 df=pd.read_csv('dataset.csv')

 X=df.iloc[:,:-1].values #The board,so all columns except last
 Y=df.iloc[:,-1].values #Only minimax so the last column

 #We normalize minimax scores for the neural network

 X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=1)   
 X_train_tensor=torch.tensor(X_train,dtype=torch.float32).to('cuda')
 Y_train_tensor=torch.tensor(Y_train,dtype=torch.float32).to('cuda')

 train_dataset=TensorDataset(X_train_tensor,Y_train_tensor)
 train_loader=DataLoader(train_dataset,batch_size=32,shuffle=True)


 myNet=TicTacToeNN().to('cuda')

 #TRAINING
 criterion=nn.MSELoss()
 optimizer=optim.Adam(myNet.parameters(),lr=0.0001)
 for epoch in range(300):

   total_loss=0

   for X_batch,Y_batch in train_loader:

    optimizer.zero_grad()
    outputs=myNet(X_batch)
    loss=criterion(outputs.squeeze(),Y_batch)
    loss.backward()
    optimizer.step()
    total_loss+=loss.item()
   if epoch%50==0:
        print(f'Epoch {epoch} Avg.Loss:{total_loss/len(train_loader):.4f}')

 #TESTING
 X_test_tensor=torch.tensor(X_test,dtype=torch.float32).to('cuda')
 Y_test_tensor=torch.tensor(Y_test,dtype=torch.float32).to('cuda')
 myNet.eval()
 with torch.no_grad():
    test_predictions=myNet(X_test_tensor)
    test_loss=criterion(test_predictions.squeeze(),Y_test_tensor)
 print(f'Test loss: {test_loss.item():.4f}')    

 torch.save(myNet.state_dict(),'tic_tac_toe_model.pth') #Saving only model weights
