from tech_news.database import db


def top_5_categories():
    categories = db.news.aggregate([
        {"$unwind": "$category"},
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
    ])
    sort_categories = sorted(categories, key=lambda x: (-x['count'], x['_id']))
    pop_categories = [category['_id'] for category in sort_categories[:5]]
    return pop_categories
