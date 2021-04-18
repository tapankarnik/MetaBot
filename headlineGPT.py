import os
import openai

def createHeadline(currentInput):
    openai.api_key = os.environ["OPENAI_API_KEY"]
    start_sequence = "\nOutput:"
    restart_sequence = "\n\nInput: "
    boiler = "Headline generator\n\nInput: I want to make a fact checking chatbot that is funny. I think should be sarcastic as well.\nOutput: The following is a conversation between a Human and AI. The AI is a fact checking chatbot and is funny, sarcastic.\n\nInput: I want to make a Senko San chatbot which is meant for friendly conversations.  She is a very cute and helpful fox girl. She is Japanese by the way\nOutput: The following is a conversation between a Human and Senko San. Senko San is a chatbot for friendly conversations and is very cute, helpful, japanese fox girl.\n\nInput: Lets make a daffy duck chatbot, basically that chatbot talks like daffy duck.\nOutput:  The following is a conversation between a Human and daffy duck. daffy duck chatbot talks like daffy duck.\n\nInput: I want a lisa manobahn chatbot. she is a kpop star in the group blackpink, shes funny, clumsy and cute.\nOutput: The following is a conversation between a Human and Lisa Manobahn. Lisa Manobahn is a kpop star in the group blackpink, she is funny, clumsy and cute.\n\nInput: "
    #currentInput  = "Lets do a catgirl chatbot. Azuki is a munchkin anime catgirl chatbot, she is bashful and sometimes mean but she really cares about you and is cute."
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

    headline = response["choices"][0]["text"][1:]
    return headline

if __name__ == '__main__':
    createHeadline("make an ai chatbot")
