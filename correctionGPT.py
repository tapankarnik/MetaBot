import os
import openai


def replaceLine(bigprompt, replacement):
    file = open(bigprompt,'r+')
    lines = file.readlines()
    lines[-1] = replacement
    f = open(bigprompt, 'w')
    f.writelines(lines)


def makeCorrections(bigprompt,currentInput):

  openai.api_key = os.environ["OPENAI_API_KEY"]

  start_sequence = "\nOutput:"
  restart_sequence = "\n\nInput:"
  boiler = "intent identifier\n\nInput: Nope, this isn't good. you should say Hi I'm not the one you want instead\nOutput: Hi I'm not the one you want\n\nInput: that's a mistake, its not you need this, its i love it\nOutput:  I love it\n\nInput: I think it would be better if you had responder I want to be free\nOutput:  I want to be free\n\nInput: nah, change it to i hate you.\nOutput: I hate you\n\nInput: say you are stupid instead.\nOutput: you are stupid\n\nInput: "
  currentInput = currentInput[9:]#'change this to i was born in america'
  prompt = boiler + currentInput + start_sequence

  response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    temperature=0.3,
    max_tokens=60,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\n"]
  )

  replacement = "Output:" + response["choices"][0]["text"]
  replaceLine(bigprompt, replacement)

if __name__ == "__main__":
  bigprompt = 'bigprompt.txt'
  currentInput = "analysis change this to i was born in america"
  makeCorrections(bigprompt,currentInput)

