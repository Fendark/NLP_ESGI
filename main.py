import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

from DocumentObject import Document


if __name__ == "__main__":
    moby_dick = gutenberg.raw('melville-moby_dick.txt')
    print(moby_dick[117:300])
    doc = Document.Document.create_from_text(moby_dick[117:300])