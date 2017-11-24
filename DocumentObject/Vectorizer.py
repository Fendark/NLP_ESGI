from gensim.models import KeyedVectors
from typing import List
from DocumentObject import Document


class Vectorizer:
    """ Transform a string into a vector representation"""

    def __init__(self, word_embedding_path: str):
        """
        :param word_embedding_path: path to gensim embedding file
        """
        # Load word embeddings from file
        # Create POS to index dictionary
        # Create shape to index dictionary
        # Create labels to index

    def encode_features(self, documents: List[Document]):
        """
        Creates a feature matrix for all documents in the sample list
        :param documents: list of all samples as document objects
        :return: lists of numpy arrays for word, pos and shape features.
                 Each item in the list is a sentence, i.e. a list of indices (one per token)
        """
        # Loop over documents
        #    Loop over sentences
        #        Loop over tokens
        #           Convert features to indices
        #           Append to sentence
        #   append to sentences
        # return word, pos, shape

    def encode_annotations(self, documents: List[Document]):
        """
        Creates the Y matrix representing the annotations (or true positives) of a list of documents
        :param documents: list of documents to be converted in annotations vector
        :return: numpy array. Each item in the list is a sentence, i.e. a list of labels (one per token)
        """
        # Loop over documents
        #    Loop over sentences
        #        Loop over tokens
        #           Convert label to numerical representation
        #           Append to sentence
        # return labels
