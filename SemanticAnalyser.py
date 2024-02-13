from antlr4 import *
from SimpAlgLexer import SimpAlgLexer
from SimpAlgParser import SimpAlgParser

class SimpAlgVisitor(ParseTreeVisitor):
    def __init__(self):
        self.symbol_table = {}
        self.current_scope = []

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
            tipo_var = self.symbol_table[var_nome]
            tipo_expr = self.visit(ctx.expressao())
            if tipo_var != tipo_expr:
                print(f"Erro semântico: Atribuição de tipo inválida para variável '{var_nome}'.")

    def visitCondicional(self, ctx:SimpAlgParser.CondicionalContext):
        tipo_condicao = self.visit(ctx.expressao_logica())
        if tipo_condicao != 'bool':
            print("Erro semântico: A condição do condicional deve ser do tipo booleano.")

        self.visit(ctx.comandos(0))  # Visitando o bloco de comandos do if
        if ctx.comandos(1):  # Se houver bloco else
            self.visit(ctx.comandos(1))  # Visitando o bloco de comandos do else

    def visitRepeticao(self, ctx:SimpAlgParser.RepeticaoContext):
        tipo_condicao = self.visit(ctx.expressao_logica())
        if tipo_condicao != 'bool':
            print("Erro semântico: A condição da repetição deve ser do tipo booleano.")
        
        self.visit(ctx.comandos())  # Visitando o bloco de comandos dentro da repetição

    def visitSaida(self, ctx:SimpAlgParser.SaidaContext):
        tipos_valores = self.visit(ctx.lista_de_valores())
        for tipo_valor in tipos_valores:
            if tipo_valor not in ['int', 'float']:
                print("Erro semântico: A saída só aceita valores inteiros ou float.")

    def visitEntrada(self, ctx:SimpAlgParser.EntradaContext):
        variaveis = ctx.lista_de_variaveis().ID()
        for variavel in variaveis:
            var_nome = variavel.getText()
            if var_nome not in self.symbol_table:
                print(f"Erro semântico: Variável '{var_nome}' não foi declarada antes de ser usada na entrada.")

    def visitOp_unario(self, ctx:SimpAlgParser.Op_unarioContext):
        return ctx.getText()  # Retorna o operador unário

    # Métodos de visita para outras regras semânticas

def main():
    input_str = "var { int x } program { if (x > 0) { print(x); } else { print(-x); } }"  
    input_stream = InputStream(input_str)  
    lexer = SimpAlgLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SimpAlgParser(token_stream)
    tree = parser.programa()

    visitor = SimpAlgVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()
