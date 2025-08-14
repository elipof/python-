from tkinter import *
win=Tk()
def butfunc():
    a=float(entry.get())
    b=float(entry2.get())
    label3.config(text=a*b)

def butfunc2():
    a=float(entry.get())
    b=float(entry2.get())
    label3.config(text=a+b)

def butfunc3():
    a = float(entry.get())
    b = float(entry2.get())
    label3.config(text=a-b)

def butfunc4():
    a = float(entry.get())
    b = float(entry2.get())
    if b==0:
        label3.config(text="second num can't be  zero")
    else:
        label3.config(text=a/b)

win.title('calculator')
win.geometry('800x500')


label=Label(master=win, text='enter num1')
label.pack()
entry=Entry(master=win)
entry.pack()

label2=Label(master=win, text='enter num2')
label2.pack()
entry2=Entry(master=win)
entry2.pack()

button=Button(master=win, text='*',command=butfunc)
button.pack()
button1=Button(master=win, text='+',command=butfunc2)
button1.pack()
button2=Button(master=win, text='-',command=butfunc3)
button2.pack()
button3=Button(master=win, text='/',command=butfunc4)
button3.pack()

label3=Label(master=win, text='result')
label3.pack()


win.mainloop()
