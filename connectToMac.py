#!/usr/local/bin/python3.8
import tkinter as tk
import os
import textwrap
import webbrowser
import subprocess

global clicked
global ip
clicked = False

def openURL(url):
    webbrowser.open_new(url)

def callback(event):
    global clicked
    if (clicked == False):
        insertIP[0].delete(0, tk.END)
        insertIP[0].config(fg = "black")
        clicked = True

def startcommand():
    global ip
    ip = insertIP[0].get()
    if (ip == "" or ip == "Enter IP"):
        result.configure(text="IP cannot be empty")
    else:
        os.popen("adb tcpip 5555 > /dev/null 2>&1")
        startEvent = os.popen("adb connect {}".format(ip))
        res = '\n'.join(textwrap.wrap(startEvent.read(), 20))
        result.configure(text=res)

def stopcommand():
    os.popen("adb kill-server")
    result.configure(text="Stopped")

def helpPage():
    window2 = tk.Toplevel(window)

    helpTitle=tk.Label(window2,text="Doesn't work?")
    helpTitle.config(font=("Courier", 44))
    helpTitle.grid(row=0, column=0)

    helpNote=tk.Label(window2,text='Make sure adb is in your path\n  and Developer options are enabled on your phone')
    helpNote.grid(row=1, column=0)
    helpNote2=tk.Label(window2,text='For anymore questions look at the readme or file an issue at:')
    helpNote2.grid(row=2, column=0)

    link1 = tk.Label(window2, text="Github", fg="blue", cursor="hand2")
    link1.grid(row=3, column=0)
    link1.bind("<Button-1>", lambda e: openURL("https://github.com/Gorter-dev/ConnectToMac"))

    helpNote3=tk.Label(window2,text='Or')
    helpNote3.grid(row=4, column=0)

    link2 = tk.Label(window2, text="Sourceforge", fg="blue", cursor="hand2")
    link2.grid(row=5, column=0)
    link2.bind("<Button-1>", lambda e: openURL("https://sourceforge.net/projects/connect-phone-mac/"))

window = tk.Tk()
window.title("ConnectToMac")
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 2], minsize=50)
window.rowconfigure([3, 4], minsize=50)
window.rowconfigure([1, 5], minsize=100)

titletext = tk.Label(text="Connect phone to pc wirelessly")
titletext.config(font=("Courier", 15))
titletext.grid(row=0, column=0)

result = tk.Label()
result.config(text="Nothing to display")
result.grid(row=1, column=0)

insertIP = []
insertIP.append(tk.Entry(fg = "gray"))
insertIP[0].bind("<Button-1>", callback)
insertIP[0].insert(0, "Enter IP")
insertIP[0].grid(row=2, column=0)

buttonConnect = tk.Button(text="Connect",width=15, height=2, command=startcommand)
buttonConnect.grid(row=3, column=0)

buttonStop = tk.Button(text="Stop",width=15, height=2, command=stopcommand)
buttonStop.grid(row=4, column=0)

buttonHelp = tk.Button(text="Help",width=15, height=2, command=helpPage)
buttonHelp.grid(row=5, column=0)

window.mainloop()