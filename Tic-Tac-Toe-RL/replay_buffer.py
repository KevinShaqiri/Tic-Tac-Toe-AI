from collections import deque
import random

class ReplayBuffer:
    def __init__(self,max_size):
        self.buffer=deque(maxlen=max_size)
    def add(self,experience):
        #adding a new 'memory' (state,action,reward,next_state,done)
        self.buffer.append(experience)  

    def sample(self,batch_size):
        return random.sample(self.buffer,batch_size)
    def size(self):

        return len(self.buffer)    
        