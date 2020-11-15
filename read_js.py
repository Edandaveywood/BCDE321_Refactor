#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-
import os


class ReadJs:

    # Jacks work, Edan's try, assert/excepts
    def check_file_type(self, input_file):
        if os.path.exists(input_file):
            if os.path.isfile(input_file):
                work_dir = os.path.dirname(input_file)
                file = input_file[len(work_dir):]
                try:
                    assert file.endswith('.js')
                    print("The current directory is: " + work_dir + "\n" +
                          "Your selected js file is: " + file)
                except AssertionError:
                    print(input_file + " is not a js file, please re-select")
                    return
        else:
            print("You did not input any path or your input file is not existed")

