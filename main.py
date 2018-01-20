import os
from Parsers.EnglishNerParser import EnglishNerParser
from DocumentObject.Vectorizer import Vectorizer
from keras.utils import np_utils
from NeuralNetwork.RecurrentNeuralNetwork import RecurrentNeuralNetwork


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
    print('Create features')
    vectorizer = Vectorizer(word_embedding_path='/Path/to/embeddings file')
    features = vectorizer.encode_features(documents_list)
    labels = vectorizer.encode_annotations(documents_list)
    print('Loaded {} data samples'.format(len(features)))

    print('Split training/validation')
    max_length = 60
    # --------------- Features ----------------
    x_train, x_validation =

    # For all feature types
    # 1. Split features to training and testing set
    # 2. Padd sequences
    x_[train | validation] = sequence.pad_sequences(features, maxlen=max_length)

    # --------------- Labels -------------------
    y_train, y_validation = [], []

    # 1. Convert to one-hot vectors
    labels = [np_utils.to_categorical(y_group, num_classes=len(vectorizer.labels)) for y_group in labels]
    # 2. Split labels to training and test set
    # 3. (only for sequence tagging) Pad sequences
    y_[train | validation] = sequence.pad_sequences(labels, maxlen=max_length)

    print('Building network...')
    RecurrentNeuralNetwork.build_sequence(word_embeddings=vectorizer.word_embeddings,
                                          input_shape={'pos': (len(vectorizer.pos2index), 10),
                                                       'shape': (len(vectorizer.shape2index), 2)},
                                          out_shape=len(vectorizer.labels),
                                          units=100, dropout_rate=0.5)
    # or
    RecurrentNeuralNetwork.build_classification(word_embeddings=vectorizer.word_embeddings,
                                                input_shape={'pos': (len(vectorizer.pos2index), 10),
                                                             'shape': (len(vectorizer.shape2index), 2),
                                                             'max_length': max_length},
                                                out_shape=len(vectorizer.labels),
                                                units=100, dropout_rate=0.5)

    print('Train...')
    trained_model_name = 'ner_weights.h5'

    # Callback that stops training based on the loss fuction
    early_stopping = EarlyStopping(monitor='val_loss', patience=10)

    # Callback that saves the best model across epochs
    saveBestModel = ModelCheckpoint(trained_model_name, monitor='val_loss', verbose=1, save_best_only=True, mode='auto')

    model.fit(x_train, y_train,
              validation_data=(x_validation, y_validation),
              batch_size=32, epochs=10, callbacks=[saveBestModel, early_stopping])

    # Load the best weights in the model
    model.load_weights(trained_model_name)

    # Save the complete model
    model.save('rnn.h5')

    # Use the test data: Unpadded feature vectors + unpaded and numerical (not one-hot vectors) labels

    y_prediction, y_validation = [], []
    # For each sample (one at a time)
    # Predict labels and convert from probabilities to classes
    # RecurrentNeuralNetwork.probas_to_classes()

    print(classification_report(y_validation, y_prediction))

    print('Reading training data')
    documents = YourParser().read_file('/Path/to/testingdata')

    print('Create features')
    vectorizer = Vectorizer(word_embedding_path='/Path/to/embeddings file')
    features = vectorizer.encode_features(documents)
    labels = vectorizer.encode_annotations(documents)
    print('Loaded {} data samples'.format(len(features)))

    model = Recurrent.load('/Path/to/modelfile')

    y_predictied = []
    # Loop over features
    # Predict labels and convert from probabilities to classes
    # model.predict(features, batch_size=1, verbose=0)
    # RecurrentNeuralNetwork.probas_to_classes()

    # Run classification report
    print(classification_report(labels, y_predictied))

    print("Finished!")
