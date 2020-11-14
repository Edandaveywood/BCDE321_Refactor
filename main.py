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
        jloader = JsonLoader('help_file.json')
        try:
            jloader.open_file()
        except FileNotFoundError:
            print('There is no help file.')
        self.jloader = jloader
        self._input_file = None
        self._director = Director()
        self._converter = Converter()
        self._director.conbuilder = self._converter
        # self.do_load_data("JSTest2.js")  # test

    def default(self, arg):
        print(arg, 'is an incorrect command, type help to see the command list')

    def do_create_pickle(self, arg):
        self._converter.make_pickle(Pickler())

    def help_create_pickle(self):
        print(self.jloader.get_help_text('create_pickle'))

    def do_load_pickle(self, arg):
        self._converter.load_pickle(Pickler())

    def do_remove_pickle(self, arg):
        self._converter.remove_pickle(Pickler())

    def do_exit(self, arg):
        return True

    def help_exit(self):
        print(self.jloader.get_help_text('exit'))

    def do_load_data(self, arg):
        try:
            raw_data = arg.split()
            self._input_file = raw_data[0]
            ReadJs().check_file_type(self._input_file)
            self._converter.load_data(self._input_file)
        except Exception as e:
            print(e)

    def help_load_data(self):
        print(self.jloader.get_help_text('load_data'))

    def do_extract_data(self, arg):
        try:
            self._converter.extract_data()
            self._converter.get_dict()
        except Exception as e:
            print(e)

    def help_extract_data(self):
        print(self.jloader.get_help_text('extract_data'))

    def do_convert_to_uml(self, arg):
        try:
            self._converter.convert_to_uml()
            self._converter.uml.view_uml()
        except Exception as e:
            print(e)

    def help_convert_to_uml(self):
        print(self.jloader.get_help_text('convert_to_uml'))

    # This is outside the scope of the original tests as I added it for the use of director for a faster UML creation.
    def do_convert_fast(self):
        self._director.build_uml(self._input_file)
        self._converter.uml.view_uml()


if __name__ == '__main__':
    import sys

    cli = CommandLineInterface()
    sys_exit_code = cli.cmdloop()
    sys.exit(sys_exit_code)
