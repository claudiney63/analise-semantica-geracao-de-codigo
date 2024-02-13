# Generated from SimpAlg.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SimpAlgParser import SimpAlgParser
else:
    from SimpAlgParser import SimpAlgParser

# This class defines a complete listener for a parse tree produced by SimpAlgParser.
class SimpAlgListener(ParseTreeListener):

    # Enter a parse tree produced by SimpAlgParser#programa.
    def enterPrograma(self, ctx:SimpAlgParser.ProgramaContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#programa.
    def exitPrograma(self, ctx:SimpAlgParser.ProgramaContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#declaracoes.
    def enterDeclaracoes(self, ctx:SimpAlgParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#declaracoes.
    def exitDeclaracoes(self, ctx:SimpAlgParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#declaracao.
    def enterDeclaracao(self, ctx:SimpAlgParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#declaracao.
    def exitDeclaracao(self, ctx:SimpAlgParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#tipo.
    def enterTipo(self, ctx:SimpAlgParser.TipoContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#tipo.
    def exitTipo(self, ctx:SimpAlgParser.TipoContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#comandos.
    def enterComandos(self, ctx:SimpAlgParser.ComandosContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#comandos.
    def exitComandos(self, ctx:SimpAlgParser.ComandosContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#comando.
    def enterComando(self, ctx:SimpAlgParser.ComandoContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#comando.
    def exitComando(self, ctx:SimpAlgParser.ComandoContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#atribuicao.
    def enterAtribuicao(self, ctx:SimpAlgParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#atribuicao.
    def exitAtribuicao(self, ctx:SimpAlgParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#saida.
    def enterSaida(self, ctx:SimpAlgParser.SaidaContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#saida.
    def exitSaida(self, ctx:SimpAlgParser.SaidaContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#entrada.
    def enterEntrada(self, ctx:SimpAlgParser.EntradaContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#entrada.
    def exitEntrada(self, ctx:SimpAlgParser.EntradaContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#condicional.
    def enterCondicional(self, ctx:SimpAlgParser.CondicionalContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#condicional.
    def exitCondicional(self, ctx:SimpAlgParser.CondicionalContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#repeticao.
    def enterRepeticao(self, ctx:SimpAlgParser.RepeticaoContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#repeticao.
    def exitRepeticao(self, ctx:SimpAlgParser.RepeticaoContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#expressao.
    def enterExpressao(self, ctx:SimpAlgParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#expressao.
    def exitExpressao(self, ctx:SimpAlgParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#termo.
    def enterTermo(self, ctx:SimpAlgParser.TermoContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#termo.
    def exitTermo(self, ctx:SimpAlgParser.TermoContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#fator.
    def enterFator(self, ctx:SimpAlgParser.FatorContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#fator.
    def exitFator(self, ctx:SimpAlgParser.FatorContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#expressao_logica.
    def enterExpressao_logica(self, ctx:SimpAlgParser.Expressao_logicaContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#expressao_logica.
    def exitExpressao_logica(self, ctx:SimpAlgParser.Expressao_logicaContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#or_expr.
    def enterOr_expr(self, ctx:SimpAlgParser.Or_exprContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#or_expr.
    def exitOr_expr(self, ctx:SimpAlgParser.Or_exprContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#and_expr.
    def enterAnd_expr(self, ctx:SimpAlgParser.And_exprContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#and_expr.
    def exitAnd_expr(self, ctx:SimpAlgParser.And_exprContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#relacional.
    def enterRelacional(self, ctx:SimpAlgParser.RelacionalContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#relacional.
    def exitRelacional(self, ctx:SimpAlgParser.RelacionalContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#lista_de_valores.
    def enterLista_de_valores(self, ctx:SimpAlgParser.Lista_de_valoresContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#lista_de_valores.
    def exitLista_de_valores(self, ctx:SimpAlgParser.Lista_de_valoresContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#lista_de_variaveis.
    def enterLista_de_variaveis(self, ctx:SimpAlgParser.Lista_de_variaveisContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#lista_de_variaveis.
    def exitLista_de_variaveis(self, ctx:SimpAlgParser.Lista_de_variaveisContext):
        pass


    # Enter a parse tree produced by SimpAlgParser#op_unario.
    def enterOp_unario(self, ctx:SimpAlgParser.Op_unarioContext):
        pass

    # Exit a parse tree produced by SimpAlgParser#op_unario.
    def exitOp_unario(self, ctx:SimpAlgParser.Op_unarioContext):
        pass



del SimpAlgParser