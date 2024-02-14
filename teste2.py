from antlr4 import *
from SimpAlgLexer import SimpAlgLexer
from SimpAlgParser import SimpAlgParser

class SymbolTableVisitor(ParseTreeVisitor):
    def __init__(self):
        self.symbol_table = {}

    def visitDeclaracao(self, ctx: SimpAlgParser.DeclaracaoContext):
        tipo = ctx.tipo().getText()
        variaveis = ctx.lista_de_variaveis().ID()
        
        # Verifica se é um único token
        if isinstance(variaveis, Token):
            var_nome = variaveis.getText()
            if var_nome in self.symbol_table:
                print(f"Erro semântico: Variável '{var_nome}' já foi declarada.")
            else:
                self.symbol_table[var_nome] = tipo
        else:
            # Se não for um único token, é necessário ajustar a lógica de iteração
            for variavel in variaveis:
                var_nome = variavel.getText()
                if var_nome in self.symbol_table:
                    print(f"Erro semântico: Variável '{var_nome}' já foi declarada.")
                else:
                    self.symbol_table[var_nome] = tipo


def main():
    input_str = "var { int x, float y } program { x = 10; y = 3.14; print(x, y); }"
    input_stream = InputStream(input_str)
    lexer = SimpAlgLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SimpAlgParser(token_stream)
    tree = parser.programa()

    # Instancia o visitor da tabela de símbolos
    symbol_table_visitor = SymbolTableVisitor()
    
    # Visita a árvore sintática para construir a tabela de símbolos
    symbol_table_visitor.visit(tree)

    # Imprime a tabela de símbolos
    print("Tabela de Símbolos:")
    for var, tipo in symbol_table_visitor.symbol_table.items():
        print(f"{var}: {tipo}")

if __name__ == '__main__':
    main()
