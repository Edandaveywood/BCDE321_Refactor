import pickle
# from js_to_dot import JS_to_dot


class Pickler:

    def __init__(self):
        self.new_file_name = ''
        self.to_be_pickled = ''

    def serialise(self, to_pickle):
        pickle_file = open('pickle.txt', 'wb')
        pickle.dump(to_pickle, pickle_file)
        pickle_file.close()
