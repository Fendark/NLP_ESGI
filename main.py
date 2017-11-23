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
    source_file = train_set_content.split("-DOCSTART- -X- O O")[:200]
    documentList = list()
    for doc in source_file:
        if doc == '':
            continue
        word_list = list()
        label_list = list()
        sentences_list = list()
        offset = 0
        for sentence in doc.strip().split("\n\n"):
            #print(sentence + " ||||")
            start = offset
            if sentence == '':
                continue
            for line in sentence.split("\n"):
                w = line.split(" ")
                offset += 1
                word_list.append(w[0].strip())
                label_list.append(w[-1])
            sentences_list.append(Interval(start, offset))
            offset += 1
        documentList.append(Document().create_from_vectors(word_list, sentences_list, label_list))

    #print(testDocument.sentences)
    train_set.close()
    print("Finished")
