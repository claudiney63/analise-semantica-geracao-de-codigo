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
        4,1,26,226,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,1,4,1,47,8,1,11,1,12,1,48,1,1,1,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,3,3,63,8,3,1,4,4,4,66,8,4,11,4,12,4,67,1,
        4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,3,5,87,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,3,9,123,8,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        3,11,145,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        5,11,157,8,11,10,11,12,11,160,9,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,176,8,12,10,12,12,12,
        179,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        3,13,192,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,202,8,
        14,1,15,1,15,1,15,5,15,207,8,15,10,15,12,15,210,9,15,1,15,1,15,1,
        16,1,16,1,16,5,16,217,8,16,10,16,12,16,220,9,16,1,16,1,16,1,17,1,
        17,1,17,0,2,22,24,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,0,2,1,0,21,24,1,0,16,17,226,0,36,1,0,0,0,2,46,1,0,0,0,4,52,
        1,0,0,0,6,62,1,0,0,0,8,65,1,0,0,0,10,86,1,0,0,0,12,88,1,0,0,0,14,
        94,1,0,0,0,16,101,1,0,0,0,18,108,1,0,0,0,20,126,1,0,0,0,22,144,1,
        0,0,0,24,161,1,0,0,0,26,191,1,0,0,0,28,201,1,0,0,0,30,203,1,0,0,
        0,32,213,1,0,0,0,34,223,1,0,0,0,36,37,5,1,0,0,37,38,5,2,0,0,38,39,
        3,2,1,0,39,40,5,3,0,0,40,41,5,4,0,0,41,42,5,2,0,0,42,43,3,8,4,0,
        43,44,5,3,0,0,44,1,1,0,0,0,45,47,3,4,2,0,46,45,1,0,0,0,47,48,1,0,
        0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,50,1,0,0,0,50,51,6,1,-1,0,51,
        3,1,0,0,0,52,53,3,6,3,0,53,54,3,6,3,0,54,55,3,32,16,0,55,56,5,5,
        0,0,56,57,6,2,-1,0,57,5,1,0,0,0,58,59,5,6,0,0,59,63,6,3,-1,0,60,
        61,5,7,0,0,61,63,6,3,-1,0,62,58,1,0,0,0,62,60,1,0,0,0,63,7,1,0,0,
        0,64,66,3,10,5,0,65,64,1,0,0,0,66,67,1,0,0,0,67,65,1,0,0,0,67,68,
        1,0,0,0,68,69,1,0,0,0,69,70,6,4,-1,0,70,9,1,0,0,0,71,72,3,12,6,0,
        72,73,6,5,-1,0,73,87,1,0,0,0,74,75,3,14,7,0,75,76,6,5,-1,0,76,87,
        1,0,0,0,77,78,3,16,8,0,78,79,6,5,-1,0,79,87,1,0,0,0,80,81,3,18,9,
        0,81,82,6,5,-1,0,82,87,1,0,0,0,83,84,3,20,10,0,84,85,6,5,-1,0,85,
        87,1,0,0,0,86,71,1,0,0,0,86,74,1,0,0,0,86,77,1,0,0,0,86,80,1,0,0,
        0,86,83,1,0,0,0,87,11,1,0,0,0,88,89,5,21,0,0,89,90,5,8,0,0,90,91,
        3,22,11,0,91,92,5,5,0,0,92,93,6,6,-1,0,93,13,1,0,0,0,94,95,5,9,0,
        0,95,96,5,10,0,0,96,97,3,30,15,0,97,98,5,11,0,0,98,99,5,5,0,0,99,
        100,6,7,-1,0,100,15,1,0,0,0,101,102,5,12,0,0,102,103,5,10,0,0,103,
        104,3,32,16,0,104,105,5,11,0,0,105,106,5,5,0,0,106,107,6,8,-1,0,
        107,17,1,0,0,0,108,109,5,13,0,0,109,110,5,10,0,0,110,111,3,28,14,
        0,111,112,5,11,0,0,112,113,5,2,0,0,113,114,3,8,4,0,114,115,6,9,-1,
        0,115,122,5,3,0,0,116,117,5,14,0,0,117,118,5,2,0,0,118,119,3,8,4,
        0,119,120,6,9,-1,0,120,121,5,3,0,0,121,123,1,0,0,0,122,116,1,0,0,
        0,122,123,1,0,0,0,123,124,1,0,0,0,124,125,6,9,-1,0,125,19,1,0,0,
        0,126,127,5,15,0,0,127,128,5,10,0,0,128,129,3,28,14,0,129,130,5,
        11,0,0,130,131,5,2,0,0,131,132,3,8,4,0,132,133,6,10,-1,0,133,134,
        5,3,0,0,134,135,6,10,-1,0,135,21,1,0,0,0,136,137,6,11,-1,0,137,138,
        3,24,12,0,138,139,6,11,-1,0,139,145,1,0,0,0,140,141,3,34,17,0,141,
        142,3,24,12,0,142,143,6,11,-1,0,143,145,1,0,0,0,144,136,1,0,0,0,
        144,140,1,0,0,0,145,158,1,0,0,0,146,147,10,2,0,0,147,148,5,16,0,
        0,148,149,3,24,12,0,149,150,6,11,-1,0,150,157,1,0,0,0,151,152,10,
        1,0,0,152,153,5,17,0,0,153,154,3,24,12,0,154,155,6,11,-1,0,155,157,
        1,0,0,0,156,146,1,0,0,0,156,151,1,0,0,0,157,160,1,0,0,0,158,156,
        1,0,0,0,158,159,1,0,0,0,159,23,1,0,0,0,160,158,1,0,0,0,161,162,6,
        12,-1,0,162,163,3,26,13,0,163,164,6,12,-1,0,164,177,1,0,0,0,165,
        166,10,2,0,0,166,167,5,18,0,0,167,168,3,26,13,0,168,169,6,12,-1,
        0,169,176,1,0,0,0,170,171,10,1,0,0,171,172,5,19,0,0,172,173,3,26,
        13,0,173,174,6,12,-1,0,174,176,1,0,0,0,175,165,1,0,0,0,175,170,1,
        0,0,0,176,179,1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,25,1,0,
        0,0,179,177,1,0,0,0,180,181,5,21,0,0,181,192,6,13,-1,0,182,183,5,
        22,0,0,183,192,6,13,-1,0,184,185,5,23,0,0,185,192,6,13,-1,0,186,
        187,5,10,0,0,187,188,3,22,11,0,188,189,5,11,0,0,189,190,6,13,-1,
        0,190,192,1,0,0,0,191,180,1,0,0,0,191,182,1,0,0,0,191,184,1,0,0,
        0,191,186,1,0,0,0,192,27,1,0,0,0,193,194,3,22,11,0,194,195,6,14,
        -1,0,195,202,1,0,0,0,196,197,5,10,0,0,197,198,3,28,14,0,198,199,
        5,11,0,0,199,200,6,14,-1,0,200,202,1,0,0,0,201,193,1,0,0,0,201,196,
        1,0,0,0,202,29,1,0,0,0,203,208,7,0,0,0,204,205,5,20,0,0,205,207,
        7,0,0,0,206,204,1,0,0,0,207,210,1,0,0,0,208,206,1,0,0,0,208,209,
        1,0,0,0,209,211,1,0,0,0,210,208,1,0,0,0,211,212,6,15,-1,0,212,31,
        1,0,0,0,213,218,5,21,0,0,214,215,5,20,0,0,215,217,5,21,0,0,216,214,
        1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,221,
        1,0,0,0,220,218,1,0,0,0,221,222,6,16,-1,0,222,33,1,0,0,0,223,224,
        7,1,0,0,224,35,1,0,0,0,14,48,62,67,86,122,144,156,158,175,177,191,
        201,208,218
    ]

