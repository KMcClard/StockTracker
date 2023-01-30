import tkinter as tk
import sys
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', 'unix$DISPLAY')


#create main window
master = tk.Tk()
master.title("tester")
master.geometry("300x100")


#make a label for the window
label1 = tk.Label(master, text='Hellooooo')
# Lay out label
label1.pack()

# Run forever!
master.mainloop()