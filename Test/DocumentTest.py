from DocumentObject import Document
import unittest

class DocumentTest(unittest.TestCase):

    def test_sample(self):
        text = "Hello, I am a jolly platypus. " \
               "I like to run and roll on tremendous hills. " \
               "I do love to run and roll, but i like to sing too! " \
               "So the jolly platypus ran, rolled and sung on tremendous hills. "
        doc = Document.create_from_text(text)

        self.assertEqual(len(doc.tokens), 46, 'ERROR : tokens')
        self.assertEquals(len(doc.sentences), 4, 'ERROR : sentences')

if __name__ == "__main__":
    unittest.main()