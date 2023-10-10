import psycopg2
from work_with_api import *


class Database:
    companies = [15478, 1740, 1102601, 2120, 3127, 4880, 816144, 839098, 3529, 78638, 80]

    def __init__(self, password):
        self.__password = password

    def create_db(self):
        try:
            conn = psycopg2.connect(host="localhost", user="postgres", dbname="HeadHunter", password=self.__password)
            cur = conn.cursor()
            cur.execute("""
            CREATE TABLE IF NOT EXISTS public.employers(
            id integer NOT NULL,
            name varchar NOT NULL,
            vacancy_count integer NOT NULL,
            CONSTRAINT employers_pkey PRIMARY KEY (id));
            
            CREATE TABLE IF NOT EXISTS vacancies(
            id integer NOT NULL UNIQUE,
            employer_id integer NOT NULL,
            name varchar NOT NULL,
            salary integer,
            url character varying NOT NULL,
            CONSTRAINT employer_id FOREIGN KEY (employer_id)
                REFERENCES employers)""")

            conn.commit()
            cur.close()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def insert_employer(self, employer_data):
        try:
            conn = psycopg2.connect(host="localhost", user="postgres", dbname="HeadHunter", password=self.__password)
            cur = conn.cursor()
            cur.execute("""
            INSERT INTO public.employers(id, name, vacancy_count)
            VALUES (%s, %s, %s)""", (employer_data['id'], employer_data['name'], employer_data['vacancy_count']))
            conn.commit()
            cur.close()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def insert_vacancy(self, vacancy_data):
        try:
            conn = psycopg2.connect(host="localhost", user="postgres", dbname="HeadHunter", password=self.__password)
            cur = conn.cursor()
            for i in range(len(vacancy_data)):
                cur.execute("""
            INSERT INTO public.vacancies(id, employer_id, name, salary, url)
            VALUES (%s, %s, %s, %s, %s)""", (
                    vacancy_data[i]['id'], vacancy_data[i]['employer_id'], vacancy_data[i]['name'],
                    vacancy_data[i]['salary'],
                    vacancy_data[i]['url']))

            conn.commit()
            cur.close()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
