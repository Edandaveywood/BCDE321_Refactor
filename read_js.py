#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-
import os


class ReadJs:
    # Jacks work, Edan's try, assert/excepts
    def check_file_type(self, input_file):
        if os.path.exists(input_file):
            try:
                assert os.path.isfile(input_file)
                work_dir = os.path.dirname(input_file)
                if input_file.startswith('/'):
                    file = input_file[len(work_dir)+1:]
                else:
                    file = input_file[len(work_dir):]
                try:
                    assert file.endswith('.js')
                    print("The current directory is: " + work_dir + "\n" +
                          "Your selected js file is: " + file)
                except AssertionError:
                    print(input_file + " is not a js file, please re-select")
                    return
            except AssertionError:
                print("You might select a wrong path(i.e. a directory path), " 
                      "please re-enter a path of the js file you want to input")
                return
        else:
            print("You did not input any path or your input file is not existed")
