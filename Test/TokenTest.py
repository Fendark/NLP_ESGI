from DocumentObject import Token
from DocumentObject import Document
import unittest

class TokenTest(unittest.TestCase):

    def test_sample(self):

        token = Token("Hello", 0, 4, "NNP", Document.get_shape_category("Hello"), "Hello")
        self.assertEqual(token._doc, "Hello", 'ERROR : TOKEN_DOC')
        self.assertEqual(token._pos, "NNP", 'ERROR : TOKEN_POSTAG')
        self.assertEqual(token._shape, "1ST-CAP", 'ERROR : TOKEN_SHAPE')
        self.assertEqual(token._text, "Hello", 'ERROR : TOKEN_text')
        self.assertEqual(token._label, None, 'ERROR : TOKEN_label')

if __name__ == "__main__":
    unittest.main()