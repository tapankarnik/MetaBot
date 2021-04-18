# MetaBot

This project is an approach towards a new way of training chatbots. The user is given a way to interact with and also give feedback to the chatbot using plain english. Why dive into a codebase when you could just tell it? We use two GPT-3 instances, one for understanding the user's feedback and generating a prompt, and the other as the chatbot. 


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
