#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-

from cmd import Cmd
from converter import Director, Converter
from json_loader import JsonLoader
from pickler import Pickler
from read_js import ReadJs


class CommandLineInterface(Cmd):

    def __init__(self):
        super().__init__()
        self.prompt = ">>> "
        self.intro = "This program will generate a class diagram from your JavaScript source code. " \
                     "Type help for a list of commands."
        j_loader = JsonLoader('help_file.json')
        j_loader.open_file()
        self.j_loader = j_loader
        self._input_file = None
        self._director = Director()
        self._converter = Converter()
        self._director.con_builder = self._converter
        # self.do_load_data("JSTest2.js")  # test

    def default(self, arg):
        print(arg, 'is an incorrect command, type help to see the command list')

    def do_create_pickle(self, arg):
        self._converter.make_pickle(Pickler())

    def help_create_pickle(self):
        print(self.j_loader.get_help_text('create_pickle'))

    def do_load_pickle(self, arg):
        self._converter.load_pickle(Pickler())

    def help_load_pickle(self):
        print(self.j_loader.get_help_text('load_pickle'))

    def do_remove_pickle(self, arg):
        self._converter.remove_pickle(Pickler())

    def help_remove_pickle(self):
        print(self.j_loader.get_help_text('remove_pickle'))

    def do_exit(self, arg):
        return True

    def help_exit(self):
        print(self.j_loader.get_help_text('exit'))

    def do_load_data(self, arg):
        raw_data = arg.split()
        self._input_file = raw_data[0]
        ReadJs().check_file_type(self._input_file)
        self._converter.load_data(self._input_file)

    def help_load_data(self):
        print(self.j_loader.get_help_text('load_data'))

    def do_extract_data(self, arg):
        self._converter.extract_data()
        self._converter.get_dict()

    def help_extract_data(self):
        print(self.j_loader.get_help_text('extract_data'))

    def do_convert_to_uml(self, arg):
        self._converter.convert_to_uml()
        self._converter.uml.view_uml()

    def help_convert_to_uml(self):
        print(self.j_loader.get_help_text('convert_to_uml'))

    # This is outside the scope of the original tests as
    # I added it for the use of director for a faster UML creation.
    def do_convert_fast(self):
        self._director.build_uml(self._input_file)
        self._converter.uml.view_uml()
