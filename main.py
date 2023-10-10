import os

if __name__ == '__main__':
    os.system('pip install psycopg2')
    os.system('pip install requests')
    from user import *
    from DBManager.filling_db import *
    from DBManager.DBManager import *

    os.system('cls')
    choice = greetings()
    os.system('cls')
    os.system('cls')
    while True:
        if choice == '1':
            passw = password()
            action_one(passw)
            manager = DBManager(passw)
            second_choice = action_two()
        elif choice == '2':
            passw = password()
            manager = DBManager(passw)
            second_choice = action_two()
        else:
            break

        if second_choice == '1':
            os.system('cls')
            for company in manager.get_companies_and_vacancies_count():
                print(f"Company: {company[0]} - Vacancies count: {company[1]}")

        elif second_choice == '2':
            os.system('cls')
            for company in manager.get_all_vacancies():
                print(f"Employer: {company[0]}\nVacancy: {company[1]}\nSalary: {company[2]}\nURL: {company[3]}\n\n")

        elif second_choice == '3':
            os.system('cls')
            print(f"Average salary: {manager.get_avg_salary()}")


        elif second_choice == '4':
            os.system('cls')
            for company in manager.get_vacancies_with_higher_salary():
                print(f"Employer: {company[0]}\nVacancy: {company[1]}\nSalary: {company[2]}\nURL: {company[3]}\n\n")

        elif second_choice == '5':
            os.system('cls')
            keyword = input("Enter keyword: ")
            for company in manager.get_vacancies_with_keyword(keyword):
                print(f"Employer: {company[0]}\nVacancy: {company[1]}\nSalary: {company[2]}\nURL: {company[3]}\n\n")

        else:
            break
