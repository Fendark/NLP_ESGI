from DocumentObject import Document

class Parser(object):
    def create(self):
        return self

    def read_file(self, filename: str) -> Document:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        return self.read(content)


class simpleTextParser(Parser):
    def read(self, content: str) -> Document:
        return Document().create_from_text(content)

