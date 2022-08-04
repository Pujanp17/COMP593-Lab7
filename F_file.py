from string import digits
from faker import Faker
import sqlite3
from datetime import datetime

fake_data = Faker()

name = fake_data.name();
address = fake_data.address();
email = fake_data.email();
age = fake_data.random_number(digits=2);
date = fake_data.date_this_month()

#profile = fake_data.simple_profile()
#for K in range (0,200):
 #   print(K)

con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS table1 (name text, address text, email text, age integer, date text)''')
cur.execute('INSERT INTO table1 VALUES (:name, :address, :email, :age, :date )',
            {'name': fake_data.name(), 'address' : fake_data.address(), 'email' : fake_data.email(), 'age' : fake_data.random_number(digits=2), 
                'date' : fake_data.date_this_month()}
        )
cur.execute('SELECT * FROM table1')

for i in cur.execute('SELECT name, address, email, age, date FROM table1'):
    print(i)

con.commit()
con.close()