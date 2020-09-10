#!/usr/local/bin/python3.8
import tkinter as tk
from tkinter import scrolledtext 
import os
import subprocess

output = """Nothing to display"""

def startcommand():
    ip = entrybox.get()
    p1 = os.popen("adb tcpip 5555 > /dev/null 2>&1")
    p2 = os.popen("adb connect {}".format(ip))
    print(p1.read())
    print(p2.read())

def logcatcommand():
    popen = subprocess.Popen(args="adb logcat", shell=True, stdout=subprocess.PIPE)
    return iter(popen.stdout.readline, b"")


def logcatresult():
    for line in logcatcommand():
        print(line)

def stopcommand():
    p4 = os.popen("adb kill-server")
    print(p4.read())

window = tk.Tk()
window.title("Wireless ADB Tool")
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)


titletext = tk.Label(text="Connect phone to pc wirelessly")
titletext.grid(row=0, column=0)

subtext = tk.Label(text="Enter the ip of your android phone here")
subtext.grid(row=1, column=0)

notetext = tk.Label(text="Make sure adb is in your path\n  and Developer options are enabled on your phone")
notetext.grid(row=2, column=0)

entrybox = tk.Entry(width=20)
entrybox.grid(row=3, column=0)

button1 = tk.Button(text="Connect",width=25, height=3, command=startcommand)
button1.grid(row=4, column=0)

button2 = tk.Button(text="Open logcat",width=25, height=3, command=logcatresult)
button2.grid(row=6, column=0)

button3 = tk.Button(text="Stop",width=25, height=3, command=stopcommand)
button3.grid(row=7, column=0)

# result = scrolledtext.ScrolledText(window, wrap = tk.WORD, width = 40, height = 10, font = ("Times New Roman", 15))
# result.grid(column = 1, row=0)
# result.insert(tk.INSERT, output)
# result.configure(state ='disabled') 

window.mainloop()