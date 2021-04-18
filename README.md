# MetaBot

This project is an approach towards a new way of training chatbots. The user is given a way to interact with and also give feedback to the chatbot using plain english. Why dive into a codebase when you could just tell it? We use two GPT-3 instances, one for understanding the user's feedback and generating a prompt, and the other as the chatbot. The first instance is dubbed the Director and the latter one the Actor. The user starts off by describing to the Director who he wants to talk to and describes the person. The Director distills this information and bootstraps the Actor according to the described characteristics. The user may chat with the Actor, and upon seeing an undesirable response, provide feedback to the Director which then corrects the Actor's response. In no time, the Actor learns how to be the perfect chatbot!


## Installation
This project uses OpenAI's GPT3 to power the responses.

Use pipenv to handle python dependencies. Do the following to set up the environment.

```
    pipenv shell
    pipenv install
```

 Then edit the .env file and add your OpenAI key

 Do 

 ```
 flask run
 ```
 
 to enjoy the MetaBot!
