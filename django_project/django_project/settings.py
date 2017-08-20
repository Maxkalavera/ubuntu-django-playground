
from os.path import abspath, dirname, normpath, join

from dotenv import load_dotenv


ENV_PATH = normpath(
    join(dirname(dirname(dirname(abspath(__file__)))), 'conf/.env'))
print(ENV_PATH)
load_dotenv(ENV_PATH)
