from tkinter import *
import random
win=Tk()
win.title('guess the word')
win.geometry('800x500')
mylist=['red','green','gray','blue']
word=random.choice(mylist)
print(word)
guess=['-']*len(word)
def show():
    label.config(text=' '.join(guess))
def check():
    letter=entry.get().lower()
    entry.delete(0, END)
    if len(letter)!=1:
        label2.config(text='import just one letter')
    elif letter in word:
        for i in range(len(word)):
            if word[i]==letter:
                guess[i]=letter
        show()
        label2.config(text='great guess')
    else:
        label2.config(text='wrong answer.try again!')
    if '-' not in guess:
        label2.config(text='you win')


label=Label(win, text='')
label.pack()
entry=Entry(win,)
entry.pack()
label2=Label(win, text=' ')
label2.pack()
button2=Button(win,text='start',command=show)
button2.pack()
button=Button(win, text='check',command=check)
button.pack()

win.mainloop()
