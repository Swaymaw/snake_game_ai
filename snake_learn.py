import gym
from stable_baselines3 import PPO
import os
import time
from snake_env import SnakeEnv

models_dir = 'models/PPO'
logsdir = f'logs/PPO'

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logsdir):
    os.makedirs(logsdir)

env = SnakeEnv()
env.reset()

model = PPO.load('models/PPO/460000.zip', env, verbose=1, tensorboard_log=logsdir)

TIMESTEPS = 10000
for i in range(1, 101):
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name="PPO")
    model.save(f'{models_dir}/{TIMESTEPS*i}')

env.close()
