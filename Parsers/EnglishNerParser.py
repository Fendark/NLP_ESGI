from Parsers.Parser import Parser
from DocumentObject import Document
from DocumentObject import Interval
from typing import List


class EnglishNerParser(Parser):
    def read(self, content: str) -> List[Document]:
        documents_list = list()
        docs = content.split("-DOCSTART- -X- O O")
        for doc in docs:
            word_list = list()
            label_list = list()
            sentences_list = list()
            offset = 0
            if doc == '':
                continue
            for sentence in doc.strip().split("\n\n"):
                start = offset
                if sentence == '':
                    continue
                for line in sentence.split("\n"):
                    words = line.split(" ")
                    offset += 1
                    word_list.append(words[0].strip())
                    label_list.append(words[-1])
                sentences_list.append(Interval(start, offset))
                offset += 1
            documents_list.append(Document().create_from_vectors(word_list, sentences_list, label_list))
        return documents_list
