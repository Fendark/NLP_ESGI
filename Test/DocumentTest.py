import unittest
from DocumentObject import Document

class DocumentTest(unittest.TestCase):

    def testCreateFromVector(self):
        return ""

    def testCreateFromText(self):
        test_text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo"
        test_doc =  Document().create_from_text(test_text)
        self.assertEqual(test_doc.tokens, 2)