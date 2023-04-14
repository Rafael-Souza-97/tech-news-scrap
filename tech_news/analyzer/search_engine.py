from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    list = []
    search = db.news.find({'title': {'$regex': title, '$options': 'i'}})
    for value in search:
        list.append((value['title'], value['url']))
    return list


# Requisito 8
def search_by_date(date):
    try:
        search_date = "{:%d/%m/%Y}".format(datetime.strptime(date, '%Y-%m-%d'))
    except ValueError:
        raise ValueError('Data inválida')

    search = db.news.find({'timestamp': search_date})
    result = [(value['title'], value['url']) for value in search]
    return result


# Requisito 9
def search_by_category(category):
    list = []
    search = db.news.find({'category': {'$regex': category, '$options': 'i'}})
    for value in search:
        list.append((value['title'], value['url']))
    return list
