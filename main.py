import stockInfo as si
import window as w
import threading
import requests

#hold onto file so that it may be used later

site = ""
setCheck = ""
with open('userInfo.txt', 'r') as f:
    strs = f.read().splitlines()
    site = strs[0]
    setCheck = strs[1]

setCheck = 1
with open('userInfo.txt', 'w') as f:
    f.write(site)
    f.write(setCheck)        
