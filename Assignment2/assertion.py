from pysmt.shortcuts import *
from lexer import Lexer, TokenKind, Token


def calculate(tokens):
    postfix_tokens = get_postfix(tokens)
    print('Postfix: ' + str(postfix_tokens))
    return arithmetic(postfix_tokens)


def get_postfix(tokens):
    stack = []
    postfix = []
    print('Tokens: ' + str(tokens))

    i = 0
    while(i < len(tokens)):
        print('Tokens: ' + str(tokens[i+1:]))
        if tokens[i].kind == TokenKind.ID:
            postfix.append(Symbol(tokens[i].text))
            if len(stack) != 0 and stack[-1].kind == TokenKind.NOT:
                postfix.append(stack.pop())
        elif tokens[i].kind == TokenKind.RPAR:
            top = stack.pop()
            while top.kind != TokenKind.LPAR:
                postfix.append(top)
                top = stack.pop()
            if len(stack) != 0 and stack[-1].kind == TokenKind.NOT:
                postfix.append(stack.pop())
        elif tokens[i].kind == TokenKind.LPAR:
            stack.append(tokens[i])
        else:
            p = precedence(tokens[i], stack[-1] if len(stack) != 0 else None)
            while p:
                postfix.append(stack.pop())
                p = precedence(
                    tokens[i], stack[-1] if len(stack) != 0 else None)
            stack.append(tokens[i])
        print('\tStack: ' + str(stack))
        print('\tOutput: ' + str(postfix) + '\n')
        i += 1

    while(len(stack) != 0):
        postfix.append(stack.pop())

    return postfix


def precedence(token, stack_top):
    t = -1
    if token.kind == TokenKind.AND:
        t = 1
    elif token.kind == TokenKind.OR:
        t = 2
    elif token.kind == TokenKind.IMPLIES:
        t = 3
    elif token.kind == TokenKind.IFF:
        t = 4

    s_t = -1
    if stack_top is not None:
        if stack_top.kind == TokenKind.LPAR:
            s_t = 1
        elif stack_top.kind == TokenKind.AND:
            s_t = 2
        elif stack_top.kind == TokenKind.OR:
            s_t = 3
        elif stack_top.kind == TokenKind.IMPLIES:
            s_t = 4
        elif stack_top.kind == TokenKind.IFF:
            s_t = 5
    else:
        return False

    return True if t > s_t else False


def arithmetic(tokens):
    stack = []

    i = 0
    while(i < len(tokens)):
        print('\n' + str(tokens[i:]) + ' -> Token: ' + str(tokens[i]))
        print('Stack: ' + str(stack) + '\n')
        if isinstance(tokens[i], Token):
            if tokens[i].kind == TokenKind.NOT:
                stack.append(Not(stack.pop()))
            elif len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                if tokens[i].kind == TokenKind.AND:
                    stack.append(And(a, b))
                elif tokens[i].kind == TokenKind.OR:
                    stack.append(Or(a, b))
                elif tokens[i].kind == TokenKind.IMPLIES:
                    stack.append(Implies(a, b))
                elif tokens[i].kind == TokenKind.IFF:
                    stack.append(Iff(a, b))
        else:
            print('\t' + str(stack) + ' <- ' + str(tokens[i]))
            stack.append(tokens[i])
        i += 1
    print('Ending Stack: ' + str(stack[-1]))
    if len(stack) == 1:
        return is_sat(stack[-1])
    else:
        raise NotImplementedError
