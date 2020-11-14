import json


class JsonLoader:

    def __init__(self, path):
        self.__filePath = path
        self.__helpTextDict = None

    def get_help_text(self, name):
        for x in self.__helpTextDict['helpText']:
            if x['functionName'] == name:
                return x['helpText']

    def open_file(self):
        with open(self.__filePath) as f:
            self.__helpTextDict = json.load(f)
