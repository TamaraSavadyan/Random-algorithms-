"""Image viewer App"""
# from tkinter import *
# from PIL import ImageTk, Image
#
# root = Tk()
# root.title("Image viewer")
# # root.geometry("400x200")
#
# myImg_1 = ImageTk.PhotoImage(Image.open('C:/Я картинки/1.png'))
# myImg_2 = ImageTk.PhotoImage(Image.open('C:/Я картинки/2.png'))
# myImg_3 = ImageTk.PhotoImage(Image.open('C:/Я картинки/3.png'))
#
# My_Images = [myImg_1, myImg_2, myImg_3]
#
# status = Label(root, text='Image 1 of ' + str(len(My_Images)), bd=1, relief=SUNKEN, anchor=E)
# status.grid(row=2, column=0, columnspan=3, sticky=W+E)
#
# myLabel = Label(root, image=myImg_1)
# myLabel.grid(row=0, column=0, columnspan=3)
#
#
# def back(image_number):
#     global myLabel
#     # global Button_Back, status
#     # global Button_Forward
#
#     myLabel.grid_forget()
#     myLabel = Label(image=My_Images[image_number - 1])
#     Button_Forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
#     Button_Back = Button(root, text='<<', command=lambda: back(image_number - 1))
#     status = Label(root, text='Image ' + str(image_number) + ' of ' + str(len(My_Images)), bd=1, relief=SUNKEN, anchor=E)
#
#     if image_number == 1:
#         Button_Back = Button(root, text='<<', state=DISABLED)
#
#     Button_Forward.grid(row=1, column=2)
#     Button_Back.grid(row=1, column=0)
#     myLabel.grid(row=0, column=0, columnspan=3)
#     status.grid(row=2, column=0, columnspan=3, sticky=W + E)
#
# def forward(image_number):
#     global myLabel
#     # global Button_Back, status
#     # global Button_Forward
#
#     myLabel.grid_forget()
#     myLabel = Label(image=My_Images[image_number - 1])
#     Button_Forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
#     Button_Back = Button(root, text='<<', command=lambda: back(image_number - 1))
#     status = Label(root, text='Image ' + str(image_number) + ' of ' + str(len(My_Images)), bd=1, relief=SUNKEN, anchor=E)
#
#     if image_number == len(My_Images):
#         Button_Forward = Button(root, text='>>', state=DISABLED)
#
#     Button_Forward.grid(row=1, column=2)
#     Button_Back.grid(row=1, column=0)
#     myLabel.grid(row=0, column=0, columnspan=3)
#     status.grid(row=2, column=0, columnspan=3, sticky=W + E)
#
#
# Button_Back = Button(root, text='<<', command=back, state=DISABLED)
# Button_Quit = Button(root, text='Quit', command=root.quit)
# Button_Forward = Button(root, text='>>', command=lambda: forward(2))
#
# Button_Back.grid(row=1, column=0)
# Button_Quit.grid(row=1, column=1)
# Button_Forward.grid(row=1, column=2, pady=10)
#
# root.mainloop()
'''Some other stuff (radiobuttons, messageboxes, frames etc.)'''
# from tkinter import *
# from tkinter import messagebox
# from PIL import ImageTk, Image
#
# root = Tk()
# root.title("TK")
# root.geometry("300x200")
# # root.iconbitmap('C:/Star icon.ico')
#
# # frame = LabelFrame(root, text='FRameE', padx=5, pady=5)
# # frame.pack(padx=10, pady=10)
# #
# # b = Button(frame, text='hello and bye', command=root.quit)
# # b2 = Button(frame, text='Yellow', bg='#cc0')
# # b.grid(row=0, column=0)
# # b2.grid(row=1, column=1)
# r = IntVar()
# r.set(2)
#
# MODES = [
#     ('Pepperoni', '1'),
#     ('Cheese', '2'),
#     ('Mushroom', '3'),
#     ('Onion', '4')
# ]
#
# pizza = StringVar()
# pizza.set("Pepperoni")
#
# for text, mode in MODES:
#     Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)
#
#
# def clicked(value):
#     myLabel = Label(root, text=value)
#     myLabel.pack()
#
#
# # Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
# # Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()
#
# # myLabel = Label(root, text=pizza.get())
# # myLabel.pack()
#
# myButton = Button(root, text='Click me!', command=lambda: clicked(pizza.get()))
# myButton.pack()
#
# '''All functions from messagebox
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno'''
#
#
# def popup():
#     response = messagebox.askyesno("Ho hey!", "Hello there!")
#     # Label(root, text=response).pack()
#     if response == 1:
#         Label(root, text="YES!").pack()
#     else:
#         Label(root, text="nooo").pack()
#
#
# Button(root, text='PopUp', command=popup).pack()
#
# mainloop()
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import sqlite3

root = Tk()
root.title("TK")
root.geometry("800x400")
root.iconbitmap("C:/Я картинки/Милыйдинозавр.ico")
'''Часть кода о дополнительном окне'''
# Label(root, text="MAJOR").grid(row=0, column=0)
#
# def place():
#     global img2
#     img2 = ImageTk.PhotoImage(Image.open('C:/Я картинки/1.png'))
#     Label(root, image=img2).grid(row=2, column=0)
#
#
# def open():
#     global my_img
#     top = Toplevel()
#     top.iconbitmap("C:/Я картинки/Милыйдинозавр.ico")
#     top.geometry("300x300")
#     Label(top, text='minor').pack()
#     my_img = ImageTk.PhotoImage(Image.open('C:/Я картинки/3.png'))
#     Label(top, image=my_img).pack()
#     Button(top, text='place image inside the root', command=place).pack()
#     Button(top, text='Close this window', command=top.destroy).pack()
#
#
# btn = Button(root, text='Open Second Window', command=open)
# btn.grid(row=1, column=0)
'''Some stuff (checkboxes, files)'''
# def Open_File():
#     global my_image
#     root.filename = filedialog.askopenfilename(initialdir='C:/Я картинки', title='Select a file',
#                                                filetypes=(('png files', '*.png'), ('all files', '*.*')))
#     Label(root, text=root.filename, fg='#faa').grid(row=1, column=0)
#     my_image = ImageTk.PhotoImage(Image.open(root.filename))
#     Label(root, image=my_image).grid(row=2, column=0)
#
#
# Button(root, text='Open File', command=Open_File).grid(row=0, column=0)
#
# def slide():
#     Label(root, text=horizontal.get()).grid(row=6, column=0)
#     root.geometry(str(horizontal.get()) + 'x' + str(vertical.get()))
#
#
# vertical = Scale(root, from_=1, to=500)
# vertical.grid(row=3, column=0)
#
# horizontal = Scale(root, from_=1, to=500, orient=HORIZONTAL)
# horizontal.grid(row=4, column=0)
#
# btn = Button(root, text='Change geometry!', command=slide)
# btn.grid(row=5, column=0)
#
# def show():
#     Label(root, text=var.get()).grid()
#
#
# var=IntVar()
#
# check = Checkbutton(root, text='Check this!', command=show, variable=var, onvalue=5, offvalue=2)
# check.grid()
'''Drop Down Boxes'''
# def show():
#     Label(root, text=clicked.get()).grid()
#
#
# options = ['Monday',
#            'Tuesday',
#            'Wednesday',
#            'Thursday',
#            'Friday']
#
# clicked = StringVar()
# clicked.set(options[0])
#
# drop = OptionMenu(root, clicked, *options)
# drop.grid()
#
# myBtn = Button(root, text='Show selection', command=show)
# myBtn.grid()
'''Databases'''
# Create database or connect to one
conn = sqlite3.connect('address_book.db')
# Create cursor
c = conn.cursor()
# Create table
'''
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )""")
'''
# Create delete a record function
def delete():
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

# Create submit function for database
def submit():
    # Create database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()
    # Clear textboxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create query function
def query():
    global query_label
    # Create database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
    # Query database
    c.execute('SELECT *, oid FROM addresses')
    records = c.fetchall()  # Also we can fetchone, fetchmany

    # Looping through records
    n = 0
    for n in range(len(records)):
        print_records = ''
        for record in records[n]:
            print_records += str(record) + "<||>"

        query_label = Label(root, text=print_records)
        query_label.grid(row=n, column=2)

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

# Create an Update function
def update():
    pass

# Create edit function to update a record
def edit():
    editor = Toplevel()
    editor.title("TK")
    editor.geometry("800x400")
    editor.iconbitmap("C:/Я картинки/Милыйдинозавр.ico")

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # Create database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    record_id = delete_box.get()
    # Query database
    c.execute('SELECT * FROM addresses WHERE oid = ' + record_id)
    records = c.fetchall()  # Also we can fetchone, fetchmany
                            #                  |         |
    # Looping through records
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        state_editor.insert(0, record[3])
        city_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Create textbox labels
    f_name_label_editor = Label(editor, text='First Name', anchor=W)
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))
    l_name_label_editor = Label(editor, text='Last Name', anchor=W)
    l_name_label_editor.grid(row=1, column=0)
    address_label_editor = Label(editor, text='Address', anchor=W)
    address_label_editor.grid(row=2, column=0)
    city_label_editor = Label(editor, text='City', anchor=W)
    city_label_editor.grid(row=3, column=0)
    state_label_editor = Label(editor, text='State', anchor=W)
    state_label_editor.grid(row=4, column=0)
    zipcode_label_editor = Label(editor, text='Zipcode', anchor=W)
    zipcode_label_editor.grid(row=5, column=0)

    save_btn = Button(editor, text='Save changes', command=update)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

# Create a clear sreen function
def clear():
    # Create database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
    # Query database
    c.execute('SELECT *, oid FROM addresses')
    records = c.fetchall()  # Also we can fetchone, fetchmany
    for i in range(len(records)):
        query_label.destroy()
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

# Create textboxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=8, column=1, pady=5)

# Create textbox labels
f_name_label = Label(root, text='First Name', anchor=W)
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text='Last Name', anchor=W)
l_name_label.grid(row=1, column=0)
address_label = Label(root, text='Address', anchor=W)
address_label.grid(row=2, column=0)
city_label = Label(root, text='City', anchor=W)
city_label.grid(row=3, column=0)
state_label = Label(root, text='State', anchor=W)
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text='Zipcode', anchor=W)
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=8, column=0, pady=5)

# Create Submit button
submit_button = Button(root, text='Add record to database', command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=0, padx=10, ipadx=100)

# Create a Query button
query_btn = Button(root, text="Show records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=0, padx=10, ipadx=130)

# Create a delete button
delete_btn = Button(root, text='Select record', command=delete)
delete_btn.grid(row=9, column=0, columnspan=2, pady=0, padx=10, ipadx=127)

# Create an Edit records button
edit_btn = Button(root, text='Edit record', command=edit)
edit_btn.grid(row=10, column=0, columnspan=2, pady=0, padx=10, ipadx=134.4)

# Create a clear screen button
clear_btn = Button(root, text='Clear', command=clear)
clear_btn.grid(row=11, column=1)

# Commit changes
conn.commit()
# Close connection
conn.close()


mainloop()
