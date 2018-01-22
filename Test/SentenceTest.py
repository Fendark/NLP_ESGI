import unittest
from DocumentObject import Sentence
from DocumentObject import Document

class SentenceTest(unittest.TestCase):

    def test(self):
        text = "Hello, I am a jolly platypus. " \
               "I like to run and roll on tremendous hills. " \
               "I do love to run and roll, but i like to sing too! " \
               "So the jolly platypus ran, rolled and sung on tremendous hills. "
        doc = Document.create_from_text(text)

        self.assertTrue(Sentence(doc,0,100))
        self.assertRaises(ValueError,Sentence.__init__,self,doc,1,0)
