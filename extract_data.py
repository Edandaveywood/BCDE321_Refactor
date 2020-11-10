#!/usr/local/bin/Python3.6
# -*- coding:utf-8 -*-
import regex
import re,os,sys
import pygraphviz as pgv



A = pgv.AGraph(directed=True, strict=True, rankdir="LR")
# add node 1 with color red
A.add_node(1, color="red")
A.add_node(5, color="blue")
# add some edges
A.add_edge(1, 2, color="green")
A.add_edge(2, 3)
A.add_edge(1, 3)
A.add_edge(3, 4)
A.add_edge(3, 5)
A.add_edge(3, 6)
A.add_edge(4, 6)
# adjust a graph parameter
A.graph_attr["epsilon"] = "0.001"
print(A.string())  # print dot file to standard output
A.layout("dot")  # layout with dot
A.draw("foo.ps")  # write to file

# logfile = sys.argv[1]
# regex = sys.argv[2]

# print(sys.argv, len(sys.argv))
#
# pattern = re.compile(regex)
#
# with open(logfile,"r+") as f:
#     while True:
#         old_offset = f.tell()
#         l = f.readline()
#         if not l:
#             break
#         if pattern.search(l):
#             # match: blank the line
#             new_offset = f.tell()
#             if old_offset > len(os.linesep):
#                 old_offset-=len(os.linesep)
#             f.seek(old_offset)
#             f.write(" "*(new_offset-old_offset-len(os.linesep)))

# with open('/Users/hadooper/PycharmProjects/BCDE321_Assignment2/js-test/throw.js','r') as f:
#     lines = f.readlines()
#     a = ''.join(lines)
#     print(a)
#
#
# with open('/Users/hadooper/PycharmProjects/BCDE321_Assignment2/js-test/throw.js','w') as f:
#    new_value = 'Something New'
#    for line in lines:
#        if line.startswith('hide'):
#            line = 'hide: ["{}"]'.format(new_value)
#        f.write(line)


func_all = []
var_all = []

file1 = open("/Users/hadooper/PycharmProjects/BCDE321_Assignment2/js-test/throw.js").read()
# file1 = open("/Users/hadooper/PycharmProjects/BCDE321_Assignment2/js-test/console-table.js").read()
print("Original output" + '\n' + file1)

# file3 = ' '.join(file1.split())
# print(file3
#       )

# file2 = file1.replace(" ", "")
file2 = re.sub(re.compile("//.*?\n" ) ,"" ,file1).replace(" ", " ")

match = re.search('function(.*)', file1)
whatIWant = match.group(1)
print(whatIWant)

non_comment = re.sub(r'#.*$', "", file2)
print('\n' + "New output" + '\n' + non_comment)

func = re.findall(r"function\s\w+", non_comment, re.S)
var = re.findall(r"var\s\w+", non_comment, re.S)


for i in func:
    j = i.strip('function')
    func_all.append(j)
print(func_all)

for i in var:
    j = i.strip('var')
    var_all.append(j)
print(var_all)


#
# reStr = r"""
#     (                               # capture the non-comment portion
#         "(?:\\.|[^"\\])*"           # capture double quoted strings
#         |
#         '(?:\\.|[^'\\])*'           # capture single quoted strings
#         |
#         (?:[^/\n"']|/[^/*\n"'])+    # any code besides newlines or string literals
#         |
#         \n                          # newline
#     )
#     |
#     (/\*  (?:[^*]|\*[^/])*   \*/)       # /* comment */
#     |
#     (?://(.*)$)                     # // single line comment
#     $"""
#
# reMultiStart = r"""         # start of a multiline comment that doesn't terminate on this line
#     (
#         /\*                 # /*
#         (
#             [^\*]           # any character that is not a *
#             |               # or
#             \*[^/]          # * followed by something that is not a /
#         )*                  # any number of these
#     )
#     $"""
#
# reMultiEnd = r"""           # end of a multiline comment that didn't start on this line
#     (
#         ^                   # start of the line
#         (
#             [^\*]           # any character that is not a *
#             |               # or
#             \*+[^/]         # * followed by something that is not a /
#         )*                  # any number of these
#         \*/                 # followed by a */
#     )
# """

# lines that have single lines comments that start with "// /" are single line comments we should keep
# regExSingleKeep = re.compile("// /")
# regExMain = re.compile(a, re.VERBOSE)
# regExMultiStart = re.compile(reMultiStart, re.VERBOSE)
# regExMultiEnd = re.compile(reMultiEnd, re.VERBOSE)
#
# print(regExMultiEnd)