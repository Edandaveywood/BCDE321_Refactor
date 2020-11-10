from esprima import parseScript
from graphviz import Digraph, Source
from pickler import Pickler
from ast_visitor import AstVisitor


class Converter:
    def __init__(self):
        self.ast = AstVisitor()
        self.input_file = None
        self._data = None
        self._dict_of_elements = {}

    def load_data(self, input_file):
        self.input_file = input_file
        return input_file

    def extract_data(self):
        file_contents = ""
        try:
            with open(self.input_file, 'r') as f:
                for line in f:
                    file_contents += line
            data = parseScript(file_contents, delegate=self.ast)
            self._data = data
            print('Data has been extracted')
            return self._data
        except Exception as e:
            print('There was an error in the JavaScript file: ' + str(e))

    def get_dict(self):
        self.ast.visit(self._data)
        self._dict_of_elements = AstVisitor.get_dict(self.ast)

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
        s.view()

    def make_pickle(self):
        pickle = Pickler()
        try:
            assert len(self._dict_of_elements.keys()) > 0
            pickle.serialise(self._dict_of_elements)
        except FileNotFoundError as e:
            print(e)
        except AssertionError:
            print('Dictionary is empty, try loading then extracting data first')
