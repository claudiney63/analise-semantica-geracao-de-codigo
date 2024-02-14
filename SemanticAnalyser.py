from antlr4 import *
from SimpAlgLexer import SimpAlgLexer
from SimpAlgParser import SimpAlgParser
from SimpAlgVisitor import SimpAlgVisitor

class SymbolTable:
    def _init_(self):
        self.variables = {}

    def add_variable(self, name, type):
        self.variables[name] = type

    def variable_exists(self, name):
        return name in self.variables

    def get_variable_type(self, name):
        return self.variables.get(name)

class SemanticAnalyzer(SimpAlgVisitor):
    def _init_(self):
        self.symbol_table = SymbolTable()

    def visitDeclaracao(self, ctx):
        type = ctx.tipo().getText()
        variables = ctx.lista_de_variaveis().ID()
        for variable in variables:
            name = variable.getText()
            if self.symbol_table.variable_exists(name):
                raise Exception(f"Variable '{name}' already declared")
            self.symbol_table.add_variable(name, type)
        return None

    # Implemente outras funções de visitante conforme necessário

# Crie um analisador léxico e um analisador sintático
input_stream = FileStream('example.txt')
lexer = SimpAlgLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = SimpAlgParser(token_stream)

# Execute a análise sintática
tree = parser.programa()

# Crie um analisador semântico e visite a árvore sintática
semantic_analyzer = SemanticAnalyzer()
semantic_analyzer.visit(tree)