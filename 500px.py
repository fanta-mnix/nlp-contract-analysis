import bs4
import requests

from scraping import format_element, write_all


response = requests.get('https://about.500px.com/terms/')
soup = bs4.BeautifulSoup(response.content, 'html5lib')
terms = u'\n'.join(format_element(el) for el in soup.select('div.section.clearfix > div.left'))

write_all('500px.txt', terms)
