import json

import requests


def getEmployers():
    req = requests.get('https://api.hh.ru/employers')
    data = req.content.decode()
    req.close()
    count_of_employers = json.loads(data)['found']
    employers = []
    i = 0
    j = count_of_employers
    while i < j:
        req = requests.get('https://api.hh.ru/employers/' + str(i + 1))
        data = req.content.decode()
        req.close()
        jsObj = json.loads(data)
        try:
            employers.append([jsObj['id'], jsObj['name']])
            i += 1
            print([jsObj['id'], jsObj['name']])
        except:
            i += 1
            j += 1
    return employers


def api_work():
    params = {
        'employer_id': 15478,  # ID 2ГИС
        'area': 113,  # Поиск в зоне
        'page': 2,  # Номер страницы
        'per_page': 100  # Кол-во вакансий на 1 странице
    }
    # req = requests.get("https://api.hh.ru/vacancies?employer_id=15478")
    req = requests.get("https://api.hh.ru/vacancies", params)
    data = req.content.decode()
    req.close()
    js = json.loads(data)

    i = 0
    for l in js['items']:
        print(js['items'][i])
        i += 1

    print(len(js['items']))


api_work()

