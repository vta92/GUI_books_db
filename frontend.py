"""
A program that store records based on:
Title, Author, Year, ISBN

User Can:
View records, Search an entry, Add entry, Update Entry, Delete, Close
Tkinter frontend with sqlite3 db backend
"""
from tkinter import *
import backend

#view function for frontend to see backend
def view_db():
    listbox.delete(0,END) #empty out the box from 0 to the end
    for rows in backend.view(): #list of tuples with (id,title,author,year,isbn)
        listbox.insert(END,rows) #new rows will be put at the end of the listbox

#searching the db
def search_db():
    listbox.delete(0,END)
    #don't use variable assignment, messing things up for partial entry searches

    for rows in backend.search(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()):
        listbox.insert(END,rows)

def add_db():
    listbox.delete(0,END)
    backend.insertion(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get())
    search_db() #view similar stuff to the inserted tuple

#use unique id to delete from the listbox
def delete_db():
    backend.delete(listbox_selection[0])
    view_db()

#connected with the listbox.bind() function.
#helper function to delete_db()
def list_binder(event):
    row=listbox.curselection()[0]
    global listbox_selection
    #print(row)
    listbox_selection = listbox.get(row) #getting first element of the tuple (id)
    #print(listbox_selection[0])

    #backfilling the entries after emptying the boxes
    entry_title.delete(0,END)
    entry_author.delete(0,END)
    entry_year.delete(0,END)
    entry_ISBN.delete(0,END)

    entry_title.insert(END,listbox_selection[1])
    entry_author.insert(END,listbox_selection[2])
    entry_year.insert(END,listbox_selection[3])
    entry_ISBN.insert(END,listbox_selection[4])

def update_db():
    #id + stringvar(), intvar() inputs
    backend.update(listbox_selection[0], title_text.get(), author_text.get(),
    year_text.get(), ISBN_text.get())
    search_db()

root = Tk()
root.wm_title("Book Database")
#Label widgets
lab1 = Label(root, text="Title")
lab2 = Label(root, text="Year")
lab3 = Label(root, text="Author")
lab4 = Label(root, text="ISBN")
#######################################
#Entry Widgets
title_text = StringVar()
year_text = IntVar()
author_text = StringVar()
ISBN_text = IntVar()

entry_title = Entry(root, textvariable=title_text)
entry_year = Entry(root, textvariable=year_text)
entry_author = Entry(root, textvariable=author_text)
entry_ISBN = Entry(root, textvariable=ISBN_text)

listbox = Listbox(root, height =6, width = 35)
#binding listbox to the user selection
listbox.bind("<<ListboxSelect>>", list_binder)

sb1 = Scrollbar(root)

b_view = Button(root, text='View', width = 12, command=view_db)
b_search = Button(root, text='Search', width = 12, command=search_db)
b_add = Button(root, text='Add', width = 12, command=add_db)
b_update = Button(root, text='Update', width = 12, command=update_db)
b_delete = Button(root, text='Delete', width = 12, command=delete_db)
b_close = Button(root, text='Close', width = 12, command=root.destroy)




#configure boxes for list and Scrollbar
listbox.configure(yscrollcommand=sb1.set) #vertical scrollbar set
sb1.configure(command=listbox.yview)
########################################
#grid layouts, labels and entries. Entries will be on the right of the labels
lab1.grid(row=0, column=0)
lab2.grid(row=1,column=0)
lab3.grid(row=0,column=2)
lab4.grid(row=1,column=2)

entry_title.grid(row=0,column=1)
entry_year.grid(row=1,column=1)
entry_author.grid(row=0,column=3)
entry_ISBN.grid(row=1,column=3)

listbox.grid(row=2,column=0,rowspan=6,columnspan=2)
sb1.grid(row=2,column=2,rowspan=6)

b_view.grid(row=2, column=3)
b_search.grid(row=4, column=3)
b_add.grid(row=5, column=3)
b_update.grid(row=6, column=3)
b_delete.grid(row=7, column=3)
b_close.grid(row=8, column=3)

root.mainloop()
