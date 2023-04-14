from tech_news.database import db


# Requisito 7
def search_by_title(title):
    lista = []
    pesquisa = db.news.find({'title': {'$regex': title, '$options': 'i'}})
    for valor in pesquisa:
        lista.append((valor['title'], valor['url']))
    return lista


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
