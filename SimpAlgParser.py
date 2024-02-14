# Generated from SimpAlg.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from SemanticAnalyser import *

def serializedATN():
    return [
        4,1,36,251,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,4,3,64,8,3,11,3,12,3,65,1,4,1,4,1,
        4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,77,8,5,10,5,12,5,80,9,5,1,6,1,6,1,
        7,4,7,85,8,7,11,7,12,7,86,1,8,1,8,1,8,1,8,1,8,3,8,94,8,8,1,9,1,9,
        1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,
        11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,3,12,125,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,
        14,1,14,5,14,138,8,14,10,14,12,14,141,9,14,1,14,1,14,1,14,3,14,146,
        8,14,1,15,1,15,1,15,5,15,151,8,15,10,15,12,15,154,9,15,1,15,1,15,
        1,15,5,15,159,8,15,10,15,12,15,162,9,15,3,15,164,8,15,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,3,16,173,8,16,1,17,1,17,1,17,1,17,1,17,
        3,17,180,8,17,1,18,1,18,1,18,1,18,3,18,186,8,18,1,18,1,18,1,18,5,
        18,191,8,18,10,18,12,18,194,9,18,1,19,1,19,1,19,1,19,3,19,200,8,
        19,1,19,1,19,1,19,5,19,205,8,19,10,19,12,19,208,9,19,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,3,20,217,8,20,1,20,1,20,1,20,3,20,222,8,20,
        1,20,1,20,1,20,5,20,227,8,20,10,20,12,20,230,9,20,1,21,1,21,1,21,
        5,21,235,8,21,10,21,12,21,238,9,21,1,22,1,22,1,22,1,22,5,22,244,
        8,22,10,22,12,22,247,9,22,1,23,1,23,1,23,0,3,36,38,40,24,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,8,1,
        0,7,8,1,0,17,18,1,0,19,20,1,0,31,32,1,0,22,23,1,0,31,33,1,0,25,30,
        1,0,31,34,253,0,48,1,0,0,0,2,52,1,0,0,0,4,57,1,0,0,0,6,63,1,0,0,
        0,8,67,1,0,0,0,10,70,1,0,0,0,12,81,1,0,0,0,14,84,1,0,0,0,16,93,1,
        0,0,0,18,95,1,0,0,0,20,100,1,0,0,0,22,106,1,0,0,0,24,112,1,0,0,0,
        26,126,1,0,0,0,28,145,1,0,0,0,30,163,1,0,0,0,32,172,1,0,0,0,34,179,
        1,0,0,0,36,181,1,0,0,0,38,195,1,0,0,0,40,221,1,0,0,0,42,231,1,0,
        0,0,44,239,1,0,0,0,46,248,1,0,0,0,48,49,3,2,1,0,49,50,3,4,2,0,50,
        51,6,0,-1,0,51,1,1,0,0,0,52,53,5,1,0,0,53,54,5,2,0,0,54,55,3,6,3,
        0,55,56,5,3,0,0,56,3,1,0,0,0,57,58,5,4,0,0,58,59,5,2,0,0,59,60,3,
        14,7,0,60,61,5,3,0,0,61,5,1,0,0,0,62,64,3,8,4,0,63,62,1,0,0,0,64,
        65,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,7,1,0,0,0,67,68,3,10,5,
        0,68,69,5,5,0,0,69,9,1,0,0,0,70,71,3,12,6,0,71,72,5,31,0,0,72,78,
        6,5,-1,0,73,74,5,6,0,0,74,75,5,31,0,0,75,77,6,5,-1,0,76,73,1,0,0,
        0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,11,1,0,0,0,80,78,
        1,0,0,0,81,82,7,0,0,0,82,13,1,0,0,0,83,85,3,16,8,0,84,83,1,0,0,0,
        85,86,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,15,1,0,0,0,88,94,3,
        18,9,0,89,94,3,20,10,0,90,94,3,22,11,0,91,94,3,24,12,0,92,94,3,26,
        13,0,93,88,1,0,0,0,93,89,1,0,0,0,93,90,1,0,0,0,93,91,1,0,0,0,93,
        92,1,0,0,0,94,17,1,0,0,0,95,96,5,31,0,0,96,97,5,9,0,0,97,98,3,28,
        14,0,98,99,5,5,0,0,99,19,1,0,0,0,100,101,5,10,0,0,101,102,5,11,0,
        0,102,103,3,42,21,0,103,104,5,12,0,0,104,105,5,5,0,0,105,21,1,0,
        0,0,106,107,5,13,0,0,107,108,5,11,0,0,108,109,3,44,22,0,109,110,
        5,12,0,0,110,111,5,5,0,0,111,23,1,0,0,0,112,113,5,14,0,0,113,114,
        5,11,0,0,114,115,3,34,17,0,115,116,5,12,0,0,116,117,5,2,0,0,117,
        118,3,14,7,0,118,124,5,3,0,0,119,120,5,15,0,0,120,121,5,2,0,0,121,
        122,3,14,7,0,122,123,5,3,0,0,123,125,1,0,0,0,124,119,1,0,0,0,124,
        125,1,0,0,0,125,25,1,0,0,0,126,127,5,16,0,0,127,128,5,11,0,0,128,
        129,3,34,17,0,129,130,5,12,0,0,130,131,5,2,0,0,131,132,3,14,7,0,
        132,133,5,3,0,0,133,27,1,0,0,0,134,139,3,30,15,0,135,136,7,1,0,0,
        136,138,3,30,15,0,137,135,1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,
        0,139,140,1,0,0,0,140,146,1,0,0,0,141,139,1,0,0,0,142,143,3,46,23,
        0,143,144,3,30,15,0,144,146,1,0,0,0,145,134,1,0,0,0,145,142,1,0,
        0,0,146,29,1,0,0,0,147,152,3,32,16,0,148,149,7,2,0,0,149,151,3,32,
        16,0,150,148,1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,152,153,1,0,
        0,0,153,164,1,0,0,0,154,152,1,0,0,0,155,160,7,3,0,0,156,157,5,21,
        0,0,157,159,7,3,0,0,158,156,1,0,0,0,159,162,1,0,0,0,160,158,1,0,
        0,0,160,161,1,0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,163,147,1,0,
        0,0,163,155,1,0,0,0,164,31,1,0,0,0,165,173,5,31,0,0,166,173,5,32,
        0,0,167,173,5,33,0,0,168,169,5,11,0,0,169,170,3,28,14,0,170,171,
        5,12,0,0,171,173,1,0,0,0,172,165,1,0,0,0,172,166,1,0,0,0,172,167,
        1,0,0,0,172,168,1,0,0,0,173,33,1,0,0,0,174,175,5,11,0,0,175,176,
        3,34,17,0,176,177,5,12,0,0,177,180,1,0,0,0,178,180,3,36,18,0,179,
        174,1,0,0,0,179,178,1,0,0,0,180,35,1,0,0,0,181,182,6,18,-1,0,182,
        185,3,38,19,0,183,184,5,22,0,0,184,186,3,38,19,0,185,183,1,0,0,0,
        185,186,1,0,0,0,186,192,1,0,0,0,187,188,10,1,0,0,188,189,5,22,0,
        0,189,191,3,36,18,0,190,187,1,0,0,0,191,194,1,0,0,0,192,190,1,0,
        0,0,192,193,1,0,0,0,193,37,1,0,0,0,194,192,1,0,0,0,195,196,6,19,
        -1,0,196,199,3,40,20,0,197,198,5,23,0,0,198,200,3,40,20,0,199,197,
        1,0,0,0,199,200,1,0,0,0,200,206,1,0,0,0,201,202,10,1,0,0,202,203,
        5,23,0,0,203,205,3,38,19,0,204,201,1,0,0,0,205,208,1,0,0,0,206,204,
        1,0,0,0,206,207,1,0,0,0,207,39,1,0,0,0,208,206,1,0,0,0,209,210,6,
        20,-1,0,210,211,5,24,0,0,211,222,3,40,20,4,212,213,5,11,0,0,213,
        216,3,40,20,0,214,215,7,4,0,0,215,217,3,40,20,0,216,214,1,0,0,0,
        216,217,1,0,0,0,217,218,1,0,0,0,218,219,5,12,0,0,219,222,1,0,0,0,
        220,222,7,5,0,0,221,209,1,0,0,0,221,212,1,0,0,0,221,220,1,0,0,0,
        222,228,1,0,0,0,223,224,10,2,0,0,224,225,7,6,0,0,225,227,3,40,20,
        0,226,223,1,0,0,0,227,230,1,0,0,0,228,226,1,0,0,0,228,229,1,0,0,
        0,229,41,1,0,0,0,230,228,1,0,0,0,231,236,7,7,0,0,232,233,5,6,0,0,
        233,235,7,7,0,0,234,232,1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,0,
        236,237,1,0,0,0,237,43,1,0,0,0,238,236,1,0,0,0,239,245,5,31,0,0,
        240,241,5,6,0,0,241,242,6,22,-1,0,242,244,5,31,0,0,243,240,1,0,0,
        0,244,247,1,0,0,0,245,243,1,0,0,0,245,246,1,0,0,0,246,45,1,0,0,0,
        247,245,1,0,0,0,248,249,7,1,0,0,249,47,1,0,0,0,21,65,78,86,93,124,
        139,145,152,160,163,172,179,185,192,199,206,216,221,228,236,245
    ]

