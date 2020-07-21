import numpy as np

class Bandit:
    actions = []
    rewards = []
    estimated_reward = []
    total_steps = 0
    step = 0
    
    def initialization(self):
        self.actions = ['left', 'right', 'up', 'down']
        self.rewards = np.random.randint(1, size=4)
        self.estimated_rewards = np.random.randint(1, size=4)
        self.total_steps = 20
        self.selection = np.random.randint(1, size=4)
    
    def working(self):
        
        for i in range(self.total_steps):
            self.rewards = np.random.randint(50, size=4)
            if i % 4 != 0:
                val = max(self.estimated_rewards)
                index = self.estimated_rewards.tolist().index(val)
                Action = self.actions[index]
            else:
                rand = (np.random.randint(4, size=1))
                Action = self.actions[rand[0]]
            
            Reward = self.rewards[self.actions.index(Action)]
            # print(self.rewards)
            # print(self.estimated_rewards)
            self.selection[self.actions.index(Action)] = self.selection[self.actions.index(Action)] + 1
            
            alpha = 1 / self.selection[self.actions.index(Action)]
            self.estimated_rewards[self.actions.index(Action)] = self.estimated_rewards[self.actions.index(Action)] + alpha * (Reward - self.estimated_rewards[self.actions.index(Action)])
        print(self.selection)
        return self.estimated_rewards


if __name__ == "__main__":

    b = Bandit()
    b.initialization()
    c = b.working()
    print(c)