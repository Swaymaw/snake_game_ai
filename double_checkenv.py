from snake_env import SnakeEnv

env = SnakeEnv()
episodes = 20

for episodes in range(episodes):
    done = False
    obs = env.reset()
    while not done:
        random_action = env.action_space.sample()
        print('action', random_action)
        obs, reward, done, info = env.step(random_action)
        print('reward', reward)
