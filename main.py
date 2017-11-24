import os
from Parsers.EnglishNerParser import EnglishNerParser


if __name__ == "__main__":
    training_set_filename = "eng.train.txt"
    training_set_path = "dataset/"
    filename = os.path.join(training_set_path, training_set_filename)
    print("Document to parse: {}".format(filename))
    print("Initiate Parser...")
    file_parser = EnglishNerParser()
    print("Parser: OK")
    print("Parsing Document...")
    documents_list = file_parser.read_file(filename)
    print("Finished!")
