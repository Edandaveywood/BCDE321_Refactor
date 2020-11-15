import pickle
import os
from abc import ABC, abstractmethod


class PickleCreator(ABC):
    @abstractmethod
    def create_pickle(self):
        """"Creates a pickle object"""

    def serialise_pickle(self, to_pickle, pickle_file_name):
        pickle = self.create_pickle()
        result = pickle.serialise(to_pickle, pickle_file_name)
        return result

    def de_serialise_pickle(self, pickle_file_name):
        pickle = self.create_pickle()
        result = pickle.de_serialise(pickle_file_name)
        return result

    def remove_pickle(self, pickle_file_name):
        pickle = self.create_pickle()
        result = pickle.remove_pickle(pickle_file_name)
        return result


class Pickler(PickleCreator):
    def create_pickle(self):
        return Pickle()


class PickleFactory(ABC):
    @abstractmethod
    def serialise(self, to_pickle, pickle_file_name):
        """"Serialises a pickle"""

    @abstractmethod
    def de_serialise(self, pickle_file_name):
        """"De-serialises a pickle"""

    @abstractmethod
    def remove_pickle(self, pickle_file_name):
        """"Deletes pickle from HDD"""


class Pickle(PickleFactory):

    def serialise(self, to_pickle, pickle_file_name):
        pickle_file = open(pickle_file_name, 'wb')
        pickle.dump(to_pickle, pickle_file)
        pickle_file.close()
        return "Pickle has been created"

    def de_serialise(self, pickle_file_name):
        pickle_file = open(pickle_file_name, 'rb')
        pickled = pickle.load(pickle_file)
        for keys in pickled:
            print(keys, "->", pickled[keys])
        pickle_file.close()
        return "Pickle shown above"

    def remove_pickle(self, pickle_file_name):
        os.remove(pickle_file_name)
        return pickle_file_name + " has been deleted"
