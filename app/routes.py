from flask import render_template, redirect
from app import app
from app.forms import SubmitQueryForm

def ask_bot(query):
    response = 'Bot says something back'
    return response

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():

    form = SubmitQueryForm()
    response='Hi Ask me anythin!'
    if form.validate_on_submit():
        response = form.user_input.data
        return render_template('index.html', data=response, form=form)   
    #prompt = "The following is a bot that is helpful and friendly.\n\n"
    #response = ask_bot(prompt)


    return render_template('index.html', data=response, form=form)
