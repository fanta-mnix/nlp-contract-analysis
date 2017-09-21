def write_all(path, content, encoding='utf-8'):
    with open(path, 'w') as writer:
        writer.write(content.encode(encoding))


def read_all(path, encoding='utf-8'):
    with open(path) as reader:
        return reader.read().decode(encoding)
