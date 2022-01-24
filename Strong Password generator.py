from tkinter import *

root = Tk()
root.geometry('600x600')
root.title('Strong passwords generator')

symbols_lbl = Label(root, text='Include symbols? (*#@)')
symbols_lbl.place(x=10, y=50, width=150, height=20)


mainloop()