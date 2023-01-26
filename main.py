import tkinter as tk
import stockInfo as si
import customtkinter

root = customtkinter.CTk()

root.geometry('300x100')
root.wm_overrideredirect(False)
root.attributes('-topmost', True)
root.resizable(False,False)
label = tk.Label(root, text = "bleh").place(x=10, y= 10)
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

root.mainloop()