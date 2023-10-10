from DBManager.filling_db import *
from work_with_api import *


def greetings():
    choose = input("""
Hello! Choose one of the following options:
1. Create a new DB
2. Connect to an existing DB
3. Exit
    
    """)
    return choose


def password():
    passw = input("Enter your password: ")
    return passw


def action_one(passw):
    print("Please, wait...")
    print("Your database is preparing...")
    db = Database(passw)
    db.create_db()

    counter = 0

    for company in db.companies:
        counter += 1
        db.insert_employer(employer_data(company))
        db.insert_vacancy(vacancies(company))
        print(f"Progress: {counter}/{len(db.companies)-1}")

    print("Your database is ready!\n")


def action_two():
    print("You have been connected to an existing database.\n")
    choice = input("""Choose one of the following options:
    1. Get companies and vacancies count
    2. Get all vacancies
    3. Get average salary
    4. Get vacancies with higher salary
    5. Get vacancies with keyword
    6. Exit
    
    """)
    return choice
