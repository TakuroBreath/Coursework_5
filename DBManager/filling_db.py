import psycopg2


class Database:
    def __init__(self, password):
        self.__password = password

    def create_db(self):
        try:
            conn = psycopg2.connect(host="localhost", user="postgres", dbname="HeadHunter", password=self.__password)
            cur = conn.cursor()
            cur.execute("""
            CREATE TABLE public.employers(
            id serial NOT NULL,
            name character varying NOT NULL,
            vacancy_count integer NOT NULL,
            PRIMARY KEY (id));
            
            CREATE TABLE public.vacancies(
            id serial NOT NULL,
            employer_id integer NOT NULL,
            name character varying NOT NULL,
            salary integer,
            url character varying NOT NULL,
            CONSTRAINT employer_id FOREIGN KEY (employer_id)
                REFERENCES public.employers (id) MATCH SIMPLE);""")
            conn.commit()
            cur.close()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


db = Database(2368)
db.create_db()
