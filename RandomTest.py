import random
import unittest

class RandomTest(unittest.TestCase):

    def test_sample(self):
        liste = list(range(10))
        extract = random.sample(liste, 5)
        for e in extract:
            self.assertIn(e, liste)

        with self.assertRaises(ValueError) as context:
            extract = random.sample(liste, 11)

    def test_choice(self):
        liste = list(range(10))
        c = random.choice(liste)
        self.assertIn(c, liste)

    def test_shuffle(self):
        liste = list(range(10))
        random.shuffle(liste)
        liste.sort()
        self.assertEqual(liste, list(range(10)))

if __name__ == "__main__":
    rndTest = RandomTest()
    rndTest.test_sample()
    rndTest.test_shuffle()