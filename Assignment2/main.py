import unittest
import os
from lexer import Lexer, TokenKind
from parser import Parser
from assertion import *
from pprint import pprint

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
                f.write('Input #' + str(i+1) + ':')
                f.write('\n---------')
                f.write('\nProposition\t\t\t: ')
                f.write(f_lines[i].replace('\'', ''))
                lexer_output = str(tokens).replace('\'', '')
                if tokens[0].kind is not None:
                    f.write('\nLexer\t\t\t\t: ')
                    f.write(lexer_output.replace('[', '[ ').replace(']', ' ]'))
                    try:
                        parse_tree = Parser(tokens[:]).parse()
                        f.write('\nParser\t\t\t\t: ')
                        f.write(str(parse_tree).replace('\'', ''))
                        
                        more_propositions = []
                        i = 0
                        for j, token in enumerate(tokens):
                            if token.kind == TokenKind.COMMA:
                                more_propositions.append(
                                    [Token(None, TokenKind.LPAR, 'LPAR')] +
                                    tokens[i:j] +
                                    [Token(None, TokenKind.RPAR, 'RPAR')])
                                i = j+1
                        more_propositions.append(
                            [Token(None, TokenKind.LPAR, 'LPAR')] +
                            tokens[i:] +
                            [Token(None, TokenKind.RPAR, 'RPAR')])
                        pprint(str(more_propositions).replace('\'', ''))
                        
                        new_tokens = []
                        for i, row in enumerate(more_propositions):
                            new_tokens += row
                            if i+1 != len(more_propositions):
                                new_tokens += [Token(None, TokenKind.AND, 'AND')]
                        pprint(str(new_tokens).replace('\'', ''))

                        s = calculate(new_tokens)
                        f.write('\nis_sat\t\t\t\t: ' + str(s))
                    except Exception as e:
                        f.write('\nParserSyntaxError(s)\t\t: ' + str(e))
                else:
                    f.write('\nSyntaxError(s)\t\t: ')
                    for i, invalidToken in enumerate(tokens):
                        f.write(
                            str(invalidToken) +
                            ' (line ' +
                            str(invalidToken.loc.line) +
                            ', col ' +
                            str(invalidToken.loc.col) + ')')
                        if i+1 != len(tokens):
                            f.write(' | ')
                if len(tokenlists)-1 != i:
                    f.write('\n\n')

        with open(output_file_path, 'r') as f:
            print(f.read())

if __name__ == '__main__':
    unittest.main()
