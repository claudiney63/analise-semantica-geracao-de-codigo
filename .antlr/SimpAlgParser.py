# Generated from c:/Users/vinic/Documents/GitHub/analise-semantica-geracao-de-codigo/SimpAlg.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from SemanticAnalyser import *
from CodeGenerator import *

def serializedATN():
    return [
        4,1,36,367,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,5,3,67,8,3,10,3,12,3,
        70,9,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,81,8,5,10,5,12,5,
        84,9,5,1,6,1,6,1,7,1,7,1,7,1,7,5,7,92,8,7,10,7,12,7,95,9,7,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,112,8,
        8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,5,10,134,8,10,10,10,12,10,137,9,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,146,8,10,1,11,1,11,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,161,8,12,10,
        12,12,12,164,9,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,173,8,
        12,10,12,12,12,176,9,12,3,12,178,8,12,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,196,8,
        13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,3,
        15,210,8,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,218,8,15,5,15,220,
        8,15,10,15,12,15,223,9,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,
        1,17,1,17,1,17,1,17,5,17,237,8,17,10,17,12,17,240,9,17,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,265,8,18,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,3,20,296,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        3,21,307,8,21,1,21,1,21,1,21,1,21,1,21,1,21,5,21,315,8,21,10,21,
        12,21,318,9,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,
        329,8,22,1,22,1,22,1,22,1,22,1,22,1,22,5,22,337,8,22,10,22,12,22,
        340,9,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,3,23,359,8,23,1,24,1,24,1,24,1,24,
        3,24,365,8,24,1,24,0,2,42,44,25,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,0,5,1,0,7,8,1,0,10,11,1,0,12,
        13,1,0,31,32,1,0,25,30,374,0,50,1,0,0,0,2,54,1,0,0,0,4,59,1,0,0,
        0,6,68,1,0,0,0,8,71,1,0,0,0,10,74,1,0,0,0,12,85,1,0,0,0,14,87,1,
        0,0,0,16,111,1,0,0,0,18,113,1,0,0,0,20,145,1,0,0,0,22,147,1,0,0,
        0,24,177,1,0,0,0,26,195,1,0,0,0,28,197,1,0,0,0,30,209,1,0,0,0,32,
        224,1,0,0,0,34,231,1,0,0,0,36,241,1,0,0,0,38,266,1,0,0,0,40,295,
        1,0,0,0,42,297,1,0,0,0,44,319,1,0,0,0,46,358,1,0,0,0,48,364,1,0,
        0,0,50,51,3,2,1,0,51,52,3,4,2,0,52,53,6,0,-1,0,53,1,1,0,0,0,54,55,
        5,1,0,0,55,56,5,2,0,0,56,57,3,6,3,0,57,58,5,3,0,0,58,3,1,0,0,0,59,
        60,5,4,0,0,60,61,5,2,0,0,61,62,3,14,7,0,62,63,5,3,0,0,63,64,6,2,
        -1,0,64,5,1,0,0,0,65,67,3,8,4,0,66,65,1,0,0,0,67,70,1,0,0,0,68,66,
        1,0,0,0,68,69,1,0,0,0,69,7,1,0,0,0,70,68,1,0,0,0,71,72,3,10,5,0,
        72,73,5,5,0,0,73,9,1,0,0,0,74,75,3,12,6,0,75,76,5,31,0,0,76,82,6,
        5,-1,0,77,78,5,6,0,0,78,79,5,31,0,0,79,81,6,5,-1,0,80,77,1,0,0,0,
        81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,11,1,0,0,0,84,82,1,
        0,0,0,85,86,7,0,0,0,86,13,1,0,0,0,87,93,6,7,-1,0,88,89,3,16,8,0,
        89,90,6,7,-1,0,90,92,1,0,0,0,91,88,1,0,0,0,92,95,1,0,0,0,93,91,1,
        0,0,0,93,94,1,0,0,0,94,15,1,0,0,0,95,93,1,0,0,0,96,97,3,18,9,0,97,
        98,6,8,-1,0,98,112,1,0,0,0,99,100,3,28,14,0,100,101,6,8,-1,0,101,
        112,1,0,0,0,102,103,3,32,16,0,103,104,6,8,-1,0,104,112,1,0,0,0,105,
        106,3,36,18,0,106,107,6,8,-1,0,107,112,1,0,0,0,108,109,3,38,19,0,
        109,110,6,8,-1,0,110,112,1,0,0,0,111,96,1,0,0,0,111,99,1,0,0,0,111,
        102,1,0,0,0,111,105,1,0,0,0,111,108,1,0,0,0,112,17,1,0,0,0,113,114,
        5,31,0,0,114,115,6,9,-1,0,115,116,5,9,0,0,116,117,3,20,10,0,117,
        118,5,5,0,0,118,119,6,9,-1,0,119,120,6,9,-1,0,120,121,6,9,-1,0,121,
        19,1,0,0,0,122,123,3,24,12,0,123,124,6,10,-1,0,124,125,6,10,-1,0,
        125,135,6,10,-1,0,126,127,7,1,0,0,127,128,3,24,12,0,128,129,6,10,
        -1,0,129,130,6,10,-1,0,130,131,6,10,-1,0,131,132,6,10,-1,0,132,134,
        1,0,0,0,133,126,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,
        1,0,0,0,136,146,1,0,0,0,137,135,1,0,0,0,138,139,3,22,11,0,139,140,
        3,24,12,0,140,141,6,10,-1,0,141,142,6,10,-1,0,142,143,6,10,-1,0,
        143,144,6,10,-1,0,144,146,1,0,0,0,145,122,1,0,0,0,145,138,1,0,0,
        0,146,21,1,0,0,0,147,148,7,1,0,0,148,23,1,0,0,0,149,150,3,26,13,
        0,150,151,6,12,-1,0,151,152,6,12,-1,0,152,162,6,12,-1,0,153,154,
        7,2,0,0,154,155,3,26,13,0,155,156,6,12,-1,0,156,157,6,12,-1,0,157,
        158,6,12,-1,0,158,159,6,12,-1,0,159,161,1,0,0,0,160,153,1,0,0,0,
        161,164,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,178,1,0,0,0,
        164,162,1,0,0,0,165,166,7,3,0,0,166,167,6,12,-1,0,167,168,6,12,-1,
        0,168,174,6,12,-1,0,169,170,5,14,0,0,170,171,7,3,0,0,171,173,6,12,
        -1,0,172,169,1,0,0,0,173,176,1,0,0,0,174,172,1,0,0,0,174,175,1,0,
        0,0,175,178,1,0,0,0,176,174,1,0,0,0,177,149,1,0,0,0,177,165,1,0,
        0,0,178,25,1,0,0,0,179,180,5,31,0,0,180,181,6,13,-1,0,181,182,6,
        13,-1,0,182,196,6,13,-1,0,183,184,5,32,0,0,184,185,6,13,-1,0,185,
        186,6,13,-1,0,186,196,6,13,-1,0,187,188,5,33,0,0,188,196,6,13,-1,
        0,189,190,5,15,0,0,190,191,3,20,10,0,191,192,6,13,-1,0,192,193,6,
        13,-1,0,193,194,5,16,0,0,194,196,1,0,0,0,195,179,1,0,0,0,195,183,
        1,0,0,0,195,187,1,0,0,0,195,189,1,0,0,0,196,27,1,0,0,0,197,198,5,
        17,0,0,198,199,5,15,0,0,199,200,3,30,15,0,200,201,5,16,0,0,201,202,
        5,5,0,0,202,203,6,14,-1,0,203,29,1,0,0,0,204,205,5,31,0,0,205,210,
        6,15,-1,0,206,210,5,32,0,0,207,210,5,33,0,0,208,210,5,34,0,0,209,
        204,1,0,0,0,209,206,1,0,0,0,209,207,1,0,0,0,209,208,1,0,0,0,210,
        221,1,0,0,0,211,217,5,6,0,0,212,213,5,31,0,0,213,218,6,15,-1,0,214,
        218,5,32,0,0,215,218,5,33,0,0,216,218,5,34,0,0,217,212,1,0,0,0,217,
        214,1,0,0,0,217,215,1,0,0,0,217,216,1,0,0,0,218,220,1,0,0,0,219,
        211,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,221,222,1,0,0,0,222,
        31,1,0,0,0,223,221,1,0,0,0,224,225,5,18,0,0,225,226,5,15,0,0,226,
        227,3,34,17,0,227,228,5,16,0,0,228,229,5,5,0,0,229,230,6,16,-1,0,
        230,33,1,0,0,0,231,232,5,31,0,0,232,238,6,17,-1,0,233,234,5,6,0,
        0,234,235,5,31,0,0,235,237,6,17,-1,0,236,233,1,0,0,0,237,240,1,0,
        0,0,238,236,1,0,0,0,238,239,1,0,0,0,239,35,1,0,0,0,240,238,1,0,0,
        0,241,242,5,19,0,0,242,243,5,15,0,0,243,244,3,40,20,0,244,245,5,
        16,0,0,245,246,5,2,0,0,246,247,3,14,7,0,247,248,5,3,0,0,248,249,
        6,18,-1,0,249,250,6,18,-1,0,250,251,6,18,-1,0,251,264,6,18,-1,0,
        252,253,5,20,0,0,253,254,5,2,0,0,254,255,3,14,7,0,255,256,5,3,0,
        0,256,257,6,18,-1,0,257,258,6,18,-1,0,258,259,6,18,-1,0,259,260,
        6,18,-1,0,260,261,6,18,-1,0,261,262,6,18,-1,0,262,263,6,18,-1,0,
        263,265,1,0,0,0,264,252,1,0,0,0,264,265,1,0,0,0,265,37,1,0,0,0,266,
        267,5,21,0,0,267,268,5,15,0,0,268,269,3,40,20,0,269,270,5,16,0,0,
        270,271,5,2,0,0,271,272,3,14,7,0,272,273,5,3,0,0,273,274,6,19,-1,
        0,274,275,6,19,-1,0,275,276,6,19,-1,0,276,277,6,19,-1,0,277,278,
        6,19,-1,0,278,279,6,19,-1,0,279,280,6,19,-1,0,280,281,6,19,-1,0,
        281,282,6,19,-1,0,282,283,6,19,-1,0,283,284,6,19,-1,0,284,39,1,0,
        0,0,285,286,5,15,0,0,286,287,3,40,20,0,287,288,5,16,0,0,288,289,
        6,20,-1,0,289,290,6,20,-1,0,290,296,1,0,0,0,291,292,3,42,21,0,292,
        293,6,20,-1,0,293,294,6,20,-1,0,294,296,1,0,0,0,295,285,1,0,0,0,
        295,291,1,0,0,0,296,41,1,0,0,0,297,298,6,21,-1,0,298,299,3,44,22,
        0,299,300,6,21,-1,0,300,306,6,21,-1,0,301,302,5,22,0,0,302,303,3,
        44,22,0,303,304,6,21,-1,0,304,305,6,21,-1,0,305,307,1,0,0,0,306,
        301,1,0,0,0,306,307,1,0,0,0,307,316,1,0,0,0,308,309,10,1,0,0,309,
        310,5,22,0,0,310,311,3,42,21,2,311,312,6,21,-1,0,312,313,6,21,-1,
        0,313,315,1,0,0,0,314,308,1,0,0,0,315,318,1,0,0,0,316,314,1,0,0,
        0,316,317,1,0,0,0,317,43,1,0,0,0,318,316,1,0,0,0,319,320,6,22,-1,
        0,320,321,3,46,23,0,321,322,6,22,-1,0,322,328,6,22,-1,0,323,324,
        5,23,0,0,324,325,3,46,23,0,325,326,6,22,-1,0,326,327,6,22,-1,0,327,
        329,1,0,0,0,328,323,1,0,0,0,328,329,1,0,0,0,329,338,1,0,0,0,330,
        331,10,1,0,0,331,332,5,23,0,0,332,333,3,44,22,2,333,334,6,22,-1,
        0,334,335,6,22,-1,0,335,337,1,0,0,0,336,330,1,0,0,0,337,340,1,0,
        0,0,338,336,1,0,0,0,338,339,1,0,0,0,339,45,1,0,0,0,340,338,1,0,0,
        0,341,342,5,24,0,0,342,343,3,46,23,0,343,344,6,23,-1,0,344,345,6,
        23,-1,0,345,359,1,0,0,0,346,347,5,15,0,0,347,348,3,40,20,0,348,349,
        5,16,0,0,349,350,6,23,-1,0,350,351,6,23,-1,0,351,359,1,0,0,0,352,
        353,3,48,24,0,353,354,7,4,0,0,354,355,3,48,24,0,355,356,6,23,-1,
        0,356,357,6,23,-1,0,357,359,1,0,0,0,358,341,1,0,0,0,358,346,1,0,
        0,0,358,352,1,0,0,0,359,47,1,0,0,0,360,361,5,31,0,0,361,365,6,24,
        -1,0,362,365,5,32,0,0,363,365,5,33,0,0,364,360,1,0,0,0,364,362,1,
        0,0,0,364,363,1,0,0,0,365,49,1,0,0,0,22,68,82,93,111,135,145,162,
        174,177,195,209,217,221,238,264,295,306,316,328,338,358,364
    ]

