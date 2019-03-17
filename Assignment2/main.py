import unittest
import os
from lexer import Lexer, TokenKind
from assertion import *

# access input file
dir_path = os.path.dirname(__file__)
file_name = 'input.txt'
input_file_path = os.path.join(dir_path, file_name)
f_lines = ['']
with open(input_file_path) as f:
    c = f.read(1)
    i = 0
    while c:
        if c != '\n':
            f_lines[i] += c
        elif c == '\n':
            f_lines.append('')
            i += 1
        c = f.read(1)
    # f_str = f.read()


class Test(unittest.TestCase):
    def test(self):
        tokenlists = []
        for i, line in enumerate(f_lines):
            if line.strip():
                tokenlists.append(Lexer(line, i+1).tokenize())

        output_file_path = os.path.join(dir_path, 'output.txt')
        with open(output_file_path, 'w') as f:
            for i, tokens in enumerate(tokenlists):
                print(calculate(tokens))

        with open(output_file_path, 'r') as f:
            print(f.read())

if __name__ == '__main__':
    unittest.main()
