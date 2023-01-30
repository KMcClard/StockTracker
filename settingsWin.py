import window as w
import tkinter as tk
import customtkinter

def createSettings():
    settings = customtkinter.CTk()

    settings.geometry('300x100')
    settings.wm_overrideredirect(False)
    settings.attributes('-topmost', True)
    settings.attributes('-alpha', 0.8)
    settings.resizable(False,False)
    settings.title("Settings")