# Generated from SimpAlg.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,229,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,4,1,53,8,1,11,1,12,
        1,54,1,2,1,2,1,2,1,2,1,3,1,3,1,4,4,4,64,8,4,11,4,12,4,65,1,5,1,5,
        1,5,1,5,1,5,3,5,73,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,3,9,104,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        11,1,11,1,11,5,11,117,8,11,10,11,12,11,120,9,11,1,11,1,11,1,11,3,
        11,125,8,11,1,12,1,12,1,12,5,12,130,8,12,10,12,12,12,133,9,12,1,
        12,1,12,1,12,5,12,138,8,12,10,12,12,12,141,9,12,3,12,143,8,12,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,152,8,13,1,14,1,14,1,14,1,
        14,1,14,3,14,159,8,14,1,15,1,15,1,15,1,15,3,15,165,8,15,1,15,1,15,
        1,15,5,15,170,8,15,10,15,12,15,173,9,15,1,16,1,16,1,16,1,16,3,16,
        179,8,16,1,16,1,16,1,16,5,16,184,8,16,10,16,12,16,187,9,16,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,3,17,196,8,17,1,17,1,17,1,17,3,17,
        201,8,17,1,17,1,17,1,17,5,17,206,8,17,10,17,12,17,209,9,17,1,18,
        1,18,1,18,5,18,214,8,18,10,18,12,18,217,9,18,1,19,1,19,1,19,5,19,
        222,8,19,10,19,12,19,225,9,19,1,20,1,20,1,20,0,3,30,32,34,21,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,0,8,1,0,6,
        7,1,0,16,17,1,0,18,19,1,0,31,32,1,0,21,22,1,0,31,33,1,0,24,29,1,
        0,31,34,233,0,42,1,0,0,0,2,52,1,0,0,0,4,56,1,0,0,0,6,60,1,0,0,0,
        8,63,1,0,0,0,10,72,1,0,0,0,12,74,1,0,0,0,14,79,1,0,0,0,16,85,1,0,
        0,0,18,91,1,0,0,0,20,105,1,0,0,0,22,124,1,0,0,0,24,142,1,0,0,0,26,
        151,1,0,0,0,28,158,1,0,0,0,30,160,1,0,0,0,32,174,1,0,0,0,34,200,
        1,0,0,0,36,210,1,0,0,0,38,218,1,0,0,0,40,226,1,0,0,0,42,43,5,1,0,
        0,43,44,5,2,0,0,44,45,3,2,1,0,45,46,5,3,0,0,46,47,5,4,0,0,47,48,
        5,2,0,0,48,49,3,8,4,0,49,50,5,3,0,0,50,1,1,0,0,0,51,53,3,4,2,0,52,
        51,1,0,0,0,53,54,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,3,1,0,0,
        0,56,57,3,6,3,0,57,58,3,38,19,0,58,59,5,5,0,0,59,5,1,0,0,0,60,61,
        7,0,0,0,61,7,1,0,0,0,62,64,3,10,5,0,63,62,1,0,0,0,64,65,1,0,0,0,
        65,63,1,0,0,0,65,66,1,0,0,0,66,9,1,0,0,0,67,73,3,12,6,0,68,73,3,
        14,7,0,69,73,3,16,8,0,70,73,3,18,9,0,71,73,3,20,10,0,72,67,1,0,0,
        0,72,68,1,0,0,0,72,69,1,0,0,0,72,70,1,0,0,0,72,71,1,0,0,0,73,11,
        1,0,0,0,74,75,5,31,0,0,75,76,5,8,0,0,76,77,3,22,11,0,77,78,5,5,0,
        0,78,13,1,0,0,0,79,80,5,9,0,0,80,81,5,10,0,0,81,82,3,36,18,0,82,
        83,5,11,0,0,83,84,5,5,0,0,84,15,1,0,0,0,85,86,5,12,0,0,86,87,5,10,
        0,0,87,88,3,38,19,0,88,89,5,11,0,0,89,90,5,5,0,0,90,17,1,0,0,0,91,
        92,5,13,0,0,92,93,5,10,0,0,93,94,3,28,14,0,94,95,5,11,0,0,95,96,
        5,2,0,0,96,97,3,8,4,0,97,103,5,3,0,0,98,99,5,14,0,0,99,100,5,2,0,
        0,100,101,3,8,4,0,101,102,5,3,0,0,102,104,1,0,0,0,103,98,1,0,0,0,
        103,104,1,0,0,0,104,19,1,0,0,0,105,106,5,15,0,0,106,107,5,10,0,0,
        107,108,3,28,14,0,108,109,5,11,0,0,109,110,5,2,0,0,110,111,3,8,4,
        0,111,112,5,3,0,0,112,21,1,0,0,0,113,118,3,24,12,0,114,115,7,1,0,
        0,115,117,3,24,12,0,116,114,1,0,0,0,117,120,1,0,0,0,118,116,1,0,
        0,0,118,119,1,0,0,0,119,125,1,0,0,0,120,118,1,0,0,0,121,122,3,40,
        20,0,122,123,3,24,12,0,123,125,1,0,0,0,124,113,1,0,0,0,124,121,1,
        0,0,0,125,23,1,0,0,0,126,131,3,26,13,0,127,128,7,2,0,0,128,130,3,
        26,13,0,129,127,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,
        1,0,0,0,132,143,1,0,0,0,133,131,1,0,0,0,134,139,7,3,0,0,135,136,
        5,20,0,0,136,138,7,3,0,0,137,135,1,0,0,0,138,141,1,0,0,0,139,137,
        1,0,0,0,139,140,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,142,126,
        1,0,0,0,142,134,1,0,0,0,143,25,1,0,0,0,144,152,5,31,0,0,145,152,
        5,32,0,0,146,152,5,33,0,0,147,148,5,10,0,0,148,149,3,22,11,0,149,
        150,5,11,0,0,150,152,1,0,0,0,151,144,1,0,0,0,151,145,1,0,0,0,151,
        146,1,0,0,0,151,147,1,0,0,0,152,27,1,0,0,0,153,154,5,10,0,0,154,
        155,3,28,14,0,155,156,5,11,0,0,156,159,1,0,0,0,157,159,3,30,15,0,
        158,153,1,0,0,0,158,157,1,0,0,0,159,29,1,0,0,0,160,161,6,15,-1,0,
        161,164,3,32,16,0,162,163,5,21,0,0,163,165,3,32,16,0,164,162,1,0,
        0,0,164,165,1,0,0,0,165,171,1,0,0,0,166,167,10,1,0,0,167,168,5,21,
        0,0,168,170,3,30,15,0,169,166,1,0,0,0,170,173,1,0,0,0,171,169,1,
        0,0,0,171,172,1,0,0,0,172,31,1,0,0,0,173,171,1,0,0,0,174,175,6,16,
        -1,0,175,178,3,34,17,0,176,177,5,22,0,0,177,179,3,34,17,0,178,176,
        1,0,0,0,178,179,1,0,0,0,179,185,1,0,0,0,180,181,10,1,0,0,181,182,
        5,22,0,0,182,184,3,32,16,0,183,180,1,0,0,0,184,187,1,0,0,0,185,183,
        1,0,0,0,185,186,1,0,0,0,186,33,1,0,0,0,187,185,1,0,0,0,188,189,6,
        17,-1,0,189,190,5,23,0,0,190,201,3,34,17,4,191,192,5,10,0,0,192,
        195,3,34,17,0,193,194,7,4,0,0,194,196,3,34,17,0,195,193,1,0,0,0,
        195,196,1,0,0,0,196,197,1,0,0,0,197,198,5,11,0,0,198,201,1,0,0,0,
        199,201,7,5,0,0,200,188,1,0,0,0,200,191,1,0,0,0,200,199,1,0,0,0,
        201,207,1,0,0,0,202,203,10,2,0,0,203,204,7,6,0,0,204,206,3,34,17,
        0,205,202,1,0,0,0,206,209,1,0,0,0,207,205,1,0,0,0,207,208,1,0,0,
        0,208,35,1,0,0,0,209,207,1,0,0,0,210,215,7,7,0,0,211,212,5,30,0,
        0,212,214,7,7,0,0,213,211,1,0,0,0,214,217,1,0,0,0,215,213,1,0,0,
        0,215,216,1,0,0,0,216,37,1,0,0,0,217,215,1,0,0,0,218,223,5,31,0,
        0,219,220,5,30,0,0,220,222,5,31,0,0,221,219,1,0,0,0,222,225,1,0,
        0,0,223,221,1,0,0,0,223,224,1,0,0,0,224,39,1,0,0,0,225,223,1,0,0,
        0,226,227,7,1,0,0,227,41,1,0,0,0,20,54,65,72,103,118,124,131,139,
        142,151,158,164,171,178,185,195,200,207,215,223
    ]

