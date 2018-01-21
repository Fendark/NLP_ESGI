import os
from Parsers.EnglishNerParser import EnglishNerParser
from DocumentObject.Vectorizer import Vectorizer
from keras.utils import np_utils
from NeuralNetwork.RecurrentNeuralNetwork import RecurrentNeuralNetwork
import numpy
from keras.preprocessing import sequence
from keras.callbacks import EarlyStopping, ModelCheckpoint

if __name__ == "__main__":
    training_set_filename = "eng.train.txt"
    training_set_path = "dataset/"
    filename = os.path.join(training_set_path, training_set_filename)
    file = open(filename,"r")
    print("Document to parse: {}".format(filename))
    print("Initiate Parser...")
    file_parser = EnglishNerParser()
    print("Parser: OK")
    print("Parsing Document...")
    documents_list = file_parser.read(file.read())
    file.close()
    print('Create features')
    vectorizer = Vectorizer(word_embedding_path='External/glove.6B.50d.w2v.txt')
    features = vectorizer.encode_features(documents_list)
    labels = vectorizer.encode_annotations(documents_list)
    print('Loaded {} data samples'.format(len(features)))

    print('Split training/validation')
    max_length = 60
    split_percent = int(numpy.ceil(len(features) * 0.7))
    print("Split index = {}".format(split_percent))
    # --------------- Features ----------------
    x_train = features[:split_percent]
    x_validation = features[split_percent:]
    x_train = sequence.pad_sequences(x_train, maxlen=max_length)
    x_validation = sequence.pad_sequences(x_validation, maxlen=max_length)

    # --------------- Labels -------------------
    y_train, y_validation = [], []
    labels = [np_utils.to_categorical(y_group, num_classes=len(vectorizer.labels)) for y_group in labels]
    y_train = labels[:split_percent]
    y_validation = labels[split_percent:]
    y_train = sequence.pad_sequences(y_train, maxlen=max_length)
    y_validation = sequence.pad_sequences(y_validation, maxlen=max_length)

    print('Building network...')
    model = RecurrentNeuralNetwork.build_classification(word_embeddings=vectorizer.word_embeddings,
                                                input_shape={'pos': (len(vectorizer.pos2index), 10),
                                                             'shape': (len(vectorizer.shape2index), 2),
                                                             'max_length': max_length},
                                                out_shape=len(vectorizer.labels),
                                                units=100, dropout_rate=0.5)

    print('Train...')
    trained_model_name = 'ner_weights.h5'
    early_stopping = EarlyStopping(monitor='val_loss', patience=10)
    saveBestModel = ModelCheckpoint(trained_model_name, monitor='val_loss', verbose=1, save_best_only=True, mode='auto')
    model.fit(x_train, y_train,
              validation_data=(x_validation, y_validation),
              batch_size=32, epochs=10, callbacks=[saveBestModel, early_stopping])

    # Use the test data: Unpadded feature vectors + unpaded and numerical (not one-hot vectors) labels

    y_prediction, y_validation = [], []
    # For each sample (one at a time)
    # Predict labels and convert from probabilities to classes
    # RecurrentNeuralNetwork.probas_to_classes()

    print("Finished!")
