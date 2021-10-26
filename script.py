import bs4
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def getTSLA():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
    r = requests.get('https://finance.yahoo.com/quote/TSLA',headers=headers)
    soup = bs4.BeautifulSoup(r.text,"html.parser")
    price=soup.find(class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text
    return price


for i in range(10):
    y = getTSLA()
    plt.scatter(i, y)
    plt.pause(0.05)

plt.show()
