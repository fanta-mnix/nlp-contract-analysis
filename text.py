# coding=utf-8
__all__ = ['normalize_symbols', 'remove_headers', 'remove_emphasis', 'remove_diacritics', 'remove_punctuation',
           'remove_stopwords', 'remove_numbers', 'lowercase', 'word_tokenize', 'chain']

import functools
import string
import nltk
import re

from patterns import *


CUSTOM_STOPWORDS = [u"500px", u"i", u"ii", u"iii", u"iv", u"v", u"vi", u"vii", u"viii", u"ix", u"x"]


def normalize_symbols(text):
    mapping = {u"’": u"'",
               u'"': u''}

    def replace(match):
        return mapping[match.group(0)]

    return re.sub(ur'[{}]'.format(ur''.join(mapping.keys())), replace, text)


def remove_diacritics(text):
    import unicodedata
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')


def remove_headers(text):
    return re.sub(r'(?<=\n)#+ .*\n', '', text)


def remove_emphasis(text):
    return re.sub(r'\*\*', '', text)


def filter_blacklist(tokens, blacklist):
    return (token for token in tokens if token not in blacklist)


def remove_numbers(tokens):
    number_pattern = re.compile(r'^[\d,.]+$')

    def is_number(value):
        if number_pattern.match(value):
            return True
        return False

    return (token for token in tokens if not is_number(token))


def chain(fs, x):
    return reduce(lambda acc, f: f(acc), fs, x)


remove_punctuation = functools.partial(filter_blacklist, blacklist=set(string.punctuation))
remove_stopwords = functools.partial(filter_blacklist,
                                     blacklist=set(CUSTOM_STOPWORDS + nltk.corpus.stopwords.words('english')))

word_tokenize = functools.partial(tokenize_with_regexp, re.compile(r'(?:{}|{})'.format(SITE_PATTERN, WORD_PATTERN)))
lowercase = functools.partial(map, unicode.lower)
