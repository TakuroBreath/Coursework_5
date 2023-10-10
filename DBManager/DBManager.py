import psycopg2

"""
idishniki
15478 - VK
1740 - Яндекс
1102601 - Самолет
2120 - Азбука Вкуса
3127 - МегаФон
4880 - Детский Мир
816144 - ВкусВилл
839098 - Автомакон
3529 - Сбер
78638 - Тинькофф
80 - Альфа-Банк
"""


class DBManager:
    def __init__(self, password):
        self.__password = password

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании."""
        companies = []
        try:
            conn = psycopg2.connect(host="localhost", user="postgres", dbname="HeadHunter", password=self.__password)
            cur = conn.cursor()

            cur.execute("SELECT name FROM employers")
            name = cur.fetchall()

            cur.execute("SELECT vacancy_count FROM employers")
            vacancy_count = cur.fetchall()

            conn.commit()
            cur.close()
            conn.close()

            for i in range(len(name)):
                companies.append((name[i][0], vacancy_count[i][0]))

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return companies

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"""
        all_vacancies = []
        try:
            conn = psycopg2.connect(host="localhost", user="postgres", dbname="HeadHunter", password=self.__password)
            cur = conn.cursor()

            cur.execute("""SELECT employers.name as employer, vacancies.name as vacancy, salary, url 
                        FROM vacancies 
                        JOIN employers ON employers.id = vacancies.employer_id""")
            all_vacancies = cur.fetchall()

            conn.commit()
            cur.close()
            conn.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return all_vacancies

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям."""
        try:
            conn = psycopg2.connect(host="localhost", user="postgres", dbname="HeadHunter", password=self.__password)
            cur = conn.cursor()

            cur.execute("""SELECT AVG(salary) FROM vacancies""")
            avg_salary = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return avg_salary[0][0]

    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        try:
            conn = psycopg2.connect(host="localhost", user="postgres", dbname="HeadHunter", password=self.__password)
            cur = conn.cursor()

            cur.execute("""SELECT employers.name as employer, vacancies.name as vacancy, salary, url 
                        FROM vacancies
                        JOIN employers ON employers.id = vacancies.employer_id
                        WHERE salary > (SELECT avg(salary) FROM vacancies)""")
            vacancies = cur.fetchall()

            conn.commit()
            cur.close()
            conn.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return vacancies

    def get_vacancies_with_keyword(self, keyword):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python."""
        try:
            conn = psycopg2.connect(host="localhost", user="postgres", dbname="HeadHunter", password=self.__password)
            cur = conn.cursor()

            cur.execute(f"""SELECT employers.name as employer, vacancies.name as vacancy, salary, url 
                        FROM vacancies
                        JOIN employers ON employers.id = vacancies.employer_id
                        WHERE LOWER(vacancies.name) LIKE '%{keyword.lower()}%'""")
            vacancies = cur.fetchall()

            conn.commit()
            cur.close()
            conn.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return vacancies
