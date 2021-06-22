import sys
from tokenize import tokenize, untokenize

token_list = {
    'ulitin': 'for',
    'ang': 'in',
    'saklaw': 'range',
    'sulat': 'print',
    'tukuyin': 'def',
    'ibalik': 'return',
    'kung': 'if',
    'kundi': 'else',
    'at': 'and',
    'o': 'or',
    'hindi': 'not',
}

filename = sys.argv[1]  # error checking

with open(filename, 'rb') as src:
    tokens = []
    for token in tokenize(src.readline):
        if token.type == 1 and token.string in token_list:
            tokens.append((token.type, token_list[token.string]))
        else:
            tokens.append((token.type, token.string))
# rebuild code from our "modified" tokens
code = untokenize(tokens).decode('utf-8')
exec(code)
