import bs4
import requests


class BaseScraper:
    def __init__(self, url, selector, cookie=None):
        self.url = url
        self.selector = selector
        self.cookie = cookie

    def parse(self, soup):
        return u'\n'.join(format_element(el) for el in soup.select(self.selector))

    def fetch(self):
        headers = {'Accept-Language': 'en-US,en;q=0.8'}
        if self.cookie is not None:
            headers['Cookie'] = self.cookie

        response = requests.get(self.url, headers=headers)
        soup = bs4.BeautifulSoup(response.content, 'html5lib')
        return self.parse(soup)


def format_element(root, indent_size=4):
    import types
    import re

    def join(iterable):
        def interleave():
            iterator = iter(item for item in iterable if item)
            try:
                last = next(iterator)
                yield last
            except StopIteration:
                return

            for el in iterator:
                if not last.endswith(u'\n'):
                    yield u' '

                yield el
                last = el

        return u''.join(interleave())

    def normalize_string(string):
        return re.sub(r'\s+', u' ', string).strip()

    def format_element_with(element, indentation):
        if isinstance(element, types.StringTypes):
            return normalize_string(element)

        if element.name == 'br':
            return u'\n'

        child_indentation = indentation + 1 if element.name == 'li' else indentation
        inner_text = join(format_element_with(child, child_indentation) for child in element.children)

        if element.name == 'p':
            return u'\n' + inner_text + u'\n'

        if element.name in ['ol', 'ul']:
            return u'\n' + inner_text

        if element.name == 'li':
            if not element.find(['h1', 'h2', 'h3', 'h4']):
                indent = u' ' * (indentation * indent_size)
                return indent + u'- ' + inner_text + u'\n'

        if element.name in ['h1', 'h2', 'h3', 'h4']:
            prefix = u'#' * int(element.name[1]) + u' '
            return u'\n' + prefix + inner_text.upper() + u'\n'

        if element.name == 'strong':
            return u'**' + inner_text + u'**'

        return inner_text

    return format_element_with(root, 0)