class SimpAlgParser ( Parser ):

    grammarFileName = "SimpAlg.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'{'", "'}'", "'program'", "';'", 
                     "'int'", "'float'", "'='", "'print'", "'('", "')'", 
                     "'scan'", "'if'", "'else'", "'while'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'or'", "'and'", "'!'", "'<'", 
                     "'>'", "'<='", "'>='", "'=='", "'!='", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INT", 
                      "FLOAT", "STRING", "Comment", "WS" ]

    RULE_programa = 0
    RULE_declaracoes = 1
    RULE_declaracao = 2
    RULE_tipo = 3
    RULE_comandos = 4
    RULE_comando = 5
    RULE_atribuicao = 6
    RULE_saida = 7
    RULE_entrada = 8
    RULE_condicional = 9
    RULE_repeticao = 10
    RULE_expressao = 11
    RULE_termo = 12
    RULE_fator = 13
    RULE_expressao_logica = 14
    RULE_or_expr = 15
    RULE_and_expr = 16
    RULE_relacional = 17
    RULE_lista_de_valores = 18
    RULE_lista_de_variaveis = 19
    RULE_op_unario = 20

    ruleNames =  [ "programa", "declaracoes", "declaracao", "tipo", "comandos", 
                   "comando", "atribuicao", "saida", "entrada", "condicional", 
                   "repeticao", "expressao", "termo", "fator", "expressao_logica", 
                   "or_expr", "and_expr", "relacional", "lista_de_valores", 
                   "lista_de_variaveis", "op_unario" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    ID=31
    INT=32
    FLOAT=33
    STRING=34
    Comment=35
    WS=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracoes(self):
            return self.getTypedRuleContext(SimpAlgParser.DeclaracoesContext,0)


        def comandos(self):
            return self.getTypedRuleContext(SimpAlgParser.ComandosContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = SimpAlgParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(SimpAlgParser.T__0)
            self.state = 43
            self.match(SimpAlgParser.T__1)
            self.state = 44
            self.declaracoes()
            self.state = 45
            self.match(SimpAlgParser.T__2)
            self.state = 46
            self.match(SimpAlgParser.T__3)
            self.state = 47
            self.match(SimpAlgParser.T__1)
            self.state = 48
            self.comandos()
            self.state = 49
            self.match(SimpAlgParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.DeclaracaoContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.DeclaracaoContext,i)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_declaracoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracoes" ):
                listener.enterDeclaracoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracoes" ):
                listener.exitDeclaracoes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracoes" ):
                return visitor.visitDeclaracoes(self)
            else:
                return visitor.visitChildren(self)




    def declaracoes(self):

        localctx = SimpAlgParser.DeclaracoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 51
                self.declaracao()
                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==6 or _la==7):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(SimpAlgParser.TipoContext,0)


        def lista_de_variaveis(self):
            return self.getTypedRuleContext(SimpAlgParser.Lista_de_variaveisContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao" ):
                return visitor.visitDeclaracao(self)
            else:
                return visitor.visitChildren(self)




    def declaracao(self):

        localctx = SimpAlgParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.tipo()
            self.state = 57
            self.lista_de_variaveis()
            self.state = 58
            self.match(SimpAlgParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpAlgParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = SimpAlgParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.ComandoContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.ComandoContext,i)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_comandos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandos" ):
                listener.enterComandos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandos" ):
                listener.exitComandos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandos" ):
                return visitor.visitComandos(self)
            else:
                return visitor.visitChildren(self)




    def comandos(self):

        localctx = SimpAlgParser.ComandosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comandos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self.comando()
                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2147529216) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribuicao(self):
            return self.getTypedRuleContext(SimpAlgParser.AtribuicaoContext,0)


        def saida(self):
            return self.getTypedRuleContext(SimpAlgParser.SaidaContext,0)


        def entrada(self):
            return self.getTypedRuleContext(SimpAlgParser.EntradaContext,0)


        def condicional(self):
            return self.getTypedRuleContext(SimpAlgParser.CondicionalContext,0)


        def repeticao(self):
            return self.getTypedRuleContext(SimpAlgParser.RepeticaoContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando" ):
                return visitor.visitComando(self)
            else:
                return visitor.visitChildren(self)




    def comando(self):

        localctx = SimpAlgParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comando)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.atribuicao()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.saida()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.entrada()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 70
                self.condicional()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 71
                self.repeticao()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpAlgParser.ID, 0)

        def expressao(self):
            return self.getTypedRuleContext(SimpAlgParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao" ):
                return visitor.visitAtribuicao(self)
            else:
                return visitor.visitChildren(self)




    def atribuicao(self):

        localctx = SimpAlgParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(SimpAlgParser.ID)
            self.state = 75
            self.match(SimpAlgParser.T__7)
            self.state = 76
            self.expressao()
            self.state = 77
            self.match(SimpAlgParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SaidaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lista_de_valores(self):
            return self.getTypedRuleContext(SimpAlgParser.Lista_de_valoresContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_saida

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaida" ):
                listener.enterSaida(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaida" ):
                listener.exitSaida(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSaida" ):
                return visitor.visitSaida(self)
            else:
                return visitor.visitChildren(self)




    def saida(self):

        localctx = SimpAlgParser.SaidaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_saida)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(SimpAlgParser.T__8)
            self.state = 80
            self.match(SimpAlgParser.T__9)
            self.state = 81
            self.lista_de_valores()
            self.state = 82
            self.match(SimpAlgParser.T__10)
            self.state = 83
            self.match(SimpAlgParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntradaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lista_de_variaveis(self):
            return self.getTypedRuleContext(SimpAlgParser.Lista_de_variaveisContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_entrada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntrada" ):
                listener.enterEntrada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntrada" ):
                listener.exitEntrada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntrada" ):
                return visitor.visitEntrada(self)
            else:
                return visitor.visitChildren(self)




    def entrada(self):

        localctx = SimpAlgParser.EntradaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_entrada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(SimpAlgParser.T__11)
            self.state = 86
            self.match(SimpAlgParser.T__9)
            self.state = 87
            self.lista_de_variaveis()
            self.state = 88
            self.match(SimpAlgParser.T__10)
            self.state = 89
            self.match(SimpAlgParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao_logica(self):
            return self.getTypedRuleContext(SimpAlgParser.Expressao_logicaContext,0)


        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.ComandosContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.ComandosContext,i)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = SimpAlgParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(SimpAlgParser.T__12)
            self.state = 92
            self.match(SimpAlgParser.T__9)
            self.state = 93
            self.expressao_logica()
            self.state = 94
            self.match(SimpAlgParser.T__10)
            self.state = 95
            self.match(SimpAlgParser.T__1)
            self.state = 96
            self.comandos()
            self.state = 97
            self.match(SimpAlgParser.T__2)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 98
                self.match(SimpAlgParser.T__13)
                self.state = 99
                self.match(SimpAlgParser.T__1)
                self.state = 100
                self.comandos()
                self.state = 101
                self.match(SimpAlgParser.T__2)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeticaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao_logica(self):
            return self.getTypedRuleContext(SimpAlgParser.Expressao_logicaContext,0)


        def comandos(self):
            return self.getTypedRuleContext(SimpAlgParser.ComandosContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_repeticao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeticao" ):
                listener.enterRepeticao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeticao" ):
                listener.exitRepeticao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeticao" ):
                return visitor.visitRepeticao(self)
            else:
                return visitor.visitChildren(self)




    def repeticao(self):

        localctx = SimpAlgParser.RepeticaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_repeticao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(SimpAlgParser.T__14)
            self.state = 106
            self.match(SimpAlgParser.T__9)
            self.state = 107
            self.expressao_logica()
            self.state = 108
            self.match(SimpAlgParser.T__10)
            self.state = 109
            self.match(SimpAlgParser.T__1)
            self.state = 110
            self.comandos()
            self.state = 111
            self.match(SimpAlgParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.TermoContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.TermoContext,i)


        def op_unario(self):
            return self.getTypedRuleContext(SimpAlgParser.Op_unarioContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao" ):
                return visitor.visitExpressao(self)
            else:
                return visitor.visitChildren(self)




    def expressao(self):

        localctx = SimpAlgParser.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expressao)
        self._la = 0 # Token type
        try:
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 31, 32, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.termo()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16 or _la==17:
                    self.state = 114
                    _la = self._input.LA(1)
                    if not(_la==16 or _la==17):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 115
                    self.termo()
                    self.state = 120
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [16, 17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.op_unario()
                self.state = 122
                self.termo()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.FatorContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.FatorContext,i)


        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SimpAlgParser.INT)
            else:
                return self.getToken(SimpAlgParser.INT, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SimpAlgParser.ID)
            else:
                return self.getToken(SimpAlgParser.ID, i)

        def getRuleIndex(self):
            return SimpAlgParser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermo" ):
                return visitor.visitTermo(self)
            else:
                return visitor.visitChildren(self)




    def termo(self):

        localctx = SimpAlgParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_termo)
        self._la = 0 # Token type
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.fator()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==18 or _la==19:
                    self.state = 127
                    _la = self._input.LA(1)
                    if not(_la==18 or _la==19):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 128
                    self.fator()
                    self.state = 133
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                _la = self._input.LA(1)
                if not(_la==31 or _la==32):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 135
                    self.match(SimpAlgParser.T__19)
                    self.state = 136
                    _la = self._input.LA(1)
                    if not(_la==31 or _la==32):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 141
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpAlgParser.ID, 0)

        def INT(self):
            return self.getToken(SimpAlgParser.INT, 0)

        def FLOAT(self):
            return self.getToken(SimpAlgParser.FLOAT, 0)

        def expressao(self):
            return self.getTypedRuleContext(SimpAlgParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_fator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator" ):
                listener.enterFator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator" ):
                listener.exitFator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFator" ):
                return visitor.visitFator(self)
            else:
                return visitor.visitChildren(self)




    def fator(self):

        localctx = SimpAlgParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_fator)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(SimpAlgParser.ID)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.match(SimpAlgParser.INT)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 146
                self.match(SimpAlgParser.FLOAT)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 147
                self.match(SimpAlgParser.T__9)
                self.state = 148
                self.expressao()
                self.state = 149
                self.match(SimpAlgParser.T__10)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expressao_logicaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao_logica(self):
            return self.getTypedRuleContext(SimpAlgParser.Expressao_logicaContext,0)


        def or_expr(self):
            return self.getTypedRuleContext(SimpAlgParser.Or_exprContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_expressao_logica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao_logica" ):
                listener.enterExpressao_logica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao_logica" ):
                listener.exitExpressao_logica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao_logica" ):
                return visitor.visitExpressao_logica(self)
            else:
                return visitor.visitChildren(self)




    def expressao_logica(self):

        localctx = SimpAlgParser.Expressao_logicaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expressao_logica)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.match(SimpAlgParser.T__9)
                self.state = 154
                self.expressao_logica()
                self.state = 155
                self.match(SimpAlgParser.T__10)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.or_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.And_exprContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.And_exprContext,i)


        def or_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.Or_exprContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.Or_exprContext,i)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_or_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr_expr" ):
                listener.enterOr_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr_expr" ):
                listener.exitOr_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr_expr" ):
                return visitor.visitOr_expr(self)
            else:
                return visitor.visitChildren(self)



    def or_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpAlgParser.Or_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_or_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.and_expr(0)
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 162
                self.match(SimpAlgParser.T__20)
                self.state = 163
                self.and_expr(0)


            self._ctx.stop = self._input.LT(-1)
            self.state = 171
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpAlgParser.Or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_or_expr)
                    self.state = 166
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")

                    self.state = 167
                    self.match(SimpAlgParser.T__20)
                    self.state = 168
                    self.or_expr(0) 
                self.state = 173
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class And_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relacional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.RelacionalContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.RelacionalContext,i)


        def and_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.And_exprContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.And_exprContext,i)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_and_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_expr" ):
                listener.enterAnd_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_expr" ):
                listener.exitAnd_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_expr" ):
                return visitor.visitAnd_expr(self)
            else:
                return visitor.visitChildren(self)



    def and_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpAlgParser.And_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_and_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.relacional(0)
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 176
                self.match(SimpAlgParser.T__21)
                self.state = 177
                self.relacional(0)


            self._ctx.stop = self._input.LT(-1)
            self.state = 185
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpAlgParser.And_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_expr)
                    self.state = 180
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")

                    self.state = 181
                    self.match(SimpAlgParser.T__21)
                    self.state = 182
                    self.and_expr(0) 
                self.state = 187
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relacional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.RelacionalContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.RelacionalContext,i)


        def ID(self):
            return self.getToken(SimpAlgParser.ID, 0)

        def INT(self):
            return self.getToken(SimpAlgParser.INT, 0)

        def FLOAT(self):
            return self.getToken(SimpAlgParser.FLOAT, 0)

        def getRuleIndex(self):
            return SimpAlgParser.RULE_relacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelacional" ):
                listener.enterRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelacional" ):
                listener.exitRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelacional" ):
                return visitor.visitRelacional(self)
            else:
                return visitor.visitChildren(self)



    def relacional(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpAlgParser.RelacionalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_relacional, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.state = 189
                self.match(SimpAlgParser.T__22)
                self.state = 190
                self.relacional(4)
                pass
            elif token in [10]:
                self.state = 191
                self.match(SimpAlgParser.T__9)
                self.state = 192
                self.relacional(0)
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21 or _la==22:
                    self.state = 193
                    _la = self._input.LA(1)
                    if not(_la==21 or _la==22):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 194
                    self.relacional(0)


                self.state = 197
                self.match(SimpAlgParser.T__10)
                pass
            elif token in [31, 32, 33]:
                self.state = 199
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15032385536) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpAlgParser.RelacionalContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relacional)
                    self.state = 202
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 203
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 204
                    self.relacional(0) 
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Lista_de_valoresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SimpAlgParser.ID)
            else:
                return self.getToken(SimpAlgParser.ID, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SimpAlgParser.INT)
            else:
                return self.getToken(SimpAlgParser.INT, i)

        def FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(SimpAlgParser.FLOAT)
            else:
                return self.getToken(SimpAlgParser.FLOAT, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(SimpAlgParser.STRING)
            else:
                return self.getToken(SimpAlgParser.STRING, i)

        def getRuleIndex(self):
            return SimpAlgParser.RULE_lista_de_valores

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_de_valores" ):
                listener.enterLista_de_valores(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_de_valores" ):
                listener.exitLista_de_valores(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_de_valores" ):
                return visitor.visitLista_de_valores(self)
            else:
                return visitor.visitChildren(self)




    def lista_de_valores(self):

        localctx = SimpAlgParser.Lista_de_valoresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_lista_de_valores)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 211
                self.match(SimpAlgParser.T__29)
                self.state = 212
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_de_variaveisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SimpAlgParser.ID)
            else:
                return self.getToken(SimpAlgParser.ID, i)

        def getRuleIndex(self):
            return SimpAlgParser.RULE_lista_de_variaveis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_de_variaveis" ):
                listener.enterLista_de_variaveis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_de_variaveis" ):
                listener.exitLista_de_variaveis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_de_variaveis" ):
                return visitor.visitLista_de_variaveis(self)
            else:
                return visitor.visitChildren(self)




    def lista_de_variaveis(self):

        localctx = SimpAlgParser.Lista_de_variaveisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_lista_de_variaveis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(SimpAlgParser.ID)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 219
                self.match(SimpAlgParser.T__29)
                self.state = 220
                self.match(SimpAlgParser.ID)
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_unarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpAlgParser.RULE_op_unario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_unario" ):
                listener.enterOp_unario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_unario" ):
                listener.exitOp_unario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_unario" ):
                return visitor.visitOp_unario(self)
            else:
                return visitor.visitChildren(self)




    def op_unario(self):

        localctx = SimpAlgParser.Op_unarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_op_unario)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.or_expr_sempred
        self._predicates[16] = self.and_expr_sempred
        self._predicates[17] = self.relacional_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def or_expr_sempred(self, localctx:Or_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def and_expr_sempred(self, localctx:And_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def relacional_sempred(self, localctx:RelacionalContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




