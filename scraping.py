def format_element(root):
    import types

    def format_element_with(element):
        if isinstance(element, types.StringTypes):
            return element.strip()

        if element.name == 'br':
            return u'\n'

        inner_text = u' '.join(format_element_with(child) for child in element.children)

        if element.name == 'p':
            return u'\n' + inner_text + u'\n'

        if element.name == 'li':
            return u'- ' + inner_text + u'\n'

        if element.name in ['h1', 'h2', 'h3']:
            return u'\n<< ' + inner_text.upper() + u' >>\n'

        if element.name == 'strong':
            return u'**' + inner_text + u'**'

        return inner_text

    return format_element_with(root)


def write_all(path, content):
    with open(path, 'w') as writer:
        writer.write(content.encode('utf8'))
