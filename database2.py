#MY FIRST SQLITE DATABASE VIA PYTHON

import csv                                                      
from dataclasses import dataclass
from datetime import date
import sqlite3

@dataclass
class Rene:
    name: str
    surname: str
    country: str
    date_of_birth: date
    job: str

file_name = 'users.csv'
users = []


with open(file_name, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        users.append(Rene(*row))

print(users)

def save_db(users):
    con = sqlite3.connect("podbrezova.db")
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS podbrezova")
        cur.execute("CREATE TABLE podbrezova(id INTEGER PRIMARY KEY, name TEXT, surname TEXT, country TEXT, date_of_birth DATE, job TEXT)")
        for user in users:
            cur.execute("INSERT INTO podbrezova(name, surname, country, date_of_birth, job) VALUES(?,?,?,?,?)", 
                        (user.name, user.surname, user.country, user.date_of_birth, user.job))


save_db(users)



