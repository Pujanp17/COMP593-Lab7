from asyncore import read
import sqlite3
from pprint import pprint
from unicodedata import name

#connecting to database
con = sqlite3.connect('database111.db')
cur = con.cursor()

#fetching table from database
cur.execute('SELECT * FROM table1')
#fetching name and age.
cur.execute('SELECT name, age from table1')

var = cur.fetchall()
#using for loop to extract people age and name above 50.

for n in cur.execute('SELECT name,age FROM table1 WHERE age > 50'):

    print(f'{n} years old');

con.commit()
con.close()



