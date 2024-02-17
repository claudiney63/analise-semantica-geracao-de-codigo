# Generated from SimpAlg.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SimpAlgParser import SimpAlgParser
else:
    from SimpAlgParser import SimpAlgParser

from SemanticAnalyser import *
from CodeGenerator import *


# This class defines a complete generic visitor for a parse tree produced by SimpAlgParser.

class SimpAlgVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpAlgParser#start.
    def visitStart(self, ctx:SimpAlgParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#var.
    def visitVar(self, ctx:SimpAlgParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#program.
    def visitProgram(self, ctx:SimpAlgParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#declaracoes.
    def visitDeclaracoes(self, ctx:SimpAlgParser.DeclaracoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#declaracao.
    def visitDeclaracao(self, ctx:SimpAlgParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#lista_de_declaracao.
    def visitLista_de_declaracao(self, ctx:SimpAlgParser.Lista_de_declaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#tipo.
    def visitTipo(self, ctx:SimpAlgParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#comandos.
    def visitComandos(self, ctx:SimpAlgParser.ComandosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#comando.
    def visitComando(self, ctx:SimpAlgParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#atribuicao.
    def visitAtribuicao(self, ctx:SimpAlgParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#expressao.
    def visitExpressao(self, ctx:SimpAlgParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#op_unario.
    def visitOp_unario(self, ctx:SimpAlgParser.Op_unarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#termo.
    def visitTermo(self, ctx:SimpAlgParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#fator.
    def visitFator(self, ctx:SimpAlgParser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#saida.
    def visitSaida(self, ctx:SimpAlgParser.SaidaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#lista_de_valores.
    def visitLista_de_valores(self, ctx:SimpAlgParser.Lista_de_valoresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#entrada.
    def visitEntrada(self, ctx:SimpAlgParser.EntradaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#lista_de_variaveis.
    def visitLista_de_variaveis(self, ctx:SimpAlgParser.Lista_de_variaveisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#condicional.
    def visitCondicional(self, ctx:SimpAlgParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#repeticao.
    def visitRepeticao(self, ctx:SimpAlgParser.RepeticaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#expressao_logica.
    def visitExpressao_logica(self, ctx:SimpAlgParser.Expressao_logicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#or_expr.
    def visitOr_expr(self, ctx:SimpAlgParser.Or_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#and_expr.
    def visitAnd_expr(self, ctx:SimpAlgParser.And_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#relacional.
    def visitRelacional(self, ctx:SimpAlgParser.RelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpAlgParser#terminal.
    def visitTerminal(self, ctx:SimpAlgParser.TerminalContext):
        return self.visitChildren(ctx)



del SimpAlgParser