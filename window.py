import tkinter as tk
import stockInfo as si
# https://medium.com/@fareedkhandev/modern-gui-using-tkinter-12da0b983e22
import customtkinter
import threading
import requests
from bs4 import BeautifulSoup
import settingsWin as sW

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
    # ANSEWER: Because you did not make a new soup or something for the function called
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
        label = tk.Label(root, text = percent, font="Georgia 12", bg= '#252525', fg= '#06d13c').place(x=400,y=47)
        print("Updated")
        print(price)
        print(newCng)
        print(percent)
        root.after(1000, updateInfo2)
    updateInfo2()

    site = ""
    setCheck = ""
    with open('userInfo.txt', 'r') as f:
        strs = f.read().splitlines()
        site = strs[0]
        setCheck = strs[1]    

    setCheck = int(setCheck)
    print("setcheck: " + str(setCheck))
    def settingsPressed():
        site = ""
        setCheck = ""
        with open('userInfo.txt', 'r') as f:
            strs = f.read().splitlines()
            site = strs[0]
            setCheck = strs[1]
            setCheck = int(setCheck)

        if(setCheck == 0):
            setCheck = 0
            with open('userInfo.txt', 'w') as f:
                f.write(site + '\n')
                f.write(str(setCheck))

            site_var = tk.StringVar()
            top = customtkinter.CTkToplevel(root)
            top.geometry('300x100')
            top.wm_overrideredirect(False)
            top.attributes('-topmost', True)
            top.attributes('-alpha', 0.8)
            top.resizable(False,False)
            top.title("Settings")
            entry = customtkinter.CTkEntry(master=top, textvariable = site_var, placeholder_text = "Enter stock URL:").pack(anchor='nw')            

            def saveSettings():
                setCheck = 0
                site = site_var.get()
                with open('userInfo.txt', 'w') as f:
                    f.write(site + '\n')
                    f.write(str(setCheck))
                top.destroy()

            saveBt = customtkinter.CTkButton(master=top, text = "save", height= 24, width=24, fg_color = 'gray', command=saveSettings).place(relx=0.5, rely=0.5, anchor=tk.CENTER)



        

    button = customtkinter.CTkButton(master=root, text = "settings", height= 32, width=40, fg_color = 'gray', command=settingsPressed).place(x=240, y=60)


    root.mainloop()

createWindow()

# Okay so you have it where it can pull the right data but now you just need to integrate everything across
# all the different data fields. 
# and make it such that grids are coolio