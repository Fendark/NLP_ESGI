from DocumentObject import Vectorizer
import unittest

class VectorizerTest(unittest.TestCase):

    def test_sample(self):
        vectorizer = Vectorizer("D:/Project/nlp/NLP_ESGI/External/glove.6B.50d.w2v.txt")
        print(vectorizer.word_embeddings)

if __name__ == "__main__":
    #unittest.main()
    test = VectorizerTest()
    test.test_sample()