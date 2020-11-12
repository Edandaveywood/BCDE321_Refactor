from esprima import parseScript
from graphviz import Digraph, Source
from pickler import Pickler
from ast_visitor import AstVisitor
from abc import ABC, abstractmethod


class ConverterBuilder(ABC):
    @property
    @abstractmethod
    def uml(self):
        pass

    @abstractmethod
    def load_data(self, input_file):
        pass

    @abstractmethod
    def extract_data(self):
        pass

    @abstractmethod
    def get_dict(self):
        pass

    @abstractmethod
    def convert_to_uml(self):
        pass

    @abstractmethod
    def make_pickle(self):
        pass


class Converter(ConverterBuilder):
    def __init__(self):
        self.ast = AstVisitor()
        self.input_file = None
        self.astdata = None
        self._dict_of_elements = {}
        self.reset()

    def reset(self):
        self._uml = Uml()

    @property
    def uml(self):
        uml = self._uml
        return uml

    def load_data(self, input_file):
        self.input_file = input_file
        self._uml.get_input_file(input_file)

    def extract_data(self):
        file_contents = ""
        try:
            with open(self.input_file, 'r') as f:
                for line in f:
                    file_contents += line
            self.astdata = parseScript(file_contents, delegate=self.ast)
            print('Data has been extracted')
            self._uml.get_ast_data(self.astdata)
        except Exception as e:
            print('There was an error in the JavaScript file: ' + str(e))

    def get_dict(self):
        self.ast.visit(self.astdata)
        self._dict_of_elements = self.ast.get_dict()
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

    def make_pickle(self):
        pickle = Pickler()
        try:
            assert len(self._dict_of_elements.keys()) > 0
            pickle.serialise(self._dict_of_elements, "pickle")
            self._uml.get_pickle(pickle.serialise(self._dict_of_elements, "pickle"))
        except FileNotFoundError as e:
            print(e)
        except AssertionError:
            print('Dictionary is empty, try loading then extracting data first')

    def load_pickle(self):
        pickle = Pickler()
        try:
            pickle.de_serialise()
        except FileNotFoundError as e:
            print(e)

    def remove_pickle(self):
        pickle = Pickler()
        try:
            pickle.remove_pickle()
        except FileNotFoundError as e:
            print(e)


class Uml:
    def __init__(self):
        self.input_file = None
        self.astdata = None
        self.dict = None
        self.umlsource = None
        self.pickle = None

    def get_input_file(self, input_file):
        self.input_file = input_file
        # print(self.input_file)

    def get_ast_data(self, astdata):
        self.astdata = astdata
        # print(self.astdata)

    def get_dict(self, dict_of_elements):
        self.dict = dict_of_elements
        # print(self.dict)

    def get_uml_source(self, umlsource):
        self.umlsource = umlsource
        # print(self.umlsource)

    def get_pickle(self, pickle):
        self.pickle = pickle
        print(self.pickle)

    def view_uml(self):
        return self.umlsource.view()


class Director:
    def __init__(self):
        self._conbuilder = None

    @property
    def conbuilder(self):
        return self._conbuilder

    @conbuilder.setter
    def conbuilder(self, conbuilder: ConverterBuilder):
        self._conbuilder = conbuilder

    def build_uml(self, input_file):
        self._conbuilder.load_data(input_file)
        self._conbuilder.extract_data()
        self._conbuilder.get_dict()
        self._conbuilder.convert_to_uml()
        self._conbuilder.make_pickle()
