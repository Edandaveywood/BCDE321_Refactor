from esprima import NodeVisitor


class AstVisitor(NodeVisitor):
    def __init__(self):
        self._operator = []
        self._obj_type = []
        self._prop_name = []
        self._right_ele = []
        self._class_names = []
        self._class_methods = []
        self._attributes = []
        self._dict_of_elements = {}
        self._index = 0

    def visit_ClassDeclaration(self, node):
        self._class_names.append(node.id.name)
        self.generic_visit(node)

    def is_constructor(self, node):
        result = False
        if node.key.name == 'constructor':
            result = True
        return result

    def visit_MethodDefinition(self, node):
        if self.is_constructor(node):
            self._class_methods = []
            self._attributes = []
            self._index += 1
            body = node.value.body.body
            self.set_class_attributes(body)
        self._class_methods.append(node.key.name)
        class_values = {
            'classname': self._class_names[self._index - 1],
            'classmethod': self._class_methods,
            'attributes': self._attributes
        }
        class_num = "class" + str(self._index)
        self._dict_of_elements[class_num] = class_values

    def set_class_attributes(self, body):
        for key in body:
            expr = key.expression
            result = 'this.'
            if expr.left is not None:
                result += expr.left.property.name
            result += expr.operator
            if expr.right.type == 'ArrayExpression':
                result += str(expr.right.elements)
            elif expr.right.type == 'Literal':
                result += expr.right.raw
            else:
                result += expr.right.name
            self._attributes.append(result)

    def get_dict(self):
        return self._dict_of_elements
