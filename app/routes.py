from flask import render_template, redirect, Response
from app import app
from app.forms import SubmitQueryForm
import master

def ask_bot(query):
    response = 'Bot says something back'
    return response
@app.route("/download")
def getPrompts():
    # with open("outputs/Adjacency.csv") as fp:
    #     csv = fp.read()
    f = open("bigprompt.txt", 'r')
    contents = f.read()
    f.close()
    return Response(
        contents,
        mimetype="text/plain",
        headers={"Content-disposition":
                 "attachment; filename=bigprompt.txt"})

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():

    form = SubmitQueryForm()
    response='Hi! What kind of Chatbot do you want?'
    if form.validate_on_submit():
        response = form.user_input.data
        master.main('bigprompt.txt', response) 
        f = open('bigprompt.txt', 'r')
        contents = f.read()
        f.close()
        form.user_input.data = ""
        return render_template('index.html', data=contents, form=form)   
    #prompt = "The following is a bot that is helpful and friendly.\n\n"
    #response = ask_bot(prompt)


    return render_template('index.html', data=response, form=form)
