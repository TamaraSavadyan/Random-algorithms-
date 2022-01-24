from tkinter import *

root = Tk()
root.title('Программа Пийп про однородные функции (сейсмотомография)')
root.geometry('1000x1000')

def F1():
    myLabel = Label(root, text='hello')
    myLabel.grid(row=1, column=0, columnspan=5)


Button_F1 = Button(root, text='GOD0', width=20, command=F1).grid(row=0, column=0)
Button_F2 = Button(root, text='GOD1', width=20, command=F1).grid(row=0, column=1)
Button_F3 = Button(root, text='GOD2', width=20, command=F1).grid(row=0, column=2)
Button_F4 = Button(root, text='F4',  width=20, command=F1).grid(row=0, column=3)
Button_F5 = Button(root, text='F5', width=20, command=F1).grid(row=0, column=4)
# , pdx=10, pdy=10
root.mainloop()
