from antlr4 import *
from output_dir.SimpAlgLexer import SimpAlgLexer
from output_dir.SimpAlgParser import SimpAlgParser
from antlr4.error.ErrorListener import ConsoleErrorListener

class MyErrorListener(ConsoleErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Erro sintático na linha {line}: {msg}")
        # Adicione o código para abortar a análise ou lidar com o erro conforme necessário
        recognizer.hasError = True


input_stream = FileStream('example.txt')
lexer = SimpAlgLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = SimpAlgParser(token_stream)

parser.removeErrorListeners()
parser.addErrorListener(MyErrorListener())

# Execute a análise sintática
# tree = parser.start()

try:
    tree = parser.start()
    # Realize as ações semânticas e a geração de código aqui
except RecognitionException as e:
    print(f"Erro léxico ou sintático: {e}")