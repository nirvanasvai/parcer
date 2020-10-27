import requests
import pprint
import json

api = {
    'main': "https://api.hh.ru/",
    'vacancies': 'https://api.hh.ru/vacancies/'
}

vacancies_string = []

def get_vacancies_by_id_or_slug(id):
    r = requests.get(url=f'https://api.hh.ru/vacancies/{id}')
    return json.loads(r.content)


def get_vacancies_text(text):
    r = requests.get(url=f'https://api.hh.ru/vacancies?text="{text}"')
    return json.loads(r.content)


def get_vacancies():
    r = requests.get(url=api['vacancies'])
    return json.loads(r.content)


for vacancie in get_vacancies_text('программист')['items']:
    print(vacancie['name'], vacancie['url'], vacancie['snippet']['requirement'].replace('&quot;', '"'))
    print(get_vacancies_by_id_or_slug(vacancie['id']))