import os

class Config(object):
    SECRET_KEY = os.environ.get('OPENAI_ACCESS_KEY')
