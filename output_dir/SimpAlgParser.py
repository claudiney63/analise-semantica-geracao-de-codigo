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
from CodeGenerator import *

def serializedATN():
    return [
        4,1,36,458,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,5,3,66,8,3,10,3,12,3,69,
        9,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,80,8,5,10,5,12,5,83,
        9,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,93,8,7,10,7,12,7,96,9,7,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,122,8,8,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,154,8,
        10,10,10,12,10,157,9,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,3,10,169,8,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,190,
        8,12,10,12,12,12,193,9,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,211,8,12,10,12,12,12,
        214,9,12,3,12,216,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,3,13,245,8,13,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,3,15,265,8,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,
        15,276,8,15,5,15,278,8,15,10,15,12,15,281,9,15,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,5,
        17,299,8,17,10,17,12,17,302,9,17,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,334,8,
        18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,
        20,374,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
        21,1,21,3,21,388,8,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,5,21,397,
        8,21,10,21,12,21,400,9,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,3,22,414,8,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,5,22,423,8,22,10,22,12,22,426,9,22,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,3,23,449,8,23,1,24,1,24,1,24,1,24,1,24,3,24,456,8,
        24,1,24,0,2,42,44,25,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,48,0,4,1,0,7,8,1,0,10,11,1,0,12,13,1,0,25,
        30,465,0,50,1,0,0,0,2,53,1,0,0,0,4,58,1,0,0,0,6,67,1,0,0,0,8,70,
        1,0,0,0,10,73,1,0,0,0,12,84,1,0,0,0,14,86,1,0,0,0,16,121,1,0,0,0,
        18,123,1,0,0,0,20,168,1,0,0,0,22,170,1,0,0,0,24,215,1,0,0,0,26,244,
        1,0,0,0,28,246,1,0,0,0,30,255,1,0,0,0,32,282,1,0,0,0,34,291,1,0,
        0,0,36,303,1,0,0,0,38,337,1,0,0,0,40,373,1,0,0,0,42,375,1,0,0,0,
        44,401,1,0,0,0,46,448,1,0,0,0,48,450,1,0,0,0,50,51,3,2,1,0,51,52,
        3,4,2,0,52,1,1,0,0,0,53,54,5,1,0,0,54,55,5,2,0,0,55,56,3,6,3,0,56,
        57,5,3,0,0,57,3,1,0,0,0,58,59,5,4,0,0,59,60,5,2,0,0,60,61,3,14,7,
        0,61,62,5,3,0,0,62,63,6,2,-1,0,63,5,1,0,0,0,64,66,3,8,4,0,65,64,
        1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,7,1,0,0,0,69,
        67,1,0,0,0,70,71,3,10,5,0,71,72,5,5,0,0,72,9,1,0,0,0,73,74,3,12,
        6,0,74,75,5,31,0,0,75,81,6,5,-1,0,76,77,5,6,0,0,77,78,5,31,0,0,78,
        80,6,5,-1,0,79,76,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,
        0,0,82,11,1,0,0,0,83,81,1,0,0,0,84,85,7,0,0,0,85,13,1,0,0,0,86,87,
        6,7,-1,0,87,94,6,7,-1,0,88,89,3,16,8,0,89,90,6,7,-1,0,90,91,6,7,
        -1,0,91,93,1,0,0,0,92,88,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,
        95,1,0,0,0,95,15,1,0,0,0,96,94,1,0,0,0,97,98,6,8,-1,0,98,99,3,18,
        9,0,99,100,6,8,-1,0,100,101,6,8,-1,0,101,102,6,8,-1,0,102,122,1,
        0,0,0,103,104,3,28,14,0,104,105,6,8,-1,0,105,106,6,8,-1,0,106,122,
        1,0,0,0,107,108,3,32,16,0,108,109,6,8,-1,0,109,110,6,8,-1,0,110,
        122,1,0,0,0,111,112,3,36,18,0,112,113,6,8,-1,0,113,114,6,8,-1,0,
        114,115,6,8,-1,0,115,122,1,0,0,0,116,117,3,38,19,0,117,118,6,8,-1,
        0,118,119,6,8,-1,0,119,120,6,8,-1,0,120,122,1,0,0,0,121,97,1,0,0,
        0,121,103,1,0,0,0,121,107,1,0,0,0,121,111,1,0,0,0,121,116,1,0,0,
        0,122,17,1,0,0,0,123,124,6,9,-1,0,124,125,5,31,0,0,125,126,6,9,-1,
        0,126,127,5,9,0,0,127,128,3,20,10,0,128,129,5,5,0,0,129,130,6,9,
        -1,0,130,131,6,9,-1,0,131,132,6,9,-1,0,132,133,6,9,-1,0,133,134,
        6,9,-1,0,134,19,1,0,0,0,135,136,6,10,-1,0,136,137,3,24,12,0,137,
        138,6,10,-1,0,138,139,6,10,-1,0,139,140,6,10,-1,0,140,141,6,10,-1,
        0,141,142,6,10,-1,0,142,155,6,10,-1,0,143,144,7,1,0,0,144,145,3,
        24,12,0,145,146,6,10,-1,0,146,147,6,10,-1,0,147,148,6,10,-1,0,148,
        149,6,10,-1,0,149,150,6,10,-1,0,150,151,6,10,-1,0,151,152,6,10,-1,
        0,152,154,1,0,0,0,153,143,1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,
        0,155,156,1,0,0,0,156,169,1,0,0,0,157,155,1,0,0,0,158,159,3,22,11,
        0,159,160,3,24,12,0,160,161,6,10,-1,0,161,162,6,10,-1,0,162,163,
        6,10,-1,0,163,164,6,10,-1,0,164,165,6,10,-1,0,165,166,6,10,-1,0,
        166,167,6,10,-1,0,167,169,1,0,0,0,168,135,1,0,0,0,168,158,1,0,0,
        0,169,21,1,0,0,0,170,171,7,1,0,0,171,23,1,0,0,0,172,173,6,12,-1,
        0,173,174,3,26,13,0,174,175,6,12,-1,0,175,176,6,12,-1,0,176,177,
        6,12,-1,0,177,178,6,12,-1,0,178,179,6,12,-1,0,179,191,6,12,-1,0,
        180,181,7,2,0,0,181,182,3,26,13,0,182,183,6,12,-1,0,183,184,6,12,
        -1,0,184,185,6,12,-1,0,185,186,6,12,-1,0,186,187,6,12,-1,0,187,188,
        6,12,-1,0,188,190,1,0,0,0,189,180,1,0,0,0,190,193,1,0,0,0,191,189,
        1,0,0,0,191,192,1,0,0,0,192,216,1,0,0,0,193,191,1,0,0,0,194,195,
        3,26,13,0,195,196,6,12,-1,0,196,197,6,12,-1,0,197,198,6,12,-1,0,
        198,199,6,12,-1,0,199,200,6,12,-1,0,200,212,6,12,-1,0,201,202,5,
        14,0,0,202,203,3,26,13,0,203,204,6,12,-1,0,204,205,6,12,-1,0,205,
        206,6,12,-1,0,206,207,6,12,-1,0,207,208,6,12,-1,0,208,209,6,12,-1,
        0,209,211,1,0,0,0,210,201,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,
        0,212,213,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,215,172,1,0,0,
        0,215,194,1,0,0,0,216,25,1,0,0,0,217,218,6,13,-1,0,218,219,5,31,
        0,0,219,220,6,13,-1,0,220,221,6,13,-1,0,221,222,6,13,-1,0,222,223,
        6,13,-1,0,223,245,6,13,-1,0,224,225,5,32,0,0,225,226,6,13,-1,0,226,
        227,6,13,-1,0,227,228,6,13,-1,0,228,229,6,13,-1,0,229,245,6,13,-1,
        0,230,231,5,33,0,0,231,232,6,13,-1,0,232,233,6,13,-1,0,233,234,6,
        13,-1,0,234,235,6,13,-1,0,235,245,6,13,-1,0,236,237,5,15,0,0,237,
        238,3,20,10,0,238,239,6,13,-1,0,239,240,6,13,-1,0,240,241,5,16,0,
        0,241,242,6,13,-1,0,242,243,6,13,-1,0,243,245,1,0,0,0,244,217,1,
        0,0,0,244,224,1,0,0,0,244,230,1,0,0,0,244,236,1,0,0,0,245,27,1,0,
        0,0,246,247,6,14,-1,0,247,248,5,17,0,0,248,249,5,15,0,0,249,250,
        3,30,15,0,250,251,5,16,0,0,251,252,5,5,0,0,252,253,6,14,-1,0,253,
        254,6,14,-1,0,254,29,1,0,0,0,255,264,6,15,-1,0,256,257,5,31,0,0,
        257,265,6,15,-1,0,258,259,5,32,0,0,259,265,6,15,-1,0,260,261,5,33,
        0,0,261,265,6,15,-1,0,262,263,5,34,0,0,263,265,6,15,-1,0,264,256,
        1,0,0,0,264,258,1,0,0,0,264,260,1,0,0,0,264,262,1,0,0,0,265,279,
        1,0,0,0,266,275,5,6,0,0,267,268,5,31,0,0,268,276,6,15,-1,0,269,270,
        5,32,0,0,270,276,6,15,-1,0,271,272,5,33,0,0,272,276,6,15,-1,0,273,
        274,5,34,0,0,274,276,6,15,-1,0,275,267,1,0,0,0,275,269,1,0,0,0,275,
        271,1,0,0,0,275,273,1,0,0,0,276,278,1,0,0,0,277,266,1,0,0,0,278,
        281,1,0,0,0,279,277,1,0,0,0,279,280,1,0,0,0,280,31,1,0,0,0,281,279,
        1,0,0,0,282,283,6,16,-1,0,283,284,5,18,0,0,284,285,5,15,0,0,285,
        286,3,34,17,0,286,287,5,16,0,0,287,288,5,5,0,0,288,289,6,16,-1,0,
        289,290,6,16,-1,0,290,33,1,0,0,0,291,292,6,17,-1,0,292,293,5,31,
        0,0,293,294,6,17,-1,0,294,300,6,17,-1,0,295,296,5,6,0,0,296,297,
        5,31,0,0,297,299,6,17,-1,0,298,295,1,0,0,0,299,302,1,0,0,0,300,298,
        1,0,0,0,300,301,1,0,0,0,301,35,1,0,0,0,302,300,1,0,0,0,303,304,6,
        18,-1,0,304,305,5,19,0,0,305,306,5,15,0,0,306,307,3,40,20,0,307,
        308,5,16,0,0,308,309,5,2,0,0,309,310,3,14,7,0,310,311,5,3,0,0,311,
        312,6,18,-1,0,312,313,6,18,-1,0,313,314,6,18,-1,0,314,315,6,18,-1,
        0,315,316,6,18,-1,0,316,317,6,18,-1,0,317,318,6,18,-1,0,318,319,
        6,18,-1,0,319,333,6,18,-1,0,320,321,5,20,0,0,321,322,5,2,0,0,322,
        323,3,14,7,0,323,324,5,3,0,0,324,325,6,18,-1,0,325,326,6,18,-1,0,
        326,327,6,18,-1,0,327,328,6,18,-1,0,328,329,6,18,-1,0,329,330,6,
        18,-1,0,330,331,6,18,-1,0,331,332,6,18,-1,0,332,334,1,0,0,0,333,
        320,1,0,0,0,333,334,1,0,0,0,334,335,1,0,0,0,335,336,6,18,-1,0,336,
        37,1,0,0,0,337,338,6,19,-1,0,338,339,5,21,0,0,339,340,5,15,0,0,340,
        341,3,40,20,0,341,342,5,16,0,0,342,343,5,2,0,0,343,344,3,14,7,0,
        344,345,5,3,0,0,345,346,6,19,-1,0,346,347,6,19,-1,0,347,348,6,19,
        -1,0,348,349,6,19,-1,0,349,350,6,19,-1,0,350,351,6,19,-1,0,351,352,
        6,19,-1,0,352,353,6,19,-1,0,353,354,6,19,-1,0,354,355,6,19,-1,0,
        355,356,6,19,-1,0,356,357,6,19,-1,0,357,358,6,19,-1,0,358,359,6,
        19,-1,0,359,39,1,0,0,0,360,361,6,20,-1,0,361,362,5,15,0,0,362,363,
        3,40,20,0,363,364,5,16,0,0,364,365,6,20,-1,0,365,366,6,20,-1,0,366,
        367,6,20,-1,0,367,374,1,0,0,0,368,369,3,42,21,0,369,370,6,20,-1,
        0,370,371,6,20,-1,0,371,372,6,20,-1,0,372,374,1,0,0,0,373,360,1,
        0,0,0,373,368,1,0,0,0,374,41,1,0,0,0,375,376,6,21,-1,0,376,377,6,
        21,-1,0,377,378,3,44,22,0,378,379,6,21,-1,0,379,380,6,21,-1,0,380,
        387,6,21,-1,0,381,382,5,22,0,0,382,383,3,44,22,0,383,384,6,21,-1,
        0,384,385,6,21,-1,0,385,386,6,21,-1,0,386,388,1,0,0,0,387,381,1,
        0,0,0,387,388,1,0,0,0,388,398,1,0,0,0,389,390,10,1,0,0,390,391,5,
        22,0,0,391,392,3,42,21,2,392,393,6,21,-1,0,393,394,6,21,-1,0,394,
        395,6,21,-1,0,395,397,1,0,0,0,396,389,1,0,0,0,397,400,1,0,0,0,398,
        396,1,0,0,0,398,399,1,0,0,0,399,43,1,0,0,0,400,398,1,0,0,0,401,402,
        6,22,-1,0,402,403,6,22,-1,0,403,404,3,46,23,0,404,405,6,22,-1,0,
        405,406,6,22,-1,0,406,413,6,22,-1,0,407,408,5,23,0,0,408,409,3,46,
        23,0,409,410,6,22,-1,0,410,411,6,22,-1,0,411,412,6,22,-1,0,412,414,
        1,0,0,0,413,407,1,0,0,0,413,414,1,0,0,0,414,424,1,0,0,0,415,416,
        10,1,0,0,416,417,5,23,0,0,417,418,3,44,22,2,418,419,6,22,-1,0,419,
        420,6,22,-1,0,420,421,6,22,-1,0,421,423,1,0,0,0,422,415,1,0,0,0,
        423,426,1,0,0,0,424,422,1,0,0,0,424,425,1,0,0,0,425,45,1,0,0,0,426,
        424,1,0,0,0,427,428,6,23,-1,0,428,429,5,24,0,0,429,430,3,46,23,0,
        430,431,6,23,-1,0,431,432,6,23,-1,0,432,433,6,23,-1,0,433,449,1,
        0,0,0,434,435,5,15,0,0,435,436,3,40,20,0,436,437,5,16,0,0,437,438,
        6,23,-1,0,438,439,6,23,-1,0,439,440,6,23,-1,0,440,449,1,0,0,0,441,
        442,3,48,24,0,442,443,7,3,0,0,443,444,3,48,24,0,444,445,6,23,-1,
        0,445,446,6,23,-1,0,446,447,6,23,-1,0,447,449,1,0,0,0,448,427,1,
        0,0,0,448,434,1,0,0,0,448,441,1,0,0,0,449,47,1,0,0,0,450,455,6,24,
        -1,0,451,452,5,31,0,0,452,456,6,24,-1,0,453,456,5,32,0,0,454,456,
        5,33,0,0,455,451,1,0,0,0,455,453,1,0,0,0,455,454,1,0,0,0,456,49,
        1,0,0,0,22,67,81,94,121,155,168,191,212,215,244,264,275,279,300,
        333,373,387,398,413,424,448,455
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
    hasError = False



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
            self.state = 50
            self.var()
            self.state = 51
            self.program()
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
            self.state = 53
            self.match(SimpAlgParser.T__0)
            self.state = 54
            self.match(SimpAlgParser.T__1)
            self.state = 55
            self.declaracoes()
            self.state = 56
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
            self.state = 58
            self.match(SimpAlgParser.T__3)
            self.state = 59
            self.match(SimpAlgParser.T__1)
            self.state = 60
            localctx._comandos = self.comandos()
            self.state = 61
            self.match(SimpAlgParser.T__2)


            if (not self.at.isError()) and (not self.hasError): 
                with open('output.py', 'w') as file:
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

                    print("\nO código intermediário foi gerado com sucesso e salvo no arquivo output.py.\n")
            else:{print("\nO código intermediário não foi gerado pois o código fonte possui algum erro.\n")}

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
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 64
                self.declaracao()
                self.state = 69
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
            self.state = 70
            self.lista_de_declaracao()
            self.state = 71
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
            self.state = 73
            localctx.t = self.tipo()
            self.state = 74
            localctx._ID = self.match(SimpAlgParser.ID)
            self.at.create(localctx._ID, (None if localctx.t is None else self._input.getText(localctx.t.start,localctx.t.stop)))
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 76
                self.match(SimpAlgParser.T__5)
                self.state = 77
                localctx._ID = self.match(SimpAlgParser.ID)
                self.at.create(localctx._ID, (None if localctx.t is None else self._input.getText(localctx.t.start,localctx.t.stop)))
                self.state = 83
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
            self.state = 84
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
            if self.hasError: return
            localctx.code =  ''
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2150498304) != 0):
                self.state = 88
                localctx._comando = self.comando()
                if self.hasError: return
                if not(localctx._comando.code == None): localctx.code =  localctx.code + '\n\t' + localctx._comando.code
                self.state = 96
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
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                if self.hasError: return
                self.state = 98
                localctx._atribuicao = self.atribuicao()
                if self.hasError: return
                if (None if localctx._atribuicao is None else self._input.getText(localctx._atribuicao.start,localctx._atribuicao.stop)) == None: localctx.code = ""
                if not((None if localctx._atribuicao is None else self._input.getText(localctx._atribuicao.start,localctx._atribuicao.stop)) == None): localctx.code = localctx._atribuicao.code
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                localctx._saida = self.saida()
                if self.hasError: return
                localctx.code = localctx._saida.code
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                localctx._entrada = self.entrada()
                if self.hasError: return
                localctx.code = localctx._entrada.code
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 111
                localctx._condicional = self.condicional()
                if self.hasError: return
                if localctx._condicional.code == None: localctx.code = "ellem"
                if not(localctx._condicional.code == None): localctx.code = localctx._condicional.code
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 116
                localctx._repeticao = self.repeticao()
                if self.hasError: return
                if localctx._repeticao.code == None: localctx.code = ""
                if not(localctx._repeticao.code == None): localctx.code = localctx._repeticao.code
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
            if self.hasError: return
            self.state = 124
            localctx._ID = self.match(SimpAlgParser.ID)
            if not self.at.isDeclared(localctx._ID): return
            self.state = 126
            self.match(SimpAlgParser.T__8)
            self.state = 127
            localctx._expressao = self.expressao()
            self.state = 128
            self.match(SimpAlgParser.T__4)
            if self.hasError: return
            if(self.st.get_type((None if localctx._ID is None else localctx._ID.text)) == 'int' and localctx._expressao.type_ == 'float'):  print(f"Erro semântico na linha {(0 if localctx._ID is None else localctx._ID.line)}: Atribuição inválida. Esperado valor do tipo int, mas recebido {localctx._expressao.type_}.")
            if(self.st.get_type((None if localctx._ID is None else localctx._ID.text)) == 'int' and localctx._expressao.type_ == 'float'): self.at.setError(True)
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
            self.line = None
            self.type_ = None
            self.val = None
            self.code = None
            self.variavel = None
            self.variavelAnterior = None
            self.t1 = None # TermoContext
            self._termo = None # TermoContext
            self.op = None # Token
            self.t2 = None # TermoContext
            self.opU = None # Op_unarioContext

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
        self.enterRule(localctx, 20, self.RULE_expressao)
        self._la = 0 # Token type
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 31, 32, 33]:
                self.enterOuterAlt(localctx, 1)
                if self.hasError: return
                self.state = 136
                localctx.t1 = localctx._termo = self.termo()
                if self.hasError: return
                localctx.val = (None if localctx.t1 is None else self._input.getText(localctx.t1.start,localctx.t1.stop))
                localctx.code = localctx.t1.code
                localctx.variavel = localctx.t1.variavel
                localctx.type_ = localctx.t1.type_
                localctx.line = localctx._termo.line
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10 or _la==11:
                    self.state = 143
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==10 or _la==11):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 144
                    localctx.t2 = localctx._termo = self.termo()
                    localctx.val = (None if localctx.t1 is None else self._input.getText(localctx.t1.start,localctx.t1.stop)) + (None if localctx.op is None else localctx.op.text) + (None if localctx.t2 is None else self._input.getText(localctx.t2.start,localctx.t2.stop))
                    localctx.type_ = 'error'
                    if(localctx.t1.type_ == "int" and localctx.t2.type_ == "int"): localctx.type_ = "int"
                    if(localctx.t1.type_ == "float" or localctx.t2.type_ == "float"): localctx.type_ = "float"
                    localctx.variavelAnterior = localctx.variavel
                    localctx.variavel = self.cg.new_temp()
                    localctx.code = localctx.code + localctx.t2.code + "\n\t" + localctx.variavel + " = " +  localctx.variavelAnterior + " " + (None if localctx.op is None else localctx.op.text) + " " + localctx.t2.variavel
                    self.state = 157
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [10, 11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                localctx.opU = self.op_unario()
                self.state = 159
                localctx._termo = self.termo()
                if self.hasError: return
                localctx.val = (None if localctx.opU is None else self._input.getText(localctx.opU.start,localctx.opU.stop)) + (None if localctx._termo is None else self._input.getText(localctx._termo.start,localctx._termo.stop))
                localctx.type_ = localctx._termo.type_
                localctx.line = localctx._termo.line
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
        self.enterRule(localctx, 22, self.RULE_op_unario)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
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
            self.line = None
            self.type_ = None
            self.val = None
            self.code = None
            self.variavel = None
            self.variavelAnterior = None
            self.f1 = None # FatorContext
            self._fator = None # FatorContext
            self.op = None # Token
            self.f2 = None # FatorContext

        def fator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpAlgParser.FatorContext)
            else:
                return self.getTypedRuleContext(SimpAlgParser.FatorContext,i)


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
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                if self.hasError: return
                self.state = 173
                localctx.f1 = localctx._fator = self.fator()
                if self.hasError: return
                localctx.val = (None if localctx.f1 is None else self._input.getText(localctx.f1.start,localctx.f1.stop))
                localctx.code = localctx.f1.code
                localctx.variavel = localctx.f1.variavel
                localctx.type_ = localctx._fator.type_
                localctx.line = localctx._fator.line
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12 or _la==13:
                    self.state = 180
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==12 or _la==13):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 181
                    localctx.f2 = localctx._fator = self.fator()
                    localctx.val = (None if localctx.f1 is None else self._input.getText(localctx.f1.start,localctx.f1.stop)) + (None if localctx.op is None else localctx.op.text) + (None if localctx.f2 is None else self._input.getText(localctx.f2.start,localctx.f2.stop))
                    if(localctx.f1.type_ == "int" and localctx.f2.type_ == "int"): localctx.type_ = "int"
                    if(localctx.f1.type_ == "float" or localctx.f2.type_ == "float"): localctx.type_ = "float"
                    localctx.variavelAnterior = localctx.variavel
                    localctx.variavel = self.cg.new_temp()
                    localctx.code = localctx.code + localctx.f2.code + "\n\t" + localctx.variavel + " = " +  localctx.variavelAnterior + " " + (None if localctx.op is None else localctx.op.text) + " " + localctx.f2.variavel
                    self.state = 193
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                localctx.f1 = localctx._fator = self.fator()
                if self.hasError: return
                localctx.val = (None if localctx.f1 is None else self._input.getText(localctx.f1.start,localctx.f1.stop))
                localctx.code = localctx.f1.code
                localctx.variavel = localctx.f1.variavel
                localctx.type_ = 'int'
                localctx.line = localctx._fator.line
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 201
                    self.match(SimpAlgParser.T__13)
                    self.state = 202
                    localctx.f2 = localctx._fator = self.fator()
                    localctx.val = (None if localctx.f1 is None else self._input.getText(localctx.f1.start,localctx.f1.stop)) + " % " + (None if localctx.f2 is None else self._input.getText(localctx.f2.start,localctx.f2.stop))
                    if(localctx.f1.type_ == "float" or localctx.f2.type_ == "float"): self.at.setError(True)
                    if(localctx.f1.type_ == "float" or localctx.f2.type_ == "float"): print(f"Erro semântico na linha {localctx.f1.line}: Operação de módulo inválida. Ambos os operandos devem ser do tipo int, mas recebido {localctx.f1.type_} e {localctx.f2.type_}.")
                    localctx.variavelAnterior = localctx.variavel
                    localctx.variavel = self.cg.new_temp()
                    localctx.code = localctx.code + localctx.f2.code + "\n\t" + localctx.variavel + " = " +  localctx.variavelAnterior + " % " + localctx.f2.variavel
                    self.state = 214
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
            self.line = None
            self.type_ = None
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
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                if self.hasError: return
                self.state = 218
                localctx._ID = self.match(SimpAlgParser.ID)
                if not(self.at.isDeclared(localctx._ID)): localctx.type_ = 'error'
                if not(localctx.type_ == 'error'): localctx.type_ = self.st.get_type((None if localctx._ID is None else localctx._ID.text))
                localctx.code = ""
                localctx.variavel = (None if localctx._ID is None else localctx._ID.text)
                localctx.line = (0 if localctx._ID is None else localctx._ID.line)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                localctx._INT = self.match(SimpAlgParser.INT)
                localctx.val = (None if localctx._INT is None else localctx._INT.text)
                localctx.code = ""
                localctx.variavel = (None if localctx._INT is None else localctx._INT.text)
                localctx.type_ = "int"
                localctx.line = (0 if localctx._INT is None else localctx._INT.line)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                localctx._FLOAT = self.match(SimpAlgParser.FLOAT)
                localctx.val = (None if localctx._FLOAT is None else localctx._FLOAT.text)
                localctx.code = ""
                localctx.variavel = (None if localctx._FLOAT is None else localctx._FLOAT.text)
                localctx.type_ = "float"
                localctx.line = (0 if localctx._FLOAT is None else localctx._FLOAT.line)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 236
                self.match(SimpAlgParser.T__14)
                self.state = 237
                localctx._expressao = self.expressao()
                localctx.code = localctx._expressao.code
                localctx.variavel = localctx._expressao.variavel
                self.state = 240
                self.match(SimpAlgParser.T__15)
                localctx.type_ = localctx._expressao.type_
                localctx.line = localctx._expressao.line
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
        self.enterRule(localctx, 28, self.RULE_saida)
        try:
            self.enterOuterAlt(localctx, 1)
            if self.hasError: return
            self.state = 247
            self.match(SimpAlgParser.T__16)
            self.state = 248
            self.match(SimpAlgParser.T__14)
            self.state = 249
            localctx._lista_de_valores = self.lista_de_valores()
            self.state = 250
            self.match(SimpAlgParser.T__15)
            self.state = 251
            self.match(SimpAlgParser.T__4)
            if self.hasError: return
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
            self._INT = None # Token
            self._FLOAT = None # Token
            self._STRING = None # Token

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
            if self.hasError: return
            self.state = 264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.state = 256
                localctx._ID = self.match(SimpAlgParser.ID)
                self.at.isDeclared(localctx._ID); localctx.code = (None if localctx._ID is None else localctx._ID.text)
                pass
            elif token in [32]:
                self.state = 258
                localctx._INT = self.match(SimpAlgParser.INT)
                localctx.code = (None if localctx._INT is None else localctx._INT.text)
                pass
            elif token in [33]:
                self.state = 260
                localctx._FLOAT = self.match(SimpAlgParser.FLOAT)
                localctx.code = (None if localctx._FLOAT is None else localctx._FLOAT.text)
                pass
            elif token in [34]:
                self.state = 262
                localctx._STRING = self.match(SimpAlgParser.STRING)
                localctx.code = (None if localctx._STRING is None else localctx._STRING.text)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 266
                self.match(SimpAlgParser.T__5)
                self.state = 275
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [31]:
                    self.state = 267
                    localctx._ID = self.match(SimpAlgParser.ID)
                    self.at.isDeclared(localctx._ID); localctx.code = localctx.code + ', ' + (None if localctx._ID is None else localctx._ID.text)
                    pass
                elif token in [32]:
                    self.state = 269
                    localctx._INT = self.match(SimpAlgParser.INT)
                    localctx.code = localctx.code + ', ' +  (None if localctx._INT is None else localctx._INT.text)
                    pass
                elif token in [33]:
                    self.state = 271
                    localctx._FLOAT = self.match(SimpAlgParser.FLOAT)
                    localctx.code = localctx.code + ', ' +  (None if localctx._FLOAT is None else localctx._FLOAT.text)
                    pass
                elif token in [34]:
                    self.state = 273
                    localctx._STRING = self.match(SimpAlgParser.STRING)
                    localctx.code = localctx.code + ', ' +  (None if localctx._STRING is None else localctx._STRING.text)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 281
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
        self.enterRule(localctx, 32, self.RULE_entrada)
        try:
            self.enterOuterAlt(localctx, 1)
            if self.hasError: return
            self.state = 283
            self.match(SimpAlgParser.T__17)
            self.state = 284
            self.match(SimpAlgParser.T__14)
            self.state = 285
            localctx._lista_de_variaveis = self.lista_de_variaveis()
            self.state = 286
            self.match(SimpAlgParser.T__15)
            self.state = 287
            self.match(SimpAlgParser.T__4)
            if self.hasError: return
            localctx.code = localctx._lista_de_variaveis.code
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
        self.enterRule(localctx, 34, self.RULE_lista_de_variaveis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            if self.hasError: return
            self.state = 292
            localctx._ID = self.match(SimpAlgParser.ID)
            self.at.isDeclared(localctx._ID); localctx.code = (None if localctx._ID is None else localctx._ID.text)
            if(self.at.isDeclared(localctx._ID)): localctx.code = (None if localctx._ID is None else localctx._ID.text) + " = " + self.st.get_type((None if localctx._ID is None else localctx._ID.text)) + "(input('input " + (None if localctx._ID is None else localctx._ID.text) + ":' ))"
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 295
                self.match(SimpAlgParser.T__5)
                self.state = 296
                localctx._ID = self.match(SimpAlgParser.ID)
                if(self.at.isDeclared(localctx._ID)): localctx.code = localctx.code + "\n\t" + (None if localctx._ID is None else localctx._ID.text) + " = " + self.st.get_type((None if localctx._ID is None else localctx._ID.text)) + "(input('input " + (None if localctx._ID is None else localctx._ID.text) + ":' ))"
                self.state = 302
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
            self.labelend = None
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
        self.enterRule(localctx, 36, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            if self.hasError: return
            self.state = 304
            self.match(SimpAlgParser.T__18)
            self.state = 305
            self.match(SimpAlgParser.T__14)
            self.state = 306
            localctx._expressao_logica = self.expressao_logica()
            self.state = 307
            self.match(SimpAlgParser.T__15)
            self.state = 308
            self.match(SimpAlgParser.T__1)
            self.state = 309
            localctx.cif = self.comandos()
            self.state = 310
            self.match(SimpAlgParser.T__2)
            if self.hasError: return
            localctx.labelif = self.cg.new_label()
            localctx.labelend = self.cg.new_label()
            if not localctx._expressao_logica.code: localctx._expressao_logica.code = ""
            if not localctx._expressao_logica.variavel: localctx._expressao_logica.variavel = ""
            localctx.code = localctx._expressao_logica.code + "\n\t"
            localctx.code = localctx.code + "if " + localctx._expressao_logica.variavel + " : goto " + localctx.labelif + "\n\t"
            localctx.code = localctx.code + "goto " + localctx.labelend + "\n\t"
            localctx.code = localctx.code + "label "+ localctx.labelif + localctx.cif.code 
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 320
                self.match(SimpAlgParser.T__19)
                self.state = 321
                self.match(SimpAlgParser.T__1)
                self.state = 322
                localctx.celse = self.comandos()
                self.state = 323
                self.match(SimpAlgParser.T__2)
                if self.hasError: return
                localctx.labelelse = self.cg.new_label()
                localctx.code = localctx._expressao_logica.code + "\n\t"
                localctx.code = localctx.code + "if " + localctx._expressao_logica.variavel + " : goto " + localctx.labelif
                localctx.code = localctx.code + localctx.celse.code + "\n\t"
                localctx.code = localctx.code + "goto " + localctx.labelelse + "\n\t"
                localctx.code = localctx.code + "label "+ localctx.labelif + localctx.cif.code + "\n\t"
                localctx.code = localctx.code + "label " + localctx.labelelse 


            localctx.code = localctx.code + "\n\tlabel " + localctx.labelend
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
        self.enterRule(localctx, 38, self.RULE_repeticao)
        try:
            self.enterOuterAlt(localctx, 1)
            if self.hasError: return
            self.state = 338
            self.match(SimpAlgParser.T__20)
            self.state = 339
            self.match(SimpAlgParser.T__14)
            self.state = 340
            localctx._expressao_logica = self.expressao_logica()
            self.state = 341
            self.match(SimpAlgParser.T__15)
            self.state = 342
            self.match(SimpAlgParser.T__1)
            self.state = 343
            localctx._comandos = self.comandos()
            self.state = 344
            self.match(SimpAlgParser.T__2)
            if self.hasError: return
            if not localctx._expressao_logica.code: localctx._expressao_logica.code = ""
            if not localctx._expressao_logica.variavel: localctx._expressao_logica.variavel = ""
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
        self.enterRule(localctx, 40, self.RULE_expressao_logica)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                if self.hasError: return
                self.state = 361
                self.match(SimpAlgParser.T__14)
                self.state = 362
                localctx._expressao_logica = self.expressao_logica()
                self.state = 363
                self.match(SimpAlgParser.T__15)
                if self.hasError: return
                localctx.code = localctx._expressao_logica.code
                localctx.variavel = localctx._expressao_logica.variavel
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                localctx._or_expr = self.or_expr(0)
                if self.hasError: return
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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_or_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            if self.hasError: return
            self.state = 377
            localctx.e1 = localctx._and_expr = self.and_expr(0)
            if self.hasError: return
            localctx.variavel = localctx._and_expr.variavel
            localctx.code = localctx._and_expr.code
            self.state = 387
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 381
                self.match(SimpAlgParser.T__21)
                self.state = 382
                localctx.e2 = localctx._and_expr = self.and_expr(0)
                if self.hasError: return
                localctx.variavel = self.cg.new_temp()
                if not(self.hasError): localctx.code = localctx.e1.code + "\n\t" + localctx.e2.code + "\n\t" + localctx.variavel + " = " + localctx.e1.variavel + " or " + localctx.e2.variavel


            self._ctx.stop = self._input.LT(-1)
            self.state = 398
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
                    self.state = 389
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 390
                    self.match(SimpAlgParser.T__21)
                    self.state = 391
                    localctx.e4 = self.or_expr(2)
                    if self.hasError: return
                    localctx.variavel = self.cg.new_temp()
                    if not(self.hasError): localctx.code = localctx.e3.code + "\n\t" + localctx.e4.code + "\n\t" + localctx.variavel + " = " + localctx.e3.variavel + " or " + localctx.e4.variavel 
                self.state = 400
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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_and_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            if self.hasError: return
            self.state = 403
            localctx.r1 = self.relacional()
            if self.hasError: return
            localctx.variavel = localctx.r1.variavel
            localctx.code = localctx.r1.code
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 407
                self.match(SimpAlgParser.T__22)
                self.state = 408
                localctx.r2 = self.relacional()
                if self.hasError: return
                localctx.variavel = self.cg.new_temp()
                if not(self.hasError): localctx.code = localctx.r1.code + "\n\t" + localctx.r2.code + "\n\t" + localctx.variavel + " = " + localctx.r1.variavel + " and " + localctx.r2.variavel


            self._ctx.stop = self._input.LT(-1)
            self.state = 424
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
                    self.state = 415
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 416
                    self.match(SimpAlgParser.T__22)
                    self.state = 417
                    localctx.e2 = self.and_expr(2)
                    if self.hasError: return
                    localctx.variavel = self.cg.new_temp()
                    if not(self.hasError): localctx.code = localctx.e1.code + "\n\t" + localctx.e2.code + "\n\t" + localctx.variavel + " = " + localctx.e1.variavel + " and " + localctx.e2.variavel 
                self.state = 426
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




    def relacional(self):

        localctx = SimpAlgParser.RelacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_relacional)
        self._la = 0 # Token type
        try:
            self.state = 448
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                if self.hasError: return
                self.state = 428
                self.match(SimpAlgParser.T__23)
                self.state = 429
                localctx._relacional = self.relacional()
                if self.hasError: return
                localctx.variavel = self.cg.new_temp()
                if not(self.hasError): localctx.code = localctx._relacional.code + "\n\t" + localctx.variavel + " = not " + localctx._relacional.variavel
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.match(SimpAlgParser.T__14)
                self.state = 435
                localctx._expressao_logica = self.expressao_logica()
                self.state = 436
                self.match(SimpAlgParser.T__15)
                if self.hasError: return
                localctx.variavel = localctx._expressao_logica.variavel
                localctx.code = localctx._expressao_logica.code
                pass
            elif token in [31, 32, 33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 441
                localctx.t1 = self.terminal()
                self.state = 442
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2113929216) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 443
                localctx.t2 = self.terminal()
                if self.hasError: return
                localctx.variavel = self.cg.new_temp()
                if not(self.hasError): localctx.code = localctx.variavel + " = " + (None if localctx.t1 is None else self._input.getText(localctx.t1.start,localctx.t1.stop)) + " " + (None if localctx.op is None else localctx.op.text) + " " + (None if localctx.t2 is None else self._input.getText(localctx.t2.start,localctx.t2.stop))
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminal" ):
                listener.enterTerminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminal" ):
                listener.exitTerminal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminal" ):
                return visitor.visitTerminal(self)
            else:
                return visitor.visitChildren(self)




    def terminal(self):

        localctx = SimpAlgParser.TerminalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_terminal)
        try:
            self.enterOuterAlt(localctx, 1)
            if self.hasError: return
            self.state = 455
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.state = 451
                localctx._ID = self.match(SimpAlgParser.ID)
                self.at.isDeclared(localctx._ID)
                pass
            elif token in [32]:
                self.state = 453
                self.match(SimpAlgParser.INT)
                pass
            elif token in [33]:
                self.state = 454
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
         




