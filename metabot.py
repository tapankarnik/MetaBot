import openai
import os

#openai.api_key = os.environ['OPENAI_API_KEY']
f = open("bigprompt.txt", "r+")
f.truncate(0)
f.close()

from app import app
