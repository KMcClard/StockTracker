import requests
from bs4 import BeautifulSoup
import threading

def printit():
    threading.Timer(1, printit).start()
    page = requests.get('https://www.marketwatch.com/investing/fund/spy')
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.select('bg-quote')[39].text
    print(price)

printit()
