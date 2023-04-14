from parsel import Selector
from tech_news.database import create_news
import requests
import time


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        page_result = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        if page_result.status_code == 200:
            return page_result.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    all_url = selector.css("h2.entry-title a::attr(href)").getall()
    if all_url:
        return all_url
    else:
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css('a.next.page-numbers::attr(href)').get()
    if next_page:
        return next_page
    return None


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)

    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css('.entry-title::text').get().strip()
    timestamp = selector.css('li.meta-date::text').get()
    writer = selector.css('span.author a::text').get()
    reading_time = int(
        selector.css('.meta-reading-time::text').get().split()[0])
    summary = "".join(
        selector.css(".entry-content > p:nth-of-type(1) ::text").getall()
        ).strip()
    category = selector.css('.category-style span.label::text').get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category
    }


# Requisito 5
def get_tech_news(amount):
    data = fetch("https://blog.betrybe.com/")
    links = scrape_updates(data)
    index = 0
    news = []
    while len(news) < amount:
        news.append(scrape_news(fetch(links[index])))
        if index == len(links) - 1:
            url = scrape_next_page_link(data)
            data = fetch(url)
            links = scrape_updates(data)
            index = 0
        else:
            index += 1
    create_news(news)
    return news