class SimpAlgParser ( Parser ):

    grammarFileName = "SimpAlg.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'{'", "'}'", "'program'", "';'", 
                     "','", "'int'", "'float'", "'='", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'('", "')'", "'print'", "'scan'", "'if'", 
                     "'else'", "'while'", "'or'", "'and'", "'!'", "'<'", 
                     "'>'", "'<='", "'>='", "'=='", "'!='" ]

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
    RULE_expressao = 10
    RULE_op_unario = 11
    RULE_termo = 12
    RULE_fator = 13
    RULE_saida = 14
    RULE_lista_de_valores = 15
    RULE_entrada = 16
    RULE_lista_de_variaveis = 17
    RULE_condicional = 18
    RULE_repeticao = 19
    RULE_expressao_logica = 20
    RULE_or_expr = 21
    RULE_and_expr = 22
    RULE_relacional = 23
    RULE_terminal = 24

    ruleNames =  [ "start", "var", "program", "declaracoes", "declaracao", 
                   "lista_de_declaracao", "tipo", "comandos", "comando", 
                   "atribuicao", "expressao", "op_unario", "termo", "fator", 
                   "saida", "lista_de_valores", "entrada", "lista_de_variaveis", 
                   "condicional", "repeticao", "expressao_logica", "or_expr", 
                   "and_expr", "relacional", "terminal" ]

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
    cg = CodeGenerator()



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




    def start(self):

        localctx = SimpAlgParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.var()
            self.state = 51
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




    def var(self):

        localctx = SimpAlgParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(SimpAlgParser.T__0)
            self.state = 55
            self.match(SimpAlgParser.T__1)
            self.state = 56
            self.declaracoes()
            self.state = 57
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
            self._comandos = None # ComandosContext

        def comandos(self):
            return self.getTypedRuleContext(SimpAlgParser.ComandosContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_program




    def program(self):

        localctx = SimpAlgParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(SimpAlgParser.T__3)
            self.state = 60
            self.match(SimpAlgParser.T__1)
            self.state = 61
            localctx._comandos = self.comandos()
            self.state = 62
            self.match(SimpAlgParser.T__2)

            with open('example.py', 'w') as file:
                file.write("\nfrom goto import with_goto\n")
                print("\nfrom goto import with_goto")
                
                file.write("@with_goto\n")
                print("@with_goto")
                
                file.write("def main():")
                print("def main():", end="")
                
                file.write((localctx._comandos.code).replace("\n\t\n\t", "\n\t") + "\n")
                print((localctx._comandos.code).replace("\n\t\n\t", "\n\t"))
                
                file.write("main()")
                print("main()")

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




    def declaracoes(self):

        localctx = SimpAlgParser.DeclaracoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 65
                self.declaracao()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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




    def declaracao(self):

        localctx = SimpAlgParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaracao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.lista_de_declaracao()
            self.state = 72
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




    def lista_de_declaracao(self):

        localctx = SimpAlgParser.Lista_de_declaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_lista_de_declaracao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            localctx.t = self.tipo()
            self.state = 75
            localctx._ID = self.match(SimpAlgParser.ID)
            self.at.create(localctx._ID, (None if localctx.t is None else self._input.getText(localctx.t.start,localctx.t.stop)))
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 77
                self.match(SimpAlgParser.T__5)
                self.state = 78
                localctx._ID = self.match(SimpAlgParser.ID)
                self.at.create(localctx._ID, (None if localctx.t is None else self._input.getText(localctx.t.start,localctx.t.stop)))
                self.state = 84
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




    def tipo(self):

        localctx = SimpAlgParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
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
            self.code = None
            self._comando = None # ComandoContext

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.ComandoContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.ComandoContext,i)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_comandos




    def comandos(self):

        localctx = SimpAlgParser.ComandosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comandos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx.code =  ''
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2150498304) != 0):
                self.state = 88
                localctx._comando = self.comando()
                localctx.code =  localctx.code + '\n\t' + localctx._comando.code
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.code = None
            self._atribuicao = None # AtribuicaoContext
            self._saida = None # SaidaContext
            self._entrada = None # EntradaContext
            self._condicional = None # CondicionalContext
            self._repeticao = None # RepeticaoContext

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




    def comando(self):

        localctx = SimpAlgParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comando)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                localctx._atribuicao = self.atribuicao()
                localctx.code = localctx._atribuicao.code
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                localctx._saida = self.saida()
                localctx.code = localctx._saida.code
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 102
                localctx._entrada = self.entrada()
                localctx.code = localctx._entrada.code
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 105
                localctx._condicional = self.condicional()
                localctx.code = localctx._condicional.code
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 108
                localctx._repeticao = self.repeticao()
                localctx.code = localctx._repeticao.code
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
            self.code = None
            self._ID = None # Token
            self._expressao = None # ExpressaoContext

        def ID(self):
            return self.getToken(SimpAlgParser.ID, 0)

        def expressao(self):
            return self.getTypedRuleContext(SimpAlgParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_atribuicao




    def atribuicao(self):

        localctx = SimpAlgParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            localctx._ID = self.match(SimpAlgParser.ID)
            self.at.isDeclared(localctx._ID)
            self.state = 115
            self.match(SimpAlgParser.T__8)
            self.state = 116
            localctx._expressao = self.expressao()
            self.state = 117
            self.match(SimpAlgParser.T__4)
            self.at.assign(localctx._ID, (None if localctx._expressao is None else self._input.getText(localctx._expressao.start,localctx._expressao.stop)))
            if not(localctx._expressao.code == ""): localctx._expressao.code = localctx._expressao.code + "\n\t"
            localctx.code = localctx._expressao.code + (None if localctx._ID is None else localctx._ID.text) + " = " +  localctx._expressao.variavel
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
            self.val = None
            self.code = None
            self.variavel = None
            self.variavelAnterior = None
            self.t1 = None # TermoContext
            self.op = None # Token
            self.t2 = None # TermoContext
            self.opU = None # Op_unarioContext
            self._termo = None # TermoContext

        def termo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.TermoContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.TermoContext,i)


        def op_unario(self):
            return self.getTypedRuleContext(SimpAlgParser.Op_unarioContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_expressao




    def expressao(self):

        localctx = SimpAlgParser.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expressao)
        self._la = 0 # Token type
        try:
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 31, 32, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                localctx.t1 = self.termo()
                localctx.val = (None if localctx.t1 is None else self._input.getText(localctx.t1.start,localctx.t1.stop))
                localctx.code = localctx.t1.code
                localctx.variavel = localctx.t1.variavel
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10 or _la==11:
                    self.state = 126
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==10 or _la==11):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 127
                    localctx.t2 = self.termo()
                    localctx.val = (None if localctx.t1 is None else self._input.getText(localctx.t1.start,localctx.t1.stop)) + (None if localctx.op is None else localctx.op.text) + (None if localctx.t2 is None else self._input.getText(localctx.t2.start,localctx.t2.stop))
                    localctx.variavelAnterior = localctx.variavel
                    localctx.variavel = self.cg.new_temp()
                    localctx.code = localctx.code + localctx.t2.code + "\n\t" + localctx.variavel + " = " +  localctx.variavelAnterior + " " + (None if localctx.op is None else localctx.op.text) + " " + localctx.t2.variavel
                    self.state = 137
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [10, 11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                localctx.opU = self.op_unario()
                self.state = 139
                localctx._termo = self.termo()
                localctx.val = (None if localctx.opU is None else self._input.getText(localctx.opU.start,localctx.opU.stop)) + (None if localctx._termo is None else self._input.getText(localctx._termo.start,localctx._termo.stop))
                localctx.variavelAnterior = localctx.variavel
                localctx.variavel = self.cg.new_temp()
                localctx.code = localctx.variavel + " = " + (None if localctx.opU is None else self._input.getText(localctx.opU.start,localctx.opU.stop)) + localctx._termo.variavel
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


    class Op_unarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpAlgParser.RULE_op_unario




    def op_unario(self):

        localctx = SimpAlgParser.Op_unarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_op_unario)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
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


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.val = None
            self.code = None
            self.variavel = None
            self.variavelAnterior = None
            self.f1 = None # FatorContext
            self.op = None # Token
            self.f2 = None # FatorContext
            self.type1 = None # Token
            self.type2 = None # Token

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




    def termo(self):

        localctx = SimpAlgParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_termo)
        self._la = 0 # Token type
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                localctx.f1 = self.fator()
                localctx.val = (None if localctx.f1 is None else self._input.getText(localctx.f1.start,localctx.f1.stop))
                localctx.code = localctx.f1.code
                localctx.variavel = localctx.f1.variavel
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12 or _la==13:
                    self.state = 153
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==12 or _la==13):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 154
                    localctx.f2 = self.fator()
                    localctx.val = (None if localctx.f1 is None else self._input.getText(localctx.f1.start,localctx.f1.stop)) + (None if localctx.op is None else localctx.op.text) + (None if localctx.f2 is None else self._input.getText(localctx.f2.start,localctx.f2.stop))
                    localctx.variavelAnterior = localctx.variavel
                    localctx.variavel = self.cg.new_temp()
                    localctx.code = localctx.code + localctx.f2.code + "\n\t" + localctx.variavel + " = " +  localctx.variavelAnterior + " " + (None if localctx.op is None else localctx.op.text) + " " + localctx.f2.variavel
                    self.state = 164
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                localctx.type1 = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==31 or _la==32):
                    localctx.type1 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.val = (None if localctx.type1 is None else localctx.type1.text)
                localctx.code = ""
                localctx.variavel = (None if localctx.type1 is None else localctx.type1.text)
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 169
                    self.match(SimpAlgParser.T__13)
                    self.state = 170
                    localctx.type2 = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==31 or _la==32):
                        localctx.type2 = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    localctx.val = (None if localctx.type1 is None else localctx.type1.text) + " % " + (None if localctx.type2 is None else localctx.type2.text)
                    self.state = 176
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
            self.val = None
            self.code = None
            self.variavel = None
            self._ID = None # Token
            self._INT = None # Token
            self._FLOAT = None # Token
            self._expressao = None # ExpressaoContext

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




    def fator(self):

        localctx = SimpAlgParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_fator)
        try:
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                localctx._ID = self.match(SimpAlgParser.ID)
                self.at.isDeclared(localctx._ID)
                localctx.code = ""
                localctx.variavel = (None if localctx._ID is None else localctx._ID.text)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                localctx._INT = self.match(SimpAlgParser.INT)
                localctx.val = (None if localctx._INT is None else localctx._INT.text)
                localctx.code = ""
                localctx.variavel = (None if localctx._INT is None else localctx._INT.text)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                localctx._FLOAT = self.match(SimpAlgParser.FLOAT)
                localctx.val = (None if localctx._FLOAT is None else localctx._FLOAT.text)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 189
                self.match(SimpAlgParser.T__14)
                self.state = 190
                localctx._expressao = self.expressao()
                localctx.code = localctx._expressao.code
                localctx.variavel = localctx._expressao.variavel
                self.state = 193
                self.match(SimpAlgParser.T__15)
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


    class SaidaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.code = None
            self._lista_de_valores = None # Lista_de_valoresContext

        def lista_de_valores(self):
            return self.getTypedRuleContext(SimpAlgParser.Lista_de_valoresContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_saida




    def saida(self):

        localctx = SimpAlgParser.SaidaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_saida)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(SimpAlgParser.T__16)
            self.state = 198
            self.match(SimpAlgParser.T__14)
            self.state = 199
            localctx._lista_de_valores = self.lista_de_valores()
            self.state = 200
            self.match(SimpAlgParser.T__15)
            self.state = 201
            self.match(SimpAlgParser.T__4)
            localctx.code = 'print(' + localctx._lista_de_valores.code + ')'
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
            self.code = None
            self._ID = None # Token

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




    def lista_de_valores(self):

        localctx = SimpAlgParser.Lista_de_valoresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_lista_de_valores)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.state = 204
                localctx._ID = self.match(SimpAlgParser.ID)
                self.at.isDeclared(localctx._ID); localctx.code = (None if localctx._ID is None else localctx._ID.text) 
                pass
            elif token in [32]:
                self.state = 206
                self.match(SimpAlgParser.INT)
                pass
            elif token in [33]:
                self.state = 207
                self.match(SimpAlgParser.FLOAT)
                pass
            elif token in [34]:
                self.state = 208
                self.match(SimpAlgParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 211
                self.match(SimpAlgParser.T__5)
                self.state = 217
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [31]:
                    self.state = 212
                    localctx._ID = self.match(SimpAlgParser.ID)
                    self.at.isDeclared(localctx._ID); localctx.code = localctx.code + ', ' + (None if localctx._ID is None else localctx._ID.text)
                    pass
                elif token in [32]:
                    self.state = 214
                    self.match(SimpAlgParser.INT)
                    pass
                elif token in [33]:
                    self.state = 215
                    self.match(SimpAlgParser.FLOAT)
                    pass
                elif token in [34]:
                    self.state = 216
                    self.match(SimpAlgParser.STRING)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.code = None
            self._lista_de_variaveis = None # Lista_de_variaveisContext

        def lista_de_variaveis(self):
            return self.getTypedRuleContext(SimpAlgParser.Lista_de_variaveisContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_entrada




    def entrada(self):

        localctx = SimpAlgParser.EntradaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_entrada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(SimpAlgParser.T__17)
            self.state = 225
            self.match(SimpAlgParser.T__14)
            self.state = 226
            localctx._lista_de_variaveis = self.lista_de_variaveis()
            self.state = 227
            self.match(SimpAlgParser.T__15)
            self.state = 228
            self.match(SimpAlgParser.T__4)
            localctx.code = localctx._lista_de_variaveis.code + ' = input("input: ").split()'
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
            self.code = None
            self._ID = None # Token

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SimpAlgParser.ID)
            else:
                return self.getToken(SimpAlgParser.ID, i)

        def getRuleIndex(self):
            return SimpAlgParser.RULE_lista_de_variaveis




    def lista_de_variaveis(self):

        localctx = SimpAlgParser.Lista_de_variaveisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_lista_de_variaveis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            localctx._ID = self.match(SimpAlgParser.ID)
            self.at.isDeclared(localctx._ID); localctx.code = (None if localctx._ID is None else localctx._ID.text)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 233
                self.match(SimpAlgParser.T__5)
                self.state = 234
                localctx._ID = self.match(SimpAlgParser.ID)
                self.at.isDeclared(localctx._ID); localctx.code = localctx.code + ', ' + (None if localctx._ID is None else localctx._ID.text)
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.code = None
            self.labelif = None
            self.labelelse = None
            self._expressao_logica = None # Expressao_logicaContext
            self.cif = None # ComandosContext
            self.celse = None # ComandosContext

        def expressao_logica(self):
            return self.getTypedRuleContext(SimpAlgParser.Expressao_logicaContext,0)


        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.ComandosContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.ComandosContext,i)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_condicional




    def condicional(self):

        localctx = SimpAlgParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(SimpAlgParser.T__18)
            self.state = 242
            self.match(SimpAlgParser.T__14)
            self.state = 243
            localctx._expressao_logica = self.expressao_logica()
            self.state = 244
            self.match(SimpAlgParser.T__15)
            self.state = 245
            self.match(SimpAlgParser.T__1)
            self.state = 246
            localctx.cif = self.comandos()
            self.state = 247
            self.match(SimpAlgParser.T__2)
            localctx.labelif = self.cg.new_label()
            localctx.code = localctx._expressao_logica.code + "\n\t"
            localctx.code = localctx.code + "if " + localctx._expressao_logica.variavel + " : goto " + localctx.labelif + "\n\t"
            localctx.code = localctx.code + "label "+ localctx.labelif + localctx.cif.code 
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 252
                self.match(SimpAlgParser.T__19)
                self.state = 253
                self.match(SimpAlgParser.T__1)
                self.state = 254
                localctx.celse = self.comandos()
                self.state = 255
                self.match(SimpAlgParser.T__2)
                localctx.labelelse = self.cg.new_label()
                localctx.code = localctx._expressao_logica.code + "\n\t"
                localctx.code = localctx.code + "if " + localctx._expressao_logica.variavel + " : goto " + localctx.labelif
                localctx.code = localctx.code + localctx.celse.code + "\n\t"
                localctx.code = localctx.code + "goto " + localctx.labelelse + "\n\t"
                localctx.code = localctx.code + "label "+ localctx.labelif + localctx.cif.code + "\n\t"
                localctx.code = localctx.code + "label " + localctx.labelelse 


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
            self.code = None
            self.whilelabel = None
            self.iflabel = None
            self.endlabel = None
            self._expressao_logica = None # Expressao_logicaContext
            self._comandos = None # ComandosContext

        def expressao_logica(self):
            return self.getTypedRuleContext(SimpAlgParser.Expressao_logicaContext,0)


        def comandos(self):
            return self.getTypedRuleContext(SimpAlgParser.ComandosContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_repeticao




    def repeticao(self):

        localctx = SimpAlgParser.RepeticaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_repeticao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(SimpAlgParser.T__20)
            self.state = 267
            self.match(SimpAlgParser.T__14)
            self.state = 268
            localctx._expressao_logica = self.expressao_logica()
            self.state = 269
            self.match(SimpAlgParser.T__15)
            self.state = 270
            self.match(SimpAlgParser.T__1)
            self.state = 271
            localctx._comandos = self.comandos()
            self.state = 272
            self.match(SimpAlgParser.T__2)
            localctx.whilelabel = self.cg.new_label()
            localctx.iflabel = self.cg.new_label()
            localctx.endlabel = self.cg.new_label()
            localctx.code = "label " + localctx.whilelabel + "\n\t" 
            localctx.code = localctx.code + localctx._expressao_logica.code + "\n\t"
            localctx.code = localctx.code + "if " + localctx._expressao_logica.variavel + " : goto " + localctx.iflabel + "\n\t"
            localctx.code = localctx.code + "goto " + localctx.endlabel + "\n\t"
            localctx.code = localctx.code + "label " + localctx.iflabel
            localctx.code = localctx.code + localctx._comandos.code + "\n\t"
            localctx.code = localctx.code + "goto " + localctx.whilelabel + "\n\t"
            localctx.code = localctx.code + "label " + localctx.endlabel
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
            self.code = None
            self.variavel = None
            self._expressao_logica = None # Expressao_logicaContext
            self._or_expr = None # Or_exprContext

        def expressao_logica(self):
            return self.getTypedRuleContext(SimpAlgParser.Expressao_logicaContext,0)


        def or_expr(self):
            return self.getTypedRuleContext(SimpAlgParser.Or_exprContext,0)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_expressao_logica




    def expressao_logica(self):

        localctx = SimpAlgParser.Expressao_logicaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expressao_logica)
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.match(SimpAlgParser.T__14)
                self.state = 286
                localctx._expressao_logica = self.expressao_logica()
                self.state = 287
                self.match(SimpAlgParser.T__15)
                localctx.code = localctx._expressao_logica.code
                localctx.variavel = localctx._expressao_logica.variavel
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                localctx._or_expr = self.or_expr(0)
                localctx.code = localctx._or_expr.code
                localctx.variavel = localctx._or_expr.variavel
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
            self.code = None
            self.variavel = None
            self.e3 = None # Or_exprContext
            self.e1 = None # And_exprContext
            self._and_expr = None # And_exprContext
            self.e2 = None # And_exprContext
            self.e4 = None # Or_exprContext

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



    def or_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpAlgParser.Or_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_or_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            localctx.e1 = localctx._and_expr = self.and_expr(0)
            localctx.variavel = localctx._and_expr.variavel
            localctx.code = localctx._and_expr.code
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 301
                self.match(SimpAlgParser.T__21)
                self.state = 302
                localctx.e2 = localctx._and_expr = self.and_expr(0)
                localctx.variavel = self.cg.new_temp()
                localctx.code = localctx.e1.code + "\n\t" + localctx.e2.code + "\n\t" + localctx.variavel + " = " + localctx.e1.variavel + " or " + localctx.e2.variavel


            self._ctx.stop = self._input.LT(-1)
            self.state = 316
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpAlgParser.Or_exprContext(self, _parentctx, _parentState)
                    localctx.e3 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_or_expr)
                    self.state = 308
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 309
                    self.match(SimpAlgParser.T__21)
                    self.state = 310
                    localctx.e4 = self.or_expr(2)
                    localctx.variavel = self.cg.new_temp()
                    localctx.code = localctx.e3.code + "\n\t" + localctx.e4.code + "\n\t" + localctx.variavel + " = " + localctx.e3.variavel + " or " + localctx.e4.variavel 
                self.state = 318
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
            self.code = None
            self.variavel = None
            self.e1 = None # And_exprContext
            self.r1 = None # RelacionalContext
            self.r2 = None # RelacionalContext
            self.e2 = None # And_exprContext

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



    def and_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpAlgParser.And_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_and_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            localctx.r1 = self.relacional()
            localctx.variavel = localctx.r1.variavel
            localctx.code = localctx.r1.code
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 323
                self.match(SimpAlgParser.T__22)
                self.state = 324
                localctx.r2 = self.relacional()
                localctx.variavel = self.cg.new_temp()
                localctx.code = localctx.r1.code + "\n\t" + localctx.r2.code + "\n\t" + localctx.variavel + " = " + localctx.r1.variavel + " and " + localctx.r2.variavel


            self._ctx.stop = self._input.LT(-1)
            self.state = 338
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpAlgParser.And_exprContext(self, _parentctx, _parentState)
                    localctx.e1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_expr)
                    self.state = 330
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 331
                    self.match(SimpAlgParser.T__22)
                    self.state = 332
                    localctx.e2 = self.and_expr(2)
                    localctx.variavel = self.cg.new_temp()
                    localctx.code = localctx.e1.code + "\n\t" + localctx.e2.code + "\n\t" + localctx.variavel + " = " + localctx.e1.variavel + " and " + localctx.e2.variavel 
                self.state = 340
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
            self.code = None
            self.variavel = None
            self._relacional = None # RelacionalContext
            self._expressao_logica = None # Expressao_logicaContext
            self.t1 = None # TerminalContext
            self.op = None # Token
            self.t2 = None # TerminalContext

        def relacional(self):
            return self.getTypedRuleContext(SimpAlgParser.RelacionalContext,0)


        def expressao_logica(self):
            return self.getTypedRuleContext(SimpAlgParser.Expressao_logicaContext,0)


        def terminal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.TerminalContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.TerminalContext,i)


        def getRuleIndex(self):
            return SimpAlgParser.RULE_relacional




    def relacional(self):

        localctx = SimpAlgParser.RelacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_relacional)
        self._la = 0 # Token type
        try:
            self.state = 358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(SimpAlgParser.T__23)
                self.state = 342
                localctx._relacional = self.relacional()
                localctx.variavel = self.cg.new_temp()
                localctx.code = localctx._relacional.code + "\n\t" + localctx.variavel + " = not " + localctx._relacional.variavel
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.match(SimpAlgParser.T__14)
                self.state = 347
                localctx._expressao_logica = self.expressao_logica()
                self.state = 348
                self.match(SimpAlgParser.T__15)
                localctx.variavel = localctx._expressao_logica.variavel
                localctx.code = localctx._expressao_logica.code
                pass
            elif token in [31, 32, 33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 352
                localctx.t1 = self.terminal()
                self.state = 353
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2113929216) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 354
                localctx.t2 = self.terminal()
                localctx.variavel = self.cg.new_temp()
                localctx.code = localctx.variavel + " = " + (None if localctx.t1 is None else self._input.getText(localctx.t1.start,localctx.t1.stop)) + " " + (None if localctx.op is None else localctx.op.text) + " " + (None if localctx.t2 is None else self._input.getText(localctx.t2.start,localctx.t2.stop))
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


    class TerminalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(SimpAlgParser.ID, 0)

        def INT(self):
            return self.getToken(SimpAlgParser.INT, 0)

        def FLOAT(self):
            return self.getToken(SimpAlgParser.FLOAT, 0)

        def getRuleIndex(self):
            return SimpAlgParser.RULE_terminal




    def terminal(self):

        localctx = SimpAlgParser.TerminalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_terminal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.state = 360
                localctx._ID = self.match(SimpAlgParser.ID)
                self.at.isDeclared(localctx._ID)
                pass
            elif token in [32]:
                self.state = 362
                self.match(SimpAlgParser.INT)
                pass
            elif token in [33]:
                self.state = 363
                self.match(SimpAlgParser.FLOAT)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[21] = self.or_expr_sempred
        self._predicates[22] = self.and_expr_sempred
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
         