class SimpAlgParser ( Parser ):

    grammarFileName = "SimpAlg.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'{'", "'}'", "'program'", "';'", 
                     "','", "'int'", "'float'", "'='", "'print'", "'('", 
                     "')'", "'scan'", "'if'", "'else'", "'while'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'or'", "'and'", "'!'", 
                     "'<'", "'>'", "'<='", "'>='", "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INT", 
                      "FLOAT", "STRING", "Comment", "WS" ]

    RULE_start = 0
    RULE_var = 1
    RULE_program = 2
    RULE_declaracoes = 3
    RULE_declaracao = 4
    RULE_lista_de_declaracao = 5
    RULE_tipo = 6
    RULE_comandos = 7
    RULE_comando = 8
    RULE_atribuicao = 9
    RULE_saida = 10
    RULE_entrada = 11
    RULE_condicional = 12
    RULE_repeticao = 13
    RULE_expressao = 14
    RULE_termo = 15
    RULE_fator = 16
    RULE_expressao_logica = 17
    RULE_or_expr = 18
    RULE_and_expr = 19
    RULE_relacional = 20
    RULE_lista_de_valores = 21
    RULE_lista_de_variaveis = 22
    RULE_op_unario = 23

    ruleNames =  [ "start", "var", "program", "declaracoes", "declaracao", 
                   "lista_de_declaracao", "tipo", "comandos", "comando", 
                   "atribuicao", "saida", "entrada", "condicional", "repeticao", 
                   "expressao", "termo", "fator", "expressao_logica", "or_expr", 
                   "and_expr", "relacional", "lista_de_valores", "lista_de_variaveis", 
                   "op_unario" ]

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



    st = SymbolTable()
    at = SemanticAnalyzer(st)



    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(SimpAlgParser.VarContext,0)


        def program(self):
            return self.getTypedRuleContext(SimpAlgParser.ProgramContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = SimpAlgParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.var()
            self.state = 49
            self.program()
            print(self.st.print_table())
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracoes(self):
            return self.getTypedRuleContext(SimpAlgParser.DeclaracoesContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = SimpAlgParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(SimpAlgParser.T__0)
            self.state = 53
            self.match(SimpAlgParser.T__1)
            self.state = 54
            self.declaracoes()
            self.state = 55
            self.match(SimpAlgParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comandos(self):
            return self.getTypedRuleContext(SimpAlgParser.ComandosContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SimpAlgParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(SimpAlgParser.T__3)
            self.state = 58
            self.match(SimpAlgParser.T__1)
            self.state = 59
            self.comandos()
            self.state = 60
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
        self.enterRule(localctx, 6, self.RULE_declaracoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self.declaracao()
                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7 or _la==8):
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

        def lista_de_declaracao(self):
            return self.getTypedRuleContext(SimpAlgParser.Lista_de_declaracaoContext,0)


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
        self.enterRule(localctx, 8, self.RULE_declaracao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.lista_de_declaracao()
            self.state = 68
            self.match(SimpAlgParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_de_declaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.t = None # TipoContext
            self._ID = None # Token

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SimpAlgParser.ID)
            else:
                return self.getToken(SimpAlgParser.ID, i)

        def tipo(self):
            return self.getTypedRuleContext(SimpAlgParser.TipoContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_lista_de_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_de_declaracao" ):
                listener.enterLista_de_declaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_de_declaracao" ):
                listener.exitLista_de_declaracao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_de_declaracao" ):
                return visitor.visitLista_de_declaracao(self)
            else:
                return visitor.visitChildren(self)




    def lista_de_declaracao(self):

        localctx = SimpAlgParser.Lista_de_declaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_lista_de_declaracao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            localctx.t = self.tipo()
            self.state = 71
            localctx._ID = self.match(SimpAlgParser.ID)
            self.at.create(localctx._ID, (None if localctx.t is None else self._input.getText(localctx.t.start,localctx.t.stop)))
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 73
                self.match(SimpAlgParser.T__5)
                self.state = 74
                localctx._ID = self.match(SimpAlgParser.ID)
                self.at.create(localctx._ID, (None if localctx.t is None else self._input.getText(localctx.t.start,localctx.t.stop)))
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 12, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
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
        self.enterRule(localctx, 14, self.RULE_comandos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 83
                self.comando()
                self.state = 86 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2147574784) != 0)):
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
        self.enterRule(localctx, 16, self.RULE_comando)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.atribuicao()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.saida()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.entrada()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.condicional()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 92
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
        self.enterRule(localctx, 18, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(SimpAlgParser.ID)
            self.state = 96
            self.match(SimpAlgParser.T__8)
            self.state = 97
            self.expressao()
            self.state = 98
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
        self.enterRule(localctx, 20, self.RULE_saida)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(SimpAlgParser.T__9)
            self.state = 101
            self.match(SimpAlgParser.T__10)
            self.state = 102
            self.lista_de_valores()
            self.state = 103
            self.match(SimpAlgParser.T__11)
            self.state = 104
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
        self.enterRule(localctx, 22, self.RULE_entrada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(SimpAlgParser.T__12)
            self.state = 107
            self.match(SimpAlgParser.T__10)
            self.state = 108
            self.lista_de_variaveis()
            self.state = 109
            self.match(SimpAlgParser.T__11)
            self.state = 110
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
        self.enterRule(localctx, 24, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(SimpAlgParser.T__13)
            self.state = 113
            self.match(SimpAlgParser.T__10)
            self.state = 114
            self.expressao_logica()
            self.state = 115
            self.match(SimpAlgParser.T__11)
            self.state = 116
            self.match(SimpAlgParser.T__1)
            self.state = 117
            self.comandos()
            self.state = 118
            self.match(SimpAlgParser.T__2)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 119
                self.match(SimpAlgParser.T__14)
                self.state = 120
                self.match(SimpAlgParser.T__1)
                self.state = 121
                self.comandos()
                self.state = 122
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
        self.enterRule(localctx, 26, self.RULE_repeticao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(SimpAlgParser.T__15)
            self.state = 127
            self.match(SimpAlgParser.T__10)
            self.state = 128
            self.expressao_logica()
            self.state = 129
            self.match(SimpAlgParser.T__11)
            self.state = 130
            self.match(SimpAlgParser.T__1)
            self.state = 131
            self.comandos()
            self.state = 132
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
        self.enterRule(localctx, 28, self.RULE_expressao)
        self._la = 0 # Token type
        try:
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 31, 32, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.termo()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==17 or _la==18:
                    self.state = 135
                    _la = self._input.LA(1)
                    if not(_la==17 or _la==18):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 136
                    self.termo()
                    self.state = 141
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [17, 18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.op_unario()
                self.state = 143
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
        self.enterRule(localctx, 30, self.RULE_termo)
        self._la = 0 # Token type
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.fator()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==19 or _la==20:
                    self.state = 148
                    _la = self._input.LA(1)
                    if not(_la==19 or _la==20):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 149
                    self.fator()
                    self.state = 154
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                _la = self._input.LA(1)
                if not(_la==31 or _la==32):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==21:
                    self.state = 156
                    self.match(SimpAlgParser.T__20)
                    self.state = 157
                    _la = self._input.LA(1)
                    if not(_la==31 or _la==32):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 162
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
        self.enterRule(localctx, 32, self.RULE_fator)
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(SimpAlgParser.ID)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(SimpAlgParser.INT)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 167
                self.match(SimpAlgParser.FLOAT)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 168
                self.match(SimpAlgParser.T__10)
                self.state = 169
                self.expressao()
                self.state = 170
                self.match(SimpAlgParser.T__11)
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
        self.enterRule(localctx, 34, self.RULE_expressao_logica)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(SimpAlgParser.T__10)
                self.state = 175
                self.expressao_logica()
                self.state = 176
                self.match(SimpAlgParser.T__11)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_or_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.and_expr(0)
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 183
                self.match(SimpAlgParser.T__21)
                self.state = 184
                self.and_expr(0)


            self._ctx.stop = self._input.LT(-1)
            self.state = 192
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpAlgParser.Or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_or_expr)
                    self.state = 187
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")

                    self.state = 188
                    self.match(SimpAlgParser.T__21)
                    self.state = 189
                    self.or_expr(0) 
                self.state = 194
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_and_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.relacional(0)
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 197
                self.match(SimpAlgParser.T__22)
                self.state = 198
                self.relacional(0)


            self._ctx.stop = self._input.LT(-1)
            self.state = 206
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpAlgParser.And_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_expr)
                    self.state = 201
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")

                    self.state = 202
                    self.match(SimpAlgParser.T__22)
                    self.state = 203
                    self.and_expr(0) 
                self.state = 208
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_relacional, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.state = 210
                self.match(SimpAlgParser.T__23)
                self.state = 211
                self.relacional(4)
                pass
            elif token in [11]:
                self.state = 212
                self.match(SimpAlgParser.T__10)
                self.state = 213
                self.relacional(0)
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==22 or _la==23:
                    self.state = 214
                    _la = self._input.LA(1)
                    if not(_la==22 or _la==23):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 215
                    self.relacional(0)


                self.state = 218
                self.match(SimpAlgParser.T__11)
                pass
            elif token in [31, 32, 33]:
                self.state = 220
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
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpAlgParser.RelacionalContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relacional)
                    self.state = 223
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 224
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2113929216) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 225
                    self.relacional(0) 
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        self.enterRule(localctx, 42, self.RULE_lista_de_valores)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 232
                self.match(SimpAlgParser.T__5)
                self.state = 233
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 238
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
        self.enterRule(localctx, 44, self.RULE_lista_de_variaveis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(SimpAlgParser.ID)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 240
                self.match(SimpAlgParser.T__5)

                self.state = 242
                self.match(SimpAlgParser.ID)
                self.state = 247
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
        self.enterRule(localctx, 46, self.RULE_op_unario)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
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
        self._predicates[18] = self.or_expr_sempred
        self._predicates[19] = self.and_expr_sempred
        self._predicates[20] = self.relacional_sempred
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
         




