import pickle
import os
# from js_to_dot import JS_to_dot


class Pickler:

    def __init__(self):
        self.pickle_file_name = ''
        self.to_be_pickled = ''

    def serialise(self, to_pickle, pickle_file_name):
        self.pickle_file_name = pickle_file_name
        pickle_file = open(self.pickle_file_name, 'wb')
        pickle.dump(to_pickle, pickle_file)
        pickle_file.close()

    def de_serialise(self):
        pickle_file = open(self.pickle_file_name, 'rb')
        pickled = pickle.load(pickle_file)
        for keys in pickled:
            print(keys, "->", pickled[keys])
        pickle_file.close()

    def remove_pickle(self):
        os.remove(self.pickle_file_name)
        print(self.pickle_file_name + ' has been deleted')
