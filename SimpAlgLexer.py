# Generated from SimpAlg.g4 by ANTLR 4.13.1
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
        4,0,36,221,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,
        1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,
        1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,
        1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,18,
        1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,23,
        1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,28,1,28,
        1,28,1,29,1,29,1,29,1,30,1,30,5,30,172,8,30,10,30,12,30,175,9,30,
        1,31,4,31,178,8,31,11,31,12,31,179,1,32,4,32,183,8,32,11,32,12,32,
        184,1,32,1,32,4,32,189,8,32,11,32,12,32,190,1,33,1,33,1,33,1,33,
        5,33,197,8,33,10,33,12,33,200,9,33,1,33,1,33,1,34,1,34,1,34,1,34,
        5,34,208,8,34,10,34,12,34,211,9,34,1,34,1,34,1,35,4,35,216,8,35,
        11,35,12,35,217,1,35,1,35,0,0,36,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,
        8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,
        19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,
        30,61,31,63,32,65,33,67,34,69,35,71,36,1,0,7,3,0,65,90,95,95,97,
        122,4,0,48,57,65,90,95,95,97,122,1,0,48,57,4,0,10,10,13,13,34,34,
        92,92,6,0,34,34,39,39,92,92,110,110,114,114,116,116,2,0,10,10,13,
        13,3,0,9,10,13,13,32,32,228,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,
        0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,
        17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,
        27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,
        37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,
        47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,
        57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,
        67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,1,73,1,0,0,0,3,77,1,0,0,0,5,
        79,1,0,0,0,7,81,1,0,0,0,9,89,1,0,0,0,11,91,1,0,0,0,13,93,1,0,0,0,
        15,97,1,0,0,0,17,103,1,0,0,0,19,105,1,0,0,0,21,111,1,0,0,0,23,113,
        1,0,0,0,25,115,1,0,0,0,27,120,1,0,0,0,29,123,1,0,0,0,31,128,1,0,
        0,0,33,134,1,0,0,0,35,136,1,0,0,0,37,138,1,0,0,0,39,140,1,0,0,0,
        41,142,1,0,0,0,43,144,1,0,0,0,45,147,1,0,0,0,47,151,1,0,0,0,49,153,
        1,0,0,0,51,155,1,0,0,0,53,157,1,0,0,0,55,160,1,0,0,0,57,163,1,0,
        0,0,59,166,1,0,0,0,61,169,1,0,0,0,63,177,1,0,0,0,65,182,1,0,0,0,
        67,192,1,0,0,0,69,203,1,0,0,0,71,215,1,0,0,0,73,74,5,118,0,0,74,
        75,5,97,0,0,75,76,5,114,0,0,76,2,1,0,0,0,77,78,5,123,0,0,78,4,1,
        0,0,0,79,80,5,125,0,0,80,6,1,0,0,0,81,82,5,112,0,0,82,83,5,114,0,
        0,83,84,5,111,0,0,84,85,5,103,0,0,85,86,5,114,0,0,86,87,5,97,0,0,
        87,88,5,109,0,0,88,8,1,0,0,0,89,90,5,59,0,0,90,10,1,0,0,0,91,92,
        5,44,0,0,92,12,1,0,0,0,93,94,5,105,0,0,94,95,5,110,0,0,95,96,5,116,
        0,0,96,14,1,0,0,0,97,98,5,102,0,0,98,99,5,108,0,0,99,100,5,111,0,
        0,100,101,5,97,0,0,101,102,5,116,0,0,102,16,1,0,0,0,103,104,5,61,
        0,0,104,18,1,0,0,0,105,106,5,112,0,0,106,107,5,114,0,0,107,108,5,
        105,0,0,108,109,5,110,0,0,109,110,5,116,0,0,110,20,1,0,0,0,111,112,
        5,40,0,0,112,22,1,0,0,0,113,114,5,41,0,0,114,24,1,0,0,0,115,116,
        5,115,0,0,116,117,5,99,0,0,117,118,5,97,0,0,118,119,5,110,0,0,119,
        26,1,0,0,0,120,121,5,105,0,0,121,122,5,102,0,0,122,28,1,0,0,0,123,
        124,5,101,0,0,124,125,5,108,0,0,125,126,5,115,0,0,126,127,5,101,
        0,0,127,30,1,0,0,0,128,129,5,119,0,0,129,130,5,104,0,0,130,131,5,
        105,0,0,131,132,5,108,0,0,132,133,5,101,0,0,133,32,1,0,0,0,134,135,
        5,43,0,0,135,34,1,0,0,0,136,137,5,45,0,0,137,36,1,0,0,0,138,139,
        5,42,0,0,139,38,1,0,0,0,140,141,5,47,0,0,141,40,1,0,0,0,142,143,
        5,37,0,0,143,42,1,0,0,0,144,145,5,111,0,0,145,146,5,114,0,0,146,
        44,1,0,0,0,147,148,5,97,0,0,148,149,5,110,0,0,149,150,5,100,0,0,
        150,46,1,0,0,0,151,152,5,33,0,0,152,48,1,0,0,0,153,154,5,60,0,0,
        154,50,1,0,0,0,155,156,5,62,0,0,156,52,1,0,0,0,157,158,5,60,0,0,
        158,159,5,61,0,0,159,54,1,0,0,0,160,161,5,62,0,0,161,162,5,61,0,
        0,162,56,1,0,0,0,163,164,5,61,0,0,164,165,5,61,0,0,165,58,1,0,0,
        0,166,167,5,33,0,0,167,168,5,61,0,0,168,60,1,0,0,0,169,173,7,0,0,
        0,170,172,7,1,0,0,171,170,1,0,0,0,172,175,1,0,0,0,173,171,1,0,0,
        0,173,174,1,0,0,0,174,62,1,0,0,0,175,173,1,0,0,0,176,178,7,2,0,0,
        177,176,1,0,0,0,178,179,1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,
        180,64,1,0,0,0,181,183,7,2,0,0,182,181,1,0,0,0,183,184,1,0,0,0,184,
        182,1,0,0,0,184,185,1,0,0,0,185,186,1,0,0,0,186,188,5,46,0,0,187,
        189,7,2,0,0,188,187,1,0,0,0,189,190,1,0,0,0,190,188,1,0,0,0,190,
        191,1,0,0,0,191,66,1,0,0,0,192,198,5,34,0,0,193,197,8,3,0,0,194,
        195,5,92,0,0,195,197,7,4,0,0,196,193,1,0,0,0,196,194,1,0,0,0,197,
        200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,201,1,0,0,0,200,
        198,1,0,0,0,201,202,5,34,0,0,202,68,1,0,0,0,203,204,5,47,0,0,204,
        205,5,47,0,0,205,209,1,0,0,0,206,208,8,5,0,0,207,206,1,0,0,0,208,
        211,1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,212,1,0,0,0,211,
        209,1,0,0,0,212,213,6,34,0,0,213,70,1,0,0,0,214,216,7,6,0,0,215,
        214,1,0,0,0,216,217,1,0,0,0,217,215,1,0,0,0,217,218,1,0,0,0,218,
        219,1,0,0,0,219,220,6,35,0,0,220,72,1,0,0,0,9,0,173,179,184,190,
        196,198,209,217,1,6,0,0
    ]

class SimpAlgLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    ID = 31
    INT = 32
    FLOAT = 33
    STRING = 34
    Comment = 35
    WS = 36

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'var'", "'{'", "'}'", "'program'", "';'", "','", "'int'", "'float'", 
            "'='", "'print'", "'('", "')'", "'scan'", "'if'", "'else'", 
            "'while'", "'+'", "'-'", "'*'", "'/'", "'%'", "'or'", "'and'", 
            "'!'", "'<'", "'>'", "'<='", "'>='", "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "FLOAT", "STRING", "Comment", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "ID", "INT", "FLOAT", 
                  "STRING", "Comment", "WS" ]

    grammarFileName = "SimpAlg.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


