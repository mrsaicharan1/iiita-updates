from flask import Flask, render_template
from flask_ask import Ask, statement, question
import bs4 as bs
from urllib.request

app = Flask(__name__)
ask = Ask(app, '/')
source = urllib.request.urlopen('https://www.bestbuy.com/site/clp/sale-page/pcmcat185700050011.c?id=pcmcat185700050011').read()
soup = bs.BeautifulSoup(source,'lxml')

@ask.launch
def launched():
    return question('Welcome to BestBuy Deals.')

@ask.intent('InvokeIntent')
def invoke():
    text = render_template('welcome')
    return statement(text).simple_card('welcome', text)

@ask.intent('DealsIntent')
def deals():
    for deal in soup.find_all('h3',attrs={'class':'offer-link'}):
        return statement(deal.text)


if __name__ == '__main__':
    app.run(debug=True)
