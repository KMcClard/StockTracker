import tkinter as tk
import stockInfo as si
import customtkinter
import threading
import requests

def createWindow():
    root = customtkinter.CTk()

    root.geometry('300x100')
    root.wm_overrideredirect(False)
    root.attributes('-topmost', True)
    root.attributes('-alpha', 1)
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

        label = tk.Label(root, text = price, font="Bahnschrift "+str(fontSize), bg= '#252525', fg= '#06d13c').place(anchor='nw')
        label = tk.Label(root, text = "cng", font="Georgia 30", bd=0, bg= '#252525', fg= '#06d13c').place(x=360,y=40)
        print("Updated")
    updateInfo()

    root.mainloop()

createWindow()