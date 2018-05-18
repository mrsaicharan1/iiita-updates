import bs4 as bs
import urllib.request
import time

from flask import Flask, render_template
from flask_ask import Ask, statement, question
import requests

app = Flask(__name__)
ask = Ask(app, "/")



def GetEvents():
    source = urllib.request.urlopen('https://www.iiita.ac.in').read()
    soup = bs.BeautifulSoup(source,'lxml')
    events = []
    for event in soup.find_all('h5'):
        events.append(event.text)
    return events



@ask.launch
def launched():
    welcome_msg = "Welcome to Indian Institute of Information Technology's Headlines. Are you interested in the latest updates?"
    return question(welcome_msg)

@ask.intent('YesIntent')
def Shareevents():
    events = GetEvents()
    events_msg = "Here are the latest updates : {},{},{},{} and {}".format(events[0],events[1],events[2],events[3],events[4])
    return statement(events_msg)

@ask.intent('NoIntent')
def NoIntent():
    exit_text = 'Okay then! Bye!'
    return statement(exit_text)

@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Goodbye")


@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Goodbye")

@ask.intent('AMAZON.HelpIntent')
def help():
    return question("Welcome to the triple i. t. skill. This skill is used to get insights about triple i. t. Allahabad's latest happenings.You can activate this skill by saying start triple i. t.Do you want to listen to the latest updates of triple i. t. ?")

@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    app.run(debug=True)