class SimpAlgParser ( Parser ):

    grammarFileName = "SimpAlg.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'{'", "'}'", "'program'", "';'", 
                     "'int'", "'float'", "'='", "'print'", "'('", "')'", 
                     "'scan'", "'if'", "'else'", "'while'", "'+'", "'-'", 
                     "'*'", "'/'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "FLOAT", "STRING", "Comment", 
                      "WS" ]

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
    RULE_lista_de_valores = 15
    RULE_lista_de_variaveis = 16
    RULE_op_unario = 17

    ruleNames =  [ "programa", "declaracoes", "declaracao", "tipo", "comandos", 
                   "comando", "atribuicao", "saida", "entrada", "condicional", 
                   "repeticao", "expressao", "termo", "fator", "expressao_logica", 
                   "lista_de_valores", "lista_de_variaveis", "op_unario" ]

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
    ID=21
    INT=22
    FLOAT=23
    STRING=24
    Comment=25
    WS=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



        self.decls = [];
        self.cmds = [];



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
            self.state = 36
            self.match(SimpAlgParser.T__0)
            self.state = 37
            self.match(SimpAlgParser.T__1)
            self.state = 38
            self.declaracoes()
            self.state = 39
            self.match(SimpAlgParser.T__2)
            self.state = 40
            self.match(SimpAlgParser.T__3)
            self.state = 41
            self.match(SimpAlgParser.T__1)
            self.state = 42
            self.comandos()
            self.state = 43
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
            self.result = None
            self.decs = None # DeclaracaoContext

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
            self.state = 46 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 45
                localctx.decs = self.declaracao()
                self.state = 48 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==6 or _la==7):
                    break

            localctx.result = self.decs
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
            self.result = None
            self.t = None # TipoContext
            self.vars_ = None # Lista_de_variaveisContext

        def tipo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.TipoContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.TipoContext,i)


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
            self.state = 52
            self.tipo()
            self.state = 53
            localctx.t = self.tipo()
            self.state = 54
            localctx.vars_ = self.lista_de_variaveis()
            self.state = 55
            self.match(SimpAlgParser.T__4)
             localctx.result =  f"{t.result} {vars_.result}" 
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
            self.result = None


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
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(SimpAlgParser.T__5)
                localctx.result =  "int"
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(SimpAlgParser.T__6)
                localctx.result =  "float"
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


    class ComandosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self.cmds = None # ComandoContext

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
            self.state = 65 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64
                localctx.cmds = self.comando()
                self.state = 67 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2142720) != 0)):
                    break

            localctx.result =  self.cmds
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
            self.result = None
            self.atr = None # AtribuicaoContext
            self.s = None # SaidaContext
            self.e = None # EntradaContext
            self.c = None # CondicionalContext
            self.r = None # RepeticaoContext

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
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                localctx.atr = self.atribuicao()
                localctx.result =  atr.result
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                localctx.s = self.saida()
                localctx.result =  s.result
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                localctx.e = self.entrada()
                localctx.result =  e.result
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 80
                localctx.c = self.condicional()
                localctx.result =  c.result
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 83
                localctx.r = self.repeticao()
                localctx.result =  r.result
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
            self.result = None
            self.exp = None # ExpressaoContext

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
            self.state = 88
            self.match(SimpAlgParser.ID)
            self.state = 89
            self.match(SimpAlgParser.T__7)
            self.state = 90
            localctx.exp = self.expressao(0)
            self.state = 91
            self.match(SimpAlgParser.T__4)
            localctx.result =  f"{ID.text} = {exp.result}"
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
            self.result = None
            self.vals = None # Lista_de_valoresContext

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
            self.state = 94
            self.match(SimpAlgParser.T__8)
            self.state = 95
            self.match(SimpAlgParser.T__9)
            self.state = 96
            localctx.vals = self.lista_de_valores()
            self.state = 97
            self.match(SimpAlgParser.T__10)
            self.state = 98
            self.match(SimpAlgParser.T__4)
            localctx.result =  f'print({vals.result})';
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
            self.result = None
            self.vars_ = None # Lista_de_variaveisContext

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
            self.state = 101
            self.match(SimpAlgParser.T__11)
            self.state = 102
            self.match(SimpAlgParser.T__9)
            self.state = 103
            localctx.vars_ = self.lista_de_variaveis()
            self.state = 104
            self.match(SimpAlgParser.T__10)
            self.state = 105
            self.match(SimpAlgParser.T__4)
            localctx.result =  f'scan({vars.result})';
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
            self.result = None
            self.exp = None # Expressao_logicaContext
            self.cmds = None # ComandosContext
            self.else_cmds = None # ComandosContext

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
            self.state = 108
            self.match(SimpAlgParser.T__12)
            self.state = 109
            self.match(SimpAlgParser.T__9)
            self.state = 110
            localctx.exp = self.expressao_logica()
            self.state = 111
            self.match(SimpAlgParser.T__10)
            self.state = 112
            self.match(SimpAlgParser.T__1)
            self.state = 113
            localctx.cmds = self.comandos()
            cond_cmds = cmds.result
            self.state = 115
            self.match(SimpAlgParser.T__2)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 116
                self.match(SimpAlgParser.T__13)
                self.state = 117
                self.match(SimpAlgParser.T__1)
                self.state = 118
                localctx.else_cmds = self.comandos()
                else_cmds = else_cmds.result
                self.state = 120
                self.match(SimpAlgParser.T__2)


            localctx.result =  f"if {exp.result}:\n    {cond_cmds}" + (f"else:\n    {else_cmds}" if else_cmds else "")
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
            self.result = None
            self.exp = None # Expressao_logicaContext
            self.cmds = None # ComandosContext

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
            self.state = 126
            self.match(SimpAlgParser.T__14)
            self.state = 127
            self.match(SimpAlgParser.T__9)
            self.state = 128
            localctx.exp = self.expressao_logica()
            self.state = 129
            self.match(SimpAlgParser.T__10)
            self.state = 130
            self.match(SimpAlgParser.T__1)
            self.state = 131
            localctx.cmds = self.comandos()
            loop_cmds = cmds.result
            self.state = 133
            self.match(SimpAlgParser.T__2)
            localctx.result =  f"while {exp.result}:\n    {loop_cmds}"
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
            self.result = None
            self.e = None # ExpressaoContext
            self.t = None # TermoContext
            self.un = None # Op_unarioContext

        def termo(self):
            return self.getTypedRuleContext(SimpAlgParser.TermoContext,0)


        def op_unario(self):
            return self.getTypedRuleContext(SimpAlgParser.Op_unarioContext,0)


        def expressao(self):
            return self.getTypedRuleContext(SimpAlgParser.ExpressaoContext,0)


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



    def expressao(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpAlgParser.ExpressaoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expressao, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 21, 22, 23]:
                self.state = 137
                localctx.t = self.termo(0)
                localctx.result =  t.result
                pass
            elif token in [16, 17]:
                self.state = 140
                localctx.un = self.op_unario()
                self.state = 141
                self.termo(0)
                localctx.result =  f"{un.text}{termo.result}"
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 158
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 156
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = SimpAlgParser.ExpressaoContext(self, _parentctx, _parentState)
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 146
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 147
                        self.match(SimpAlgParser.T__15)
                        self.state = 148
                        localctx.t = self.termo(0)
                        localctx.result =  f"{e.result} + {t.result}"
                        pass

                    elif la_ == 2:
                        localctx = SimpAlgParser.ExpressaoContext(self, _parentctx, _parentState)
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 151
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 152
                        self.match(SimpAlgParser.T__16)
                        self.state = 153
                        localctx.t = self.termo(0)
                        localctx.result =  f"{e.result} - {t.result}"
                        pass

             
                self.state = 160
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self.e = None # TermoContext
            self.f = None # FatorContext

        def fator(self):
            return self.getTypedRuleContext(SimpAlgParser.FatorContext,0)


        def termo(self):
            return self.getTypedRuleContext(SimpAlgParser.TermoContext,0)


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



    def termo(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpAlgParser.TermoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_termo, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            localctx.f = self.fator()
            localctx.result =  f.result
            self._ctx.stop = self._input.LT(-1)
            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 175
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = SimpAlgParser.TermoContext(self, _parentctx, _parentState)
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termo)
                        self.state = 165
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 166
                        self.match(SimpAlgParser.T__17)
                        self.state = 167
                        localctx.f = self.fator()
                        localctx.result =  f"{e.result} * {f.result}"
                        pass

                    elif la_ == 2:
                        localctx = SimpAlgParser.TermoContext(self, _parentctx, _parentState)
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termo)
                        self.state = 170
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 171
                        self.match(SimpAlgParser.T__18)
                        self.state = 172
                        localctx.f = self.fator()
                        localctx.result =  f"{e.result} / {f.result}"
                        pass

             
                self.state = 179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self.exp = None # ExpressaoContext

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
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(SimpAlgParser.ID)
                localctx.result =  ID.text
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.match(SimpAlgParser.INT)
                localctx.result =  INT.text
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.match(SimpAlgParser.FLOAT)
                localctx.result =  FLOAT.text
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 186
                self.match(SimpAlgParser.T__9)
                self.state = 187
                localctx.exp = self.expressao(0)
                self.state = 188
                self.match(SimpAlgParser.T__10)
                localctx.result =  f"({exp.result})"
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
            self.result = None
            self.e = None # ExpressaoContext
            self.exp = None # Expressao_logicaContext

        def expressao(self):
            return self.getTypedRuleContext(SimpAlgParser.ExpressaoContext,0)


        def expressao_logica(self):
            return self.getTypedRuleContext(SimpAlgParser.Expressao_logicaContext,0)


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
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                localctx.e = self.expressao(0)
                localctx.result =  e.result
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.match(SimpAlgParser.T__9)
                self.state = 197
                localctx.exp = self.expressao_logica()
                self.state = 198
                self.match(SimpAlgParser.T__10)
                localctx.result =  f"({exp.result})"
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_de_valoresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self.first = None # Token
            self.values = None # Token

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
        self.enterRule(localctx, 30, self.RULE_lista_de_valores)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            localctx.first = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31457280) != 0)):
                localctx.first = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 204
                self.match(SimpAlgParser.T__19)
                self.state = 205
                localctx.values = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31457280) != 0)):
                    localctx.values = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)


                    vals = [first.text]
                    if values:
                        for val in values:
                            vals.append(val.text)
                    localctx.result = ", ".join(vals)
                
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
            self.result = None
            self.first = None # Token
            self._ID = None # Token
            self.vars_ = list() # of Tokens

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
        self.enterRule(localctx, 32, self.RULE_lista_de_variaveis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            localctx.first = self.match(SimpAlgParser.ID)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 214
                self.match(SimpAlgParser.T__19)
                self.state = 215
                localctx._ID = self.match(SimpAlgParser.ID)
                localctx.vars_.append(localctx._ID)
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)


                    vars_list = [first.text]
                    if localctx.vars_:
                        for var in localctx.vars_:
                            vars_list.append(var.text)
                    localctx.result = ", ".join(vars_list)
                
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
        self.enterRule(localctx, 34, self.RULE_op_unario)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
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
        self._predicates[11] = self.expressao_sempred
        self._predicates[12] = self.termo_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressao_sempred(self, localctx:ExpressaoContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def termo_sempred(self, localctx:TermoContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




