from stable_baselines3.common.env_checker import check_env
from snake_env import SnakeEnv

env = SnakeEnv()

check_env(env)
