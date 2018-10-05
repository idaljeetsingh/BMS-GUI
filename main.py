"""
    Title       :   Book Management System
    Author      :   Daljeet Singh Chhabra
    Language    :   Python
    File Name   :   main.py
    Date Created    :   04-10-2018
    Last Modified   :   05-10-2018
"""


from tkinter import *
import backend


def get_selected_row(event):
    try:
        global selected_tuple
        index = book_list.curselection()[0]
        selected_tuple = book_list.get(index)
        title_entry.delete(0, END)
        title_entry.insert(END, selected_tuple[1])

        author_entry.delete(0, END)
        author_entry.insert(END, selected_tuple[2])

        year_entry.delete(0, END)
        year_entry.insert(END, selected_tuple[3])

        isbn_entry.delete(0, END)
        isbn_entry.insert(END, selected_tuple[4])

    except IndexError:
        pass


def view_command():
    book_list.delete(0, END)
    for row in backend.view():
        book_list.insert(END, row)


def search_command():
    book_list.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        book_list.insert(END, row)


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    book_list.delete(0, END)
    book_list.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


def delete_command():
    backend.delete(selected_tuple[0])
    view_command()


window = Tk()
window.title("Book Management System")

title_label = Label(window, text="Title")
title_label.grid(row=0, column=0)

title_text = StringVar()
title_entry = Entry(window, textvariable=title_text)
title_entry.grid(row=0, column=1)

author_label = Label(window, text="Author")
author_label.grid(row=0, column=3)

author_text = StringVar()
author_entry = Entry(window, textvariable=author_text)
author_entry.grid(row=0, column=4)

isbn_label = Label(window, text="ISBN")
isbn_label.grid(row=1, column=0)

isbn_text = StringVar()
isbn_entry = Entry(window, textvariable=isbn_text)
isbn_entry.grid(row=1, column=1)

year_label = Label(window, text="Year")
year_label.grid(row=1, column=3)

year_text = StringVar()
year_entry = Entry(window, textvariable=year_text)
year_entry.grid(row=1, column=4)

book_list = Listbox(window, height=10, width=40)
book_list.grid(row=3, column=0, rowspan=6, columnspan=3)

s_bar = Scrollbar(window)
s_bar.grid(row=2, column=3, rowspan=6)

book_list.configure(yscrollcommand=s_bar.set)
s_bar.configure(command=book_list.yview)

book_list.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=3, column=4)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=4, column=4)

b3 = Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=5, column=4)

b4 = Button(window, text="Update selected", width=12, command=update_command)
b4.grid(row=6, column=4)

b5 = Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=7, column=4)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=8, column=4)

window.mainloop()
