from flask import Flask, render_template
from flask_ask import Ask, statement, question
import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://www.bestbuy.com/site/clp/sale-page/pcmcat185700050011.c?id=pcmcat185700050011').read()
soup = bs.BeautifulSoup(source,'lxml')

for deal in soup.find_all('a',attrs={'class':'offer-link'}):
    print (deal.text)
