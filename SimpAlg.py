from antlr4 import *
from output_dir.SimpAlgLexer import SimpAlgLexer
from output_dir.SimpAlgParser import SimpAlgParser

input_stream = FileStream('example.txt')
lexer = SimpAlgLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = SimpAlgParser(token_stream)

# Execute a análise sintática
tree = parser.start()