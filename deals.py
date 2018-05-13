from flask import Flask, render_template
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('HelloIntent')
def hello(firstname):
    text = render_template('hello', firstname=firstname)
    return statement(text).simple_card('Hello', text)

@ask.intent('InvokeIntent')
def invoke():
    

if __name__ == '__main__':
    app.run(debug=True)
