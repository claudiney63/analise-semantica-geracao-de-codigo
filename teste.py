from antlr4 import *
from SimpAlgLexer import SimpAlgLexer
from SimpAlgParser import SimpAlgParser

class SimpAlgVisitor(ParseTreeVisitor):
    def __init__(self):
        self.symbol_table = {}
    #colocar todos os tratamentos de erros
    def visitDeclaracao(self, ctx:SimpAlgParser.DeclaracaoContext):
        tipo = ctx.tipo().getText()
        variaveis = ctx.lista_de_variaveis().ID()
        for variavel in variaveis:
            var_nome = variavel.getText()
            if var_nome in self.symbol_table:
                print(f"Erro semântico: Variável '{var_nome}' já foi declarada.")
            else:
                self.symbol_table[var_nome] = tipo

    def visitAtribuicao(self, ctx:SimpAlgParser.AtribuicaoContext):
        var_nome = ctx.ID().getText()
        if var_nome not in self.symbol_table:
            print(f"Erro semântico: Variável '{var_nome}' não foi declarada antes de ser atribuída.")
        else:
            self.visit(ctx.expressao())

def main():
    input_str = "var { int x } program { x = 10; y = 3.14; print(x, y); }"
    input_stream = InputStream(input_str)
    lexer = SimpAlgLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SimpAlgParser(token_stream)
    tree = parser.programa()

    visitor = SimpAlgVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()