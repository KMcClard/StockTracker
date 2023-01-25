import tkinter as tk

root = tk.Tk()

root.geometry('200x200')
root.wm_overrideredirect(True)
label = tk.Label(root, bd = 0, bg = 'black')

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