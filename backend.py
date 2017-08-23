import sqlite3

#establish connection using ID as the unique primary key for fast query
def connect():
    conn = sqlite3.connect("books.db")
    curs = conn.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, \
    title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()


def insertion(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    curs = conn.cursor()
    curs.execute("INSERT INTO book VALUES(NULL,?,?,?,?)", (title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    curs = conn.cursor()
    curs.execute("SELECT * FROM book")
    rows = curs.fetchall()
    conn.commit()
    conn.close()
    return rows

#empty arguments to prevent bug of all 4 parameters being needed
def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("books.db")
    curs = conn.cursor()
    curs.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",\
    (title,author,year,isbn))
    rows = curs.fetchall()
    conn.commit()
    conn.close()
    return rows

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    curs = conn.cursor()
    curs.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect("books.db")
    curs = conn.cursor()
    curs.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()

#connect()
#insertion("A Game of Thrones", "George R. R. Martin",year=2011, isbn=553593714)
#print(view())
#print(search(year="2011"))
#delete(1)
#delete(2)
#update(10,"The Journey to Greatness","vinh", 1992, 1234567891)
#print(search(author="vinh"))
