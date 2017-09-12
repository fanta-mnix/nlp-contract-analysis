from scraper.BaseScraper import BaseScraper
from util import write_all


def save_terms(url, selector, path, cookie=None):
    terms = BaseScraper(url, selector, cookie).fetch()
    write_all(path, terms)


save_terms('https://web.archive.org/web/20120919090519/http://500px.com/terms',
           '#terms > div.left-legal > div.section > div.left', 'data/500px.md')
