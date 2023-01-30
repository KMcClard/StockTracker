import requests
from bs4 import BeautifulSoup
import threading
import re

# def printit():
#     threading.Timer(1, printit).start()
#     page = requests.get('https://www.marketwatch.com/investing/fund/spy')
#     soup = BeautifulSoup(page.content, 'html.parser')
#     price = soup.select('bg-quote')[39].text
#     print(price)
# printit()

site = "www.google.com"
s = "www.google.com"
with open('userInfo.txt', 'r') as f:
    site = f.read().splitlines()
    site = str(site)
    site = (site[2:-2])

page = requests.get(str(site))
soup = BeautifulSoup(page.content, 'html.parser')


def pullPrice():
    page = requests.get(str(site))
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.select('bg-quote')[39].text
    return price

def pullTicker():
    ticker = soup.select('title')[0].text
    ticker = (ticker[:3])
    return ticker

# THIS WORKS!! the first h2 header holds data for all main price
def pullSpecPrice():
    page = requests.get(str(site))
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.select('h2')[0].text
    price.split()
    newPrice = price[1]+price[3:10]
    print(newPrice)
pullSpecPrice()