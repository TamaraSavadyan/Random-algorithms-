from tkinter import *
import operator

Operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
root = Tk()
root.title('Calculator')
# root.geometry('500x500')

e = Entry(root, fg='#0aa', width=49, borderwidth=5)
e.grid(row=0, column=0, columnspan=4)


def Plus():
    first_number = float(e.get())
    global f_num, operator
    f_num = first_number
    operator = '+'
    e.delete(0, END)


def Minus():
    global f_num, operator
    f_num = float(e.get())
    operator = '-'
    e.delete(0, END)


def Divide():
    global f_num, operator
    f_num = float(e.get())
    operator = '/'
    e.delete(0, END)


def Multiple():
    global f_num, operator
    f_num = float(e.get())
    operator = '*'
    e.delete(0, END)


def Equal():
    second_number = float(e.get())
    e.delete(0, END)
    e.insert(0, Operators[operator](f_num, second_number))


def Clear():
    e.delete(0, END)


def Number(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


Button_Plus = Button(root, text='+', padx=19, pady=10, command=Plus)
Button_Minus = Button(root, text='-', padx=20, pady=10, command=Minus)
Button_Divide = Button(root, text='/', padx=20, pady=10, command=Divide)
Button_Multiple = Button(root, text='*', padx=20, pady=10, command=Multiple)
Button_Equal = Button(root, text='=', padx=40, pady=10, command=Equal)
Button_Clear = Button(root, text='C', padx=40, pady=10, command=Clear)

Button_1 = Button(root, text='1', padx=40, pady=10, command=lambda: Number(1))
Button_2 = Button(root, text='2', padx=40, pady=10, command=lambda: Number(2))
Button_3 = Button(root, text='3', padx=40, pady=10, command=lambda: Number(3))
Button_4 = Button(root, text='4', padx=40, pady=10, command=lambda: Number(4))
Button_5 = Button(root, text='5', padx=40, pady=10, command=lambda: Number(5))
Button_6 = Button(root, text='6', padx=40, pady=10, command=lambda: Number(6))
Button_7 = Button(root, text='7', padx=40, pady=10, command=lambda: Number(7))
Button_8 = Button(root, text='8', padx=40, pady=10, command=lambda: Number(8))
Button_9 = Button(root, text='9', padx=40, pady=10, command=lambda: Number(9))
Button_0 = Button(root, text='0', padx=40, pady=10, command=lambda: Number(0))

Button_Equal.grid(row=4, column=1)
Button_Clear.grid(row=4, column=2)
Button_0.grid(row=4, column=0)

Button_1.grid(row=3, column=0)
Button_2.grid(row=3, column=1)
Button_3.grid(row=3, column=2)

Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)

Button_7.grid(row=1, column=0)
Button_8.grid(row=1, column=1)
Button_9.grid(row=1, column=2)

Button_Plus.grid(row=1, column=3)
Button_Minus.grid(row=2, column=3)
Button_Divide.grid(row=4, column=3)
Button_Multiple.grid(row=3, column=3)

root.mainloop()
