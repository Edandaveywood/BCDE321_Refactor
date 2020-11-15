from esprima import parseScript
from graphviz import Digraph, Source
from pickler import PickleCreator
from ast_visitor import AstVisitor
from abc import ABC, abstractmethod


class ConverterBuilder(ABC):
    @property
    @abstractmethod
    def uml(self):
        """Returns a UML object"""

    @abstractmethod
    def load_data(self, input_file):
        """Loads data from file"""

    @abstractmethod
    def extract_data(self):
        """Extracts loaded data"""

    @abstractmethod
    def get_dict(self):
        """Gets a dictionary of all relevant information"""

    @abstractmethod
    def convert_to_uml(self):
        """Converts UML to a png image"""

    @abstractmethod
    def make_pickle(self, pickle_creator: PickleCreator):
        """"Serialises a pickle"""

    @abstractmethod
    def load_pickle(self, pickle_creator: PickleCreator):
        """"De-serialises a pickle"""

    @abstractmethod
    def remove_pickle(self, pickle_creator: PickleCreator):
        """"Deletes pickle from HDD"""


class Converter(ConverterBuilder):
    def __init__(self):
        self._ast = AstVisitor()
        self._input_file = None
        self._ast_data = None
        self._dict_of_elements = {}
        self.reset()

    def reset(self):
        self._uml = Uml()

    @property
    def uml(self):
        uml = self._uml
        return uml

    def load_data(self, input_file):
        self._input_file = input_file
        self._uml.get_input_file(input_file)

    def extract_data(self):
        file_contents = ""
        try:
            with open(self._input_file, 'r') as f:
                for line in f:
                    file_contents += line
            self._ast_data = parseScript(file_contents, delegate=self._ast)
            print('Data has been extracted')
            self._uml.get_ast_data(self._ast_data)
        except Exception as e:
            print('There was an error in the JavaScript file: ' + str(e))

    def get_dict(self):
        self._ast.visit(self._ast_data)
        self._dict_of_elements = self._ast.get_dict()
        self._uml.get_dict(self._dict_of_elements)

    def convert_to_uml(self):
        dot = Digraph(comment='UML Diagram')
        for key in self._dict_of_elements:
            class_info = self._dict_of_elements.get(key)
            classname = class_info.get('classname')
            methods = class_info.get('classmethod')
            attributes = class_info.get('attributes')
            dot.node(classname,
                     "{{{classname}|{attributes}|{methods}}}".format(
                         classname=classname,
                         attributes="\\l".join(attributes),
                         methods="()\\l".join(methods) + "()"
                     ),
                     shape="record",
                     )
        s = Source(dot.source, filename="test.gv", format="png")
        self._uml.get_uml_source(s)
        print("Conversion complete, opening now")

    def make_pickle(self, pickle_creator: PickleCreator):
        try:
            assert len(self._dict_of_elements.keys()) > 0
            self._uml.get_pickle(pickle_creator.serialise_pickle(self._dict_of_elements, "pickle"))
        except AssertionError:
            print('Dictionary is empty, try loading then extracting data first')

    def load_pickle(self, pickle_creator: PickleCreator):
        self._uml.get_pickle(pickle_creator.de_serialise_pickle("pickle"))

    def remove_pickle(self, pickle_creator: PickleCreator):
        self._uml.get_pickle(pickle_creator.remove_pickle("pickle"))


class Uml:
    def __init__(self):
        self.input_file = None
        self.ast_data = None
        self.dict = None
        self.uml_source = None
        self.pickle = None

    def get_input_file(self, input_file):
        self.input_file = input_file
        # print(self.input_file)

    def get_ast_data(self, ast_data):
        self.ast_data = ast_data
        # print(self.ast_data)

    def get_dict(self, dict_of_elements):
        self.dict = dict_of_elements
        # print(self.dict)

    def get_uml_source(self, uml_source):
        self.uml_source = uml_source
        # print(self.uml_source)

    def get_pickle(self, pickle):
        self.pickle = pickle
        print(self.pickle)

    def view_uml(self):
        return self.uml_source.view()


class Director:
    def __init__(self):
        self._con_builder = None

    @property
    def con_builder(self):
        return self._con_builder

    @con_builder.setter
    def con_builder(self, con_builder: ConverterBuilder):
        self._con_builder = con_builder

    def build_uml(self, input_file):
        self._con_builder.load_data(input_file)
        self._con_builder.extract_data()
        self._con_builder.get_dict()
        self._con_builder.convert_to_uml()
        self._con_builder.make_pickle()
