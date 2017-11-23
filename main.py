#import nltk
#from nltk.corpus import gutenberg
#from nltk.tokenize import sent_tokenize
#from nltk.tokenize import word_tokenize
import os

from DocumentObject import Document
from DocumentObject import Interval


if __name__ == "__main__":
    #moby_dick = gutenberg.raw('melville-moby_dick.txt')
    #print(moby_dick[117:300])
    #doc = Document.Document.create_from_text(moby_dick[117:300])
    training_set_filename = "eng.train.txt"
    training_set_path = "dataset/"
    train_set = open(os.path.join(training_set_path, training_set_filename), "r")
    train_set_content = train_set.read()
    word_list = list()
    sentences_list = list()
    source_file = train_set_content.split("-DOCSTART- -X- O O")[:200]
    offset = 0
    for doc in source_file:
        for sentence in doc.split("\n\n"):
            #print(sentence + " ||||")
            start = offset
            if sentence == "":
                offset += 1
            else:
                for line in sentence.split("\n"):
                    for w in line.split(" ")[0]:
                        offset += len(w.strip())
                        word_list.append(w)
            sentences_list.append(Interval(start, offset))

    train_set.close()
