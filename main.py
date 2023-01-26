import stockInfo as si
import window as w
import threading
import requests

#hold onto file so that it may be used later
w.createWindow()

def keepUpdating():
    threading.Timer(1, keepUpdating).start()
    w.updateInfo()
keepUpdating()