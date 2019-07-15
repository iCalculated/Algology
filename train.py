from gensim.models import KeyedVectors
from gensim.test.utils import get_tmpfile


if __name__ == '__main__':
    try:
        load('word2vec.model')
    except:
        file = './GoogleNews-vectors-negative300.bin'

    print(f"Training from {file}")
    model = KeyedVectors.load_word2vec_format(file, binary=True)

    print("Model trained")

    print("Saving model")
    #All who try to run this be warned, it will eat your computer
    model_file = get_tmpfile("word2vec.model")
    model.save(model_file)
    print("Model saved")


