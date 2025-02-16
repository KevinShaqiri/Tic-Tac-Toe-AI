import torch
import torch.nn as nn
import torch.optim as optim
import random
import numpy as np
from replay_buffer import ReplayBuffer
class DQN(nn.Module):
    def __init__(self):
        super(DQN,self).__init__()
        self.input=nn.Linear(9,256)
        self.hidden1=nn.Linear(256,128)
        self.hidden2=nn.Linear(128,64)
        self.hidden3=nn.Linear(64,32)
        self.output=nn.Linear(32,9)

    def forward(self,x):
        x=torch.relu(self.input(x))
        x=torch.relu(self.hidden1(x))
        x=torch.relu(self.hidden2(x))
        x=torch.relu(self.hidden3(x))
        x=self.output(x)
        return x





class DQNAgent:
    
    def __init__(self,epsilon=0.1):
        self.model=DQN().to('cuda')
        self.epsilon=epsilon
        self.buffer=ReplayBuffer(max_size=10000)

    def select_action(self,state,available_actions):

        if random.random()<self.epsilon:
            return random.choice(available_actions)
        state_tensor=torch.tensor(state,dtype=torch.float32).unsqueeze(0).to('cuda')

        with torch.no_grad():
            q_values=self.model(state_tensor)

        q_values=q_values.cpu().numpy().flatten()
        best_action=max(available_actions,key=lambda a:q_values[a])
        
        return best_action   
         
    def store_experience(self,state,action,reward,next_state,done):
        self.buffer.add((state,action,reward,next_state,done))


    def train(self,batch_size,gamma,optimizer,criterion):
        if self.buffer.size()<batch_size:
            return 0.0
        batch=self.buffer.sample(batch_size)
        states,actions,rewards,next_states,dones=zip(*batch)

        states=torch.tensor(states,dtype=torch.float32).to('cuda')
        actions=torch.tensor(actions,dtype=torch.int64).to('cuda')
        rewards=torch.tensor(rewards,dtype=torch.float32).to('cuda')
        next_states=torch.tensor(next_states,dtype=torch.float32).to('cuda')
        dones=torch.tensor(dones,dtype=torch.float32).to('cuda')
       #Current state Q values
        q_values=self.model(states)
        q_values=q_values.gather(1,actions.unsqueeze(1)).squeeze(1)
          #Compute target Q values for next states
        with torch.no_grad():
            next_q_values=self.model(next_states).max(1)[0]
            target_q_values=rewards+gamma*next_q_values*(1-dones)
        loss=criterion(q_values,target_q_values)
        optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=1.0)
        optimizer.step()
        return loss.item()
