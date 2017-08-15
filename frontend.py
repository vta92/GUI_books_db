"""
A program that store records based on:
Title, Author, Year, ISBN

User Can:
View records, Search an entry, Add entry, Update Entry, Delete, Close
Tkinter frontend with sqlite3 db backend
"""
from tkinter import *

root = Tk()

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
sb1 = Scrollbar(root)

b1 = Button(root, text='Query', width = 12)
b2 = Button(root, text='Search', width = 12)
b3 = Button(root, text='Add', width = 12)
b4 = Button(root, text='Update', width = 12)
b5 = Button(root, text='Delete', width = 12)
b6 = Button(root, text='Close', width = 12)




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

b1.grid(row=2, column=3)
b2.grid(row=4, column=3)
b3.grid(row=5, column=3)
b4.grid(row=6, column=3)
b5.grid(row=7, column=3)
b6.grid(row=8, column=3)

root.mainloop()
