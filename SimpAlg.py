from antlr4 import *
from SimpAlgLexer import SimpAlgLexer
from SimpAlgParser import SimpAlgParser

input_stream = FileStream('example.txt')
lexer = SimpAlgLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = SimpAlgParser(token_stream)

# Execute a análise sintática
tree = parser.start()

