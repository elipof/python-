from tkinter import *
import random
from tkinter.ttk import Combobox

win=Tk()
win.title('random')
win.geometry('800x500')

def show(e):
    fruits=['Apple','Peach','Orange','coconout']
    color=['yellow','green','gray','black']
    print(combo.get())
    if (combo.get())=='color':
        print(random.choice(color))
    elif (combo.get())=='fruits':
        print(random.choice(fruits))

mylist=['color','fruits']
combo=Combobox(win, values=mylist)
combo.pack()
combo.set('select one catagory')

combo.bind('<<ComboboxSelected>>',show)
win.mainloop()
