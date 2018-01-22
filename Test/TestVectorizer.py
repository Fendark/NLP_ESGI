import unittest
from DocumentObject import Vectorizer
from Parsers import EnglishNerParser
import os


class TestVectorizer(unittest):
    def test_englishNERParser(self):
        docs = EnglishNerParser().read_file(os.path.join('dataset', 'eng.testa.txt'))
        vectorizer = Vectorizer(word_embedding_path=os.path.join("dataset", "embeddings", "fichier"))

        vectorizer.encode_features(docs)