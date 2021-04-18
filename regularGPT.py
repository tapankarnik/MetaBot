import openai
import os
def regularResponse(currentInput):
    openai.api_key = os.environ["OPENAI_API_KEY"]
    start_sequence = "\nOutput:"
    restart_sequence = "\n\nInput: "

    file = open('bigprompt.txt','r')
    boiler =  file.read()

    prompt = boiler + restart_sequence + currentInput + start_sequence

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
    answer = str(response["choices"][0]["text"])
    #print(response)

    f = open('bigprompt.txt',"w")
    f.write(prompt)
    f.write(answer)

if __name__ == '__main__':
    regularResponse("How are you?")
