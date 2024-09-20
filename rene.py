import csv
from collections import namedtuple
from datetime import datetime
from dateutil.relativedelta import relativedelta

User = namedtuple('User', 'first_name last_name country date_of_birth job')

users = []
file_name = 'users.csv'

def calculate_age(dob_str):
    # dob = datetime.strptime(dob_str, "%Y-%m-%d")
    dob = datetime.fromisoformat(dob_str)
    today = datetime.today()
    
    age = relativedelta(today, dob)
    
    return age.years

with open(file_name, 'r') as f:

    reader = csv.reader(f)
    next(reader) # skips header

    for row in reader:
        users.append(User(*row))
 

sorted_users = sorted(users, key=lambda u: calculate_age(u.date_of_birth), 
                      reverse=True)
# sorted_users = sorted(users, key=lambda u: u.date_of_birth)

for user in sorted_users:
    print(user)