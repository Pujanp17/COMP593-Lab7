from string import digits
from faker import Faker
import sqlite3
from datetime import datetime


con = sqlite3.connect('database111.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS table1 (name text, address text, email text, age integer, date text)''')

def main():
    fake_data = Faker()
    cur.execute('INSERT INTO table1 VALUES (:name, :address, :email, :age, :date )',
            {'name': fake_data.name(), 'address' : fake_data.address(), 'email' : fake_data.email(), 'age' : fake_data.random_number(digits=2), 
                'date' : fake_data.date_this_month()}
        )

for i in range(200):
    main()

print(i)
con.commit()
con.close()





