import bs4 as bs
import urllib.request
import time

from flask import Flask, render_template
from flask_ask import Ask, statement, question
import requests

app = Flask(__name__)
ask = Ask(app, "/")
source = urllib.request.urlopen('https://www.bestbuy.com/site/clp/sale-page/pcmcat185700050011.c?id=pcmcat185700050011').read()
soup = bs.BeautifulSoup(source,'lxml')

def GetDeals():
    time.sleep(1)
    deals = []
    for deal in soup.find_all('h3',attrs={"class":"offer-link"}):
        deals.append(deal)
    return deals


@ask.launch
def launched():
    welcome_msg = "Welcome to BestBuy Deals. Are you interested in today's deals?"
    return question(welcome_msg)

@ask.intent('YesIntent')
def ShareDeals():
    deals = GetDeals()
    deals_msg = "The top deals for today are {}".format(deals)
    return statement(deals_msg)

@ask.intent('NoIntent')
def NoIntent():
    exit_text = 'Okay then! Bye!'
    return statement(exit_text)

if __name__ == '__main__':
    app.run(debug=True)
