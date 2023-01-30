import tkinter as tk
import stockInfo as si
# https://medium.com/@fareedkhandev/modern-gui-using-tkinter-12da0b983e22
import customtkinter
import threading
import requests
from bs4 import BeautifulSoup

def createWindow():
    root = customtkinter.CTk()

    root.geometry('300x100')
    root.wm_overrideredirect(False)
    root.attributes('-topmost', True)
    root.attributes('-alpha', 0.8)
    root.resizable(False,False)
    #label = tk.Label(root, text = si.pullPrice(), font="Bahnschrift 80", bg= '#252525', fg= '#06d13c').place(x=10, y= 10)
    label = tk.Label(root, text = si.pullTicker(), font="Georgia 30 bold", bg = '#252525', fg = '#06d13c').pack(anchor='ne')

    root.title(si.pullTicker())

    customtkinter.set_appearance_mode("dark")

    def SaveLastClickPos(event):
        global lastClickX, lastClickY
        lastClickX = event.x
        lastClickY = event.y

    def Dragging(event):
        x,y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
        root.geometry("+%s+%s" % (x, y))

    root.bind('<Button-1>', SaveLastClickPos)
    root.bind('<B1-Motion>', Dragging)

    def updateInfo():
        threading.Timer(1,updateInfo).start()
        price = si.pullPrice()
        print(price)
        fontSize = 80
        #price = 100000.01
        if float(price) <= 99.99:
            fontSize = 100
        elif float(price) <= 999.99:
            fontSize = 90
        elif float(price) <= 9999.99:
            fontSize = 80
        elif float(price) <= 99999.99:
            fontSize = 70
        elif float(price) <= 999999.99:
            fontSize = 60
        else:
            fontSize = 50

        label = tk.Label(root, text = si.pullPrice(), font="Bahnschrift "+str(fontSize), bg= '#252525', fg= '#06d13c').place(anchor='nw')
        label = tk.Label(root, text = "cng", font="Georgia 30", bd=0, bg= '#252525', fg= '#06d13c').place(x=360,y=40)
        print(price)
        print("Updated")
    #updateInfo()

    #I tried piping in information from stockInfo.py and for some reason I woudln't update
    # is that becuase it is from another file or what?
    # why does this one work and the other doesn't
    def updateInfo2():
        page = requests.get('https://www.marketwatch.com/investing/fund/spy')
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.select('bg-quote')[39].text
        cng = soup.select('bg-quote')[40].text
        cng.split()
        newCng = cng[2:6]
        percent = cng[7:14]
        fontSize = 80
        #price = 100000.01
        if float(price) <= 99.99:
            fontSize = 100
        elif float(price) <= 999.99:
            fontSize = 90
        elif float(price) <= 9999.99:
            fontSize = 80
        elif float(price) <= 99999.99:
            fontSize = 70
        elif float(price) <= 999999.99:
            fontSize = 60
        else:
            fontSize = 50

        #you need to learn how to use the grid system for this!!
        # it will make things so much easier rather than having to try and place everything that's gonna get screwed by 
        # font sizing changes
        label = tk.Label(root, text = price, font="Bahnschrift "+str(fontSize), bg= '#252525', fg= '#06d13c').place(anchor='nw')
        label = tk.Label(root, text = newCng, font="Georgia 14", bg= '#252525', fg= '#06d13c').place(x=360,y=45)
        label = tk.Label(root, text = percent, font="Georgia 12", bg= '#252525', fg= '#06d13c').place(x=400,y=45)
        print("Updated")
        print(price)
        print(newCng)
        print(percent)
        root.after(3000, updateInfo2)
    updateInfo2()

    root.mainloop()

createWindow()

#push that stuff cuzzo