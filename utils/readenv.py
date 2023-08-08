
from decouple import Config, RepositoryEnv


def getEnvValue(key):
    
    DOTENV_FILE = '.env'
    env_config = Config(RepositoryEnv(DOTENV_FILE))

    return env_config.get(key)
