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
    req = requests.get("https://api.hh.ru/vacancies?employer_id=15478")
    data = req.content.decode()
    req.close()
    js = json.loads(data)

    t = js['found']
    pages = t // 100
    for page in range(pages+1):
        params = {
            'employer_id': 15478,  # ID VK
            'area': 113,  # Поиск в зоне 113 - RF
            'page': page,  # Номер страницы
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
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
