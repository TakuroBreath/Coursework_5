import json
import requests


def vacancies(emp_id):
    vacancies_data = []
    vacancy = {}
    for page in range(0, 20):
        params = {
            'employer_id': emp_id,
            'area': 113,  # Поиск в зоне 113 - RF
            'page': page,  # Номер страницы
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        req = requests.get("https://api.hh.ru/vacancies", params)
        data = req.content.decode()
        req.close()
        js = json.loads(data)
        for i in range(len(js['items'])):
            if js['items'][i]['salary'] is None:
                vacancy = {'id': int(js['items'][i]['id']), 'name': js['items'][i]['name'],
                           'employer_id': int(emp_id),
                           'salary': None, 'url': js['items'][i]['alternate_url']}
            else:
                vacancy = {'id': int(js['items'][i]['id']), 'name': js['items'][i]['name'],
                           'employer_id': int(emp_id),
                           'salary': js['items'][i]['salary']['to'], 'url': js['items'][i]['alternate_url']}

            vacancies_data.append(vacancy)

    return vacancies_data


def employer_data(emp_id):
    req = requests.get(f"https://api.hh.ru/employers/{emp_id}")
    data = req.content.decode()
    req.close()
    js = json.loads(data)

    return {'id': js['id'], 'name': js['name'], 'vacancy_count': js["open_vacancies"]}
