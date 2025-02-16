import torch
import torch.optim as optim
from rl_agent import DQNAgent
from enviroment import TicTacToeEnv
torch.backends.cudnn.benchmark=True
Agent=DQNAgent(epsilon=1.0)
env=TicTacToeEnv()
num_episodes=20000
batch_size=64
gamma=0.97
learning_rate=0.0001
target_update_freq=100

criterion=torch.nn.SmoothL1Loss()
optimizer=optim.Adam(Agent.model.parameters(),lr=learning_rate)

for episode in range(num_episodes):
    state=env.reset() #Start a new game
    done=False
    player=1 #X starts

    while not done:

        available_actions=env.get_available_actions()
             #Select action
        action=Agent.select_action(state,available_actions)
        
        next_state,reward,done=env.step(action,player)

        Agent.store_experience(state,action,reward,next_state,done)
        if not done:
            available_actions=env.get_available_actions()
            opponent_action=Agent.select_action(next_state,available_actions)
            next_state_opp,reward_opp,done_opp=env.step(opponent_action,-player)
            Agent.store_experience(next_state,opponent_action,reward_opp,next_state_opp,done_opp)
            next_state=next_state_opp
            done=done_opp
        player*=-1    
        
        #Train agent
        if Agent.buffer.size()>batch_size:
           loss=Agent.train(batch_size,gamma,optimizer,criterion)
        else:
            loss=None
        if episode > 5000:
         Agent.epsilon = max(0.1, Agent.epsilon * 0.999)
    if episode%2000==0:
            if loss is not None: 
             print(f"Episode {episode}/{num_episodes} - Epsilon: {Agent.epsilon:.3f} - Loss: {loss:.4f}")    
            else:
             print(f"Episode {episode}/{num_episodes} - Epsilon: {Agent.epsilon:.3f} - Loss: N/A")    
print("Training complete!")
torch.save(Agent.model.state_dict(), "tic_tac_toe_rl_model.pth")

