import tkinter as tk
from tkinter import *


root = Tk()

root.title('Welcome to The Subtle Art of Not Giving a Fuck Hacks')
root.geometry("400x400")
label1 = Label(root, text='UnFuck Your Mind Hacks')
label1.grid(row=0, column=0)


def clicked():
    btn['state'] = 'disabled'
    btn['text'] = 'Subscribed'
    btn['bg'] = 'Green'
    label2 = Label(root, text='Thank You')
    label2.grid()


btn = Button(root, text='Subscribed', fg='red',bg='white', command=clicked)
btn.grid(row=0 , column=1)
#------------------------------------------------
root.mainloop()