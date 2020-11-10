#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-
import os
import re


class Read_js:

    def __init__(self):
        self._fucntion_name = []
        self._var_name = []

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
                    # return "The current directory is: " + work_dir + "\n" + \
                    #        "Your selected js file is: " + file
                except AssertionError:
                    print(input_file + " is not a js file, please re-select")
                    return
            except AssertionError:
                print("You might select a wrong path(i.e. a directory path), " 
                      "please re-enter a path of the js file you want to input")
                return
        else:
            print("You did not input any path or your input file is not existed")

    def get_data(self, input_file):
        function_all = []
        var_all = []
        source = open(input_file).read()
        # print("Original output" + '\n' + source)
        # test1 = ' '.join(source.split())
        # test2 = re.sub(re.compile("//.*?\n"), "", test1)
        # print(source)

        function = re.findall(r'function\s\w+', source, re.S) + re.findall(r'function\s\w+', source, re.S)
        var = re.findall(r'var\s\w+', source, re.S) + re.findall(r'const\s\w+', source, re.S) + re.findall(r'let\s\w+', source, re.S)


        for obj in function:
            function_all.append(obj.lstrip('function'))


        for obj in var:
            var_all.append(re.sub('var|const|let| ', '', obj))
            # var_all.append(obj.lstrip('var' or 'const' or 'let'))
        print(var_all + '\n' + function_all)


        # file1 = open("/Users/hadooper/PycharmProjects/BCDE321_Assignment2/js-test/throw.js").read()
        # file1 = open("/Users/hadooper/PycharmProjects/BCDE321_Assignment2/js-test/console-table.js").read()
        # print("Original output" + '\n' + file1)

        # file3 = ' '.join(file1.split())
        # print(file3)

        # file2 = file1.replace(" ", "")
        # file2 = re.sub(re.compile("//.*?\n"), "", file1).replace(" ", " ")
        #
        # match = re.search('function(.*)', file1)
        # whatIWant = match.group(1)
        # print(whatIWant)
        #
        # non_comment = re.sub(r'#.*$', "", file2)
        # print('\n' + "New output" + '\n' + non_comment)
        #
        # func = re.findall(r"function\s\w+", non_comment, re.S)
        # var = re.findall(r"var\s\w+", non_comment, re.S)
        #
        # for i in func:
        #     j = i.strip('function')
        # func_all.append(j)
        # print(func_all)
        #
        # for i in var:
        #     j = i.strip('var')
        # var_all.append(j)
        # print(var_all)


# if __name__ == '__main__':
#     a = Read_js()
#     a.check_file_type("/Users/hadooper/PycharmProjects/BCDE321_Assignment2/js-test/breakpoints.js")
#     a.check_file_type("/Users/hadooper/PycharmProjects/BCDE321_Assignment2/js-test/breakpoints.mp3")
#     a.check_file_type("/Users/hadooper/PycharmProjects/BCDE321_Assignment2/js-test/")
#     a.check_file_type("/Users/hadooper/PycharmProjects/BCDE321_Assignment2/Bar.py")
#     # a.check_file_type("JStest1.js")
#
    # print("=" * 100)
    # a.get_data("/Users/hadooper/PycharmProjects/BCDE321_Assignment2/JStest1.js")
    #
    # a.get_data("/Users/hadooper/PycharmProjects/BCDE321_Assignment2/js-test/throw.js")


