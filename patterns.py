SITE_PATTERN = r'\b(?:[a-z]+://)?(?:\w{2,}\.)+?(?:com|net|org)(?:/[^/]+)*\b'
WORD_PATTERN = r'\b\w{2,}\b'


def tokenize_with_regexp(regexp, sent):
    return regexp.findall(sent)