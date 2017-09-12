def write_all(path, content):
    with open(path, 'w') as writer:
        writer.write(content.encode('utf8'))
