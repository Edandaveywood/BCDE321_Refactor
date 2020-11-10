#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-


# Jack imports
import asyncio
import os
import subprocess
from read_js import Read_js
from mysql import main1, main2, main3, main4, main5

# Edan imports
from cmd import Cmd
from converter import Converter
from json_loader import JsonLoader

os.environ["PATH"] += os.pathsep + './wavi-master/bin'
dir_path = os.path.dirname(os.path.realpath(__file__))
wavi_path = os.path.join(dir_path, "wavi-master/bin")
dot_path = os.path.join(dir_path, "Graphviz 2.44.1/bin")
os.environ["PATH"] += os.pathsep + wavi_path + dot_path

class CommandLineInterface(Cmd):

    def __init__(self):
        super().__init__()
        self.con = Converter()
        self.prompt = ">>> "
        self.intro = "This program will generate a class diagram from your JavaScript source code. " \
                     "Type help for a list of commands."
        jloader = JsonLoader('help_file.json')
        # self.do_load_data("JSTest2.js")  # test
        try:
            jloader.open_file()
        except FileNotFoundError:
            print('There is no help file.')
        self.jloader = jloader

    def default(self, arg):
        print(arg, 'is an incorrect command, type help to see the command list')

    def do_create_pickle(self, arg):
        self.con.make_pickle()

    def help_create_pickle(self):
        print(self.jloader.get_help_text('create_pickle'))

    def do_exit(self, arg):
        return True

    def help_exit(self):
        print(self.jloader.get_help_text('exit'))

    def do_load_data(self, arg):
        try:
            raw_data = arg.split()
            input_file = raw_data[0]
            Read_js().check_file_type(input_file)

            self.con.load_data(input_file)

        except IndexError:
            print(f'You should follow the format, please try "help load_data" to find the use.')

        except Exception as e:
            print(e)

    def help_load_data(self):
        print(self.jloader.get_help_text('load_data'))

    def do_extract_data(self, arg):
        try:
            self.con.visit(self.con.extract_data(self.con))
        except Exception as e:
            print(e)

    def help_extract_data(self):
        print(self.jloader.get_help_text('extract_data'))

    def do_convert_to_uml(self, arg):
        try:
            self.con.convert_to_uml()

        except Exception as e:
            print(e)

    def help_convert_to_uml(self):
        print(self.jloader.get_help_text('convert_to_uml'))

    # Jack uncompleted coding
    def do_read_js(self, arg):
        chk = Read_js()
        chk.check_file_type(arg)

    def help_read_js(self):
        print(self.jloader.get_help_text('read_js'))

    def do_pwd(self, arg):
        print(os.getcwd())

    def help_pwd(self):
        print(self.jloader.get_help_text('pwd'))

    def do_db_connect(self, arg):
        loop = asyncio.get_event_loop()
        try:
            result = loop.run_until_complete(main1())
            print(result)
        except Exception as e:
            print(e)

    def help_db_connect(self):
        print(self.jloader.get_help_text('db_connect'))

    def do_db_info(self, arg):
        loop = asyncio.get_event_loop()
        try:
            result = loop.run_until_complete(main3())
            print(result)
        except Exception as e:
            print(e)

    def help_db_info(self):
        print(self.jloader.get_help_text('db_info'))

    def do_table_select(self, arg):

        try:
            raw_data = arg.split()
            db = raw_data[0]

            loop = asyncio.get_event_loop()

            if db == '-a':
                result = loop.run_until_complete(main5())
                print(result)
            elif db == '-m':
                result = loop.run_until_complete(main4())
                print(result)
            elif db == '-i':
                result = loop.run_until_complete(main2())
                print(result)
            else:
                print(f'The table you choose is not existed in the database, please try "db_connect" to check the existed tables')
        except Exception as e:
            print(e)

    def help_table_select(self):
        print(self.jloader.get_help_text('table_select'))

    # def do_cls_info_select_all(self, arg):
    #     loop = asyncio.get_event_loop()
    #     try:
    #         result = loop.run_until_complete(main2())
    #         print(result)
    #     except Exception as e:
    #         print(e)

    # def do_cls_mtd_select_all(self, arg):
    #     loop = asyncio.get_event_loop()
    #     try:
    #         result = loop.run_until_complete(main4())
    #         print(result)
    #     except Exception as e:
    #         print(e)

    # def do_cls_atr_select_all(self, arg):
    #     loop = asyncio.get_event_loop()
    #     try:
    #         result = loop.run_until_complete(main5())
    #         print(result)
    #     except Exception as e:
    #         print(e)

    def do_wavi(self, arg):
        try:
            raw_data = arg.split()
            input_file = raw_data[0]

            command = "wavi {0} uml-test.svg".format(input_file)
            print("Your wavi directory is: " + wavi_path)
            subprocess.run(command, cwd=dir_path, shell=True)

        except Exception as e:
            print(e)

    def help_wavi(self):
        print(self.jloader.get_help_text('wavi'))



if __name__ == '__main__':
    import sys

    cli = CommandLineInterface()
    sys_exit_code = cli.cmdloop()
    print('Exiting with code: {!r}'.format(sys_exit_code))
    sys.exit(sys_exit_code)
