# Generated from C:/University/6_sem/YAPIS/grammar\ListLanguage.g4 by ANTLR 4.12.0
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
        4,1,42,338,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,5,0,64,8,0,10,0,12,0,
        67,9,0,1,0,5,0,70,8,0,10,0,12,0,73,9,0,1,1,4,1,76,8,1,11,1,12,1,
        77,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,90,8,2,1,3,1,3,1,
        3,3,3,95,8,3,4,3,97,8,3,11,3,12,3,98,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,3,3,112,8,3,4,3,114,8,3,11,3,12,3,115,1,4,5,4,119,
        8,4,10,4,12,4,122,9,4,1,4,1,4,3,4,126,8,4,4,4,128,8,4,11,4,12,4,
        129,1,4,3,4,133,8,4,1,4,5,4,136,8,4,10,4,12,4,139,9,4,1,5,1,5,1,
        5,1,5,1,5,1,6,1,6,1,6,3,6,149,8,6,5,6,151,8,6,10,6,12,6,154,9,6,
        1,6,1,6,1,7,1,7,1,7,3,7,161,8,7,5,7,163,8,7,10,7,12,7,166,9,7,1,
        7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,3,9,176,8,9,5,9,178,8,9,10,9,12,9,
        181,9,9,1,9,1,9,1,10,1,10,5,10,187,8,10,10,10,12,10,190,9,10,1,10,
        3,10,193,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,14,1,14,1,15,1,15,3,15,224,8,15,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,3,17,238,8,17,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,4,18,248,8,18,11,18,12,18,249,1,18,
        1,18,1,19,1,19,1,19,1,19,1,19,1,19,5,19,260,8,19,10,19,12,19,263,
        9,19,1,19,1,19,1,19,4,19,268,8,19,11,19,12,19,269,1,19,1,19,1,20,
        1,20,1,20,1,20,1,20,5,20,279,8,20,10,20,12,20,282,9,20,1,20,1,20,
        1,21,1,21,1,21,1,21,3,21,290,8,21,5,21,292,8,21,10,21,12,21,295,
        9,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,24,
        1,24,1,24,3,24,311,8,24,1,25,1,25,1,25,1,25,1,25,3,25,318,8,25,1,
        25,1,25,1,26,1,26,1,27,1,27,1,27,1,27,3,27,328,8,27,1,28,1,28,3,
        28,332,8,28,1,29,1,29,1,30,1,30,1,30,0,0,31,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        0,5,1,0,28,31,2,0,28,31,33,37,1,0,11,15,1,0,40,41,1,0,28,32,358,
        0,65,1,0,0,0,2,75,1,0,0,0,4,89,1,0,0,0,6,96,1,0,0,0,8,120,1,0,0,
        0,10,140,1,0,0,0,12,145,1,0,0,0,14,157,1,0,0,0,16,169,1,0,0,0,18,
        171,1,0,0,0,20,184,1,0,0,0,22,194,1,0,0,0,24,204,1,0,0,0,26,209,
        1,0,0,0,28,219,1,0,0,0,30,221,1,0,0,0,32,225,1,0,0,0,34,235,1,0,
        0,0,36,239,1,0,0,0,38,253,1,0,0,0,40,273,1,0,0,0,42,285,1,0,0,0,
        44,298,1,0,0,0,46,303,1,0,0,0,48,310,1,0,0,0,50,312,1,0,0,0,52,321,
        1,0,0,0,54,327,1,0,0,0,56,331,1,0,0,0,58,333,1,0,0,0,60,335,1,0,
        0,0,62,64,3,38,19,0,63,62,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,
        66,1,0,0,0,66,71,1,0,0,0,67,65,1,0,0,0,68,70,3,4,2,0,69,68,1,0,0,
        0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,1,1,0,0,0,73,71,1,
        0,0,0,74,76,3,4,2,0,75,74,1,0,0,0,76,77,1,0,0,0,77,75,1,0,0,0,77,
        78,1,0,0,0,78,3,1,0,0,0,79,90,3,6,3,0,80,90,3,42,21,0,81,90,3,20,
        10,0,82,90,3,40,20,0,83,90,3,30,15,0,84,90,3,48,24,0,85,90,3,44,
        22,0,86,90,3,34,17,0,87,90,3,46,23,0,88,90,3,50,25,0,89,79,1,0,0,
        0,89,80,1,0,0,0,89,81,1,0,0,0,89,82,1,0,0,0,89,83,1,0,0,0,89,84,
        1,0,0,0,89,85,1,0,0,0,89,86,1,0,0,0,89,87,1,0,0,0,89,88,1,0,0,0,
        90,5,1,0,0,0,91,97,3,10,5,0,92,94,5,40,0,0,93,95,5,19,0,0,94,93,
        1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,96,91,1,0,0,0,96,92,1,0,0,0,
        97,98,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,113,
        5,27,0,0,101,114,3,14,7,0,102,114,3,16,8,0,103,114,3,12,6,0,104,
        114,3,18,9,0,105,114,3,8,4,0,106,114,3,46,23,0,107,114,3,10,5,0,
        108,114,3,50,25,0,109,111,5,40,0,0,110,112,5,19,0,0,111,110,1,0,
        0,0,111,112,1,0,0,0,112,114,1,0,0,0,113,101,1,0,0,0,113,102,1,0,
        0,0,113,103,1,0,0,0,113,104,1,0,0,0,113,105,1,0,0,0,113,106,1,0,
        0,0,113,107,1,0,0,0,113,108,1,0,0,0,113,109,1,0,0,0,114,115,1,0,
        0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,7,1,0,0,0,117,119,5,21,0,
        0,118,117,1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,
        0,121,127,1,0,0,0,122,120,1,0,0,0,123,125,3,56,28,0,124,126,7,0,
        0,0,125,124,1,0,0,0,125,126,1,0,0,0,126,128,1,0,0,0,127,123,1,0,
        0,0,128,129,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,132,1,0,
        0,0,131,133,3,60,30,0,132,131,1,0,0,0,132,133,1,0,0,0,133,137,1,
        0,0,0,134,136,5,22,0,0,135,134,1,0,0,0,136,139,1,0,0,0,137,135,1,
        0,0,0,137,138,1,0,0,0,138,9,1,0,0,0,139,137,1,0,0,0,140,141,5,40,
        0,0,141,142,5,23,0,0,142,143,5,41,0,0,143,144,5,24,0,0,144,11,1,
        0,0,0,145,152,5,21,0,0,146,148,3,16,8,0,147,149,5,19,0,0,148,147,
        1,0,0,0,148,149,1,0,0,0,149,151,1,0,0,0,150,146,1,0,0,0,151,154,
        1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,155,1,0,0,0,154,152,
        1,0,0,0,155,156,5,22,0,0,156,13,1,0,0,0,157,164,5,23,0,0,158,160,
        3,16,8,0,159,161,5,19,0,0,160,159,1,0,0,0,160,161,1,0,0,0,161,163,
        1,0,0,0,162,158,1,0,0,0,163,166,1,0,0,0,164,162,1,0,0,0,164,165,
        1,0,0,0,165,167,1,0,0,0,166,164,1,0,0,0,167,168,5,24,0,0,168,15,
        1,0,0,0,169,170,3,58,29,0,170,17,1,0,0,0,171,179,5,23,0,0,172,173,
        3,16,8,0,173,175,3,18,9,0,174,176,3,18,9,0,175,174,1,0,0,0,175,176,
        1,0,0,0,176,178,1,0,0,0,177,172,1,0,0,0,178,181,1,0,0,0,179,177,
        1,0,0,0,179,180,1,0,0,0,180,182,1,0,0,0,181,179,1,0,0,0,182,183,
        5,24,0,0,183,19,1,0,0,0,184,188,3,22,11,0,185,187,3,26,13,0,186,
        185,1,0,0,0,187,190,1,0,0,0,188,186,1,0,0,0,188,189,1,0,0,0,189,
        192,1,0,0,0,190,188,1,0,0,0,191,193,3,24,12,0,192,191,1,0,0,0,192,
        193,1,0,0,0,193,21,1,0,0,0,194,195,5,8,0,0,195,196,5,21,0,0,196,
        197,3,56,28,0,197,198,3,28,14,0,198,199,3,56,28,0,199,200,5,22,0,
        0,200,201,5,25,0,0,201,202,3,2,1,0,202,203,5,26,0,0,203,23,1,0,0,
        0,204,205,5,9,0,0,205,206,5,21,0,0,206,207,3,2,1,0,207,208,5,22,
        0,0,208,25,1,0,0,0,209,210,5,10,0,0,210,211,5,21,0,0,211,212,3,56,
        28,0,212,213,3,28,14,0,213,214,3,56,28,0,214,215,5,22,0,0,215,216,
        5,25,0,0,216,217,3,2,1,0,217,218,5,26,0,0,218,27,1,0,0,0,219,220,
        7,1,0,0,220,29,1,0,0,0,221,223,3,32,16,0,222,224,3,24,12,0,223,222,
        1,0,0,0,223,224,1,0,0,0,224,31,1,0,0,0,225,226,5,5,0,0,226,227,5,
        21,0,0,227,228,3,54,27,0,228,229,5,7,0,0,229,230,3,56,28,0,230,231,
        5,22,0,0,231,232,5,25,0,0,232,233,3,2,1,0,233,234,5,26,0,0,234,33,
        1,0,0,0,235,237,3,36,18,0,236,238,3,24,12,0,237,236,1,0,0,0,237,
        238,1,0,0,0,238,35,1,0,0,0,239,240,5,6,0,0,240,241,5,21,0,0,241,
        242,3,56,28,0,242,243,3,28,14,0,243,244,3,56,28,0,244,245,5,22,0,
        0,245,247,5,25,0,0,246,248,3,2,1,0,247,246,1,0,0,0,248,249,1,0,0,
        0,249,247,1,0,0,0,249,250,1,0,0,0,250,251,1,0,0,0,251,252,5,26,0,
        0,252,37,1,0,0,0,253,254,5,4,0,0,254,255,5,40,0,0,255,256,5,21,0,
        0,256,261,3,58,29,0,257,258,5,19,0,0,258,260,3,58,29,0,259,257,1,
        0,0,0,260,263,1,0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,264,1,
        0,0,0,263,261,1,0,0,0,264,265,5,22,0,0,265,267,5,25,0,0,266,268,
        3,2,1,0,267,266,1,0,0,0,268,269,1,0,0,0,269,267,1,0,0,0,269,270,
        1,0,0,0,270,271,1,0,0,0,271,272,5,26,0,0,272,39,1,0,0,0,273,274,
        5,40,0,0,274,275,5,21,0,0,275,280,3,58,29,0,276,277,5,19,0,0,277,
        279,3,58,29,0,278,276,1,0,0,0,279,282,1,0,0,0,280,278,1,0,0,0,280,
        281,1,0,0,0,281,283,1,0,0,0,282,280,1,0,0,0,283,284,5,22,0,0,284,
        41,1,0,0,0,285,286,5,2,0,0,286,293,5,21,0,0,287,289,3,56,28,0,288,
        290,5,19,0,0,289,288,1,0,0,0,289,290,1,0,0,0,290,292,1,0,0,0,291,
        287,1,0,0,0,292,295,1,0,0,0,293,291,1,0,0,0,293,294,1,0,0,0,294,
        296,1,0,0,0,295,293,1,0,0,0,296,297,5,22,0,0,297,43,1,0,0,0,298,
        299,5,3,0,0,299,300,5,21,0,0,300,301,3,56,28,0,301,302,5,22,0,0,
        302,45,1,0,0,0,303,304,5,1,0,0,304,305,5,21,0,0,305,306,5,22,0,0,
        306,47,1,0,0,0,307,308,5,16,0,0,308,311,5,40,0,0,309,311,5,41,0,
        0,310,307,1,0,0,0,310,309,1,0,0,0,311,49,1,0,0,0,312,313,3,54,27,
        0,313,314,5,18,0,0,314,315,3,52,26,0,315,317,5,21,0,0,316,318,3,
        56,28,0,317,316,1,0,0,0,317,318,1,0,0,0,318,319,1,0,0,0,319,320,
        5,22,0,0,320,51,1,0,0,0,321,322,7,2,0,0,322,53,1,0,0,0,323,328,5,
        40,0,0,324,328,3,16,8,0,325,328,3,40,20,0,326,328,3,10,5,0,327,323,
        1,0,0,0,327,324,1,0,0,0,327,325,1,0,0,0,327,326,1,0,0,0,328,55,1,
        0,0,0,329,332,3,54,27,0,330,332,5,41,0,0,331,329,1,0,0,0,331,330,
        1,0,0,0,332,57,1,0,0,0,333,334,7,3,0,0,334,59,1,0,0,0,335,336,7,
        4,0,0,336,61,1,0,0,0,35,65,71,77,89,94,96,98,111,113,115,120,125,
        129,132,137,148,152,160,164,175,179,188,192,223,237,249,261,269,
        280,289,293,310,317,327,331
    ]

class ListLanguageParser ( Parser ):

    grammarFileName = "ListLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'input'", "'print'", "'range'", "'def'", 
                     "'for'", "'while'", "'in'", "'if'", "'else'", "'elif'", 
                     "'get'", "'pop'", "'append'", "'remove'", "'clear'", 
                     "'return'", "':'", "'.'", "','", "'\"'", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "'='", "'+'", "'-'", "'*'", 
                     "'/'", "'**'", "'<'", "'>'", "'=='", "'>='", "'<='", 
                     "'<>'", "'!='" ]

    symbolicNames = [ "<INVALID>", "INPUT", "PRINT", "RANGE", "DEF", "FOR", 
                      "WHILE", "IN", "IF", "ELSE", "ELIF", "GET", "POP", 
                      "APPEND", "REMOVE", "CLEAR", "RETURN", "TWO_POINT", 
                      "POINT_FOR_M", "COMMA", "OPEN_CLOSE_EL", "OPEN_PAREN", 
                      "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", 
                      "CLOSE_BRACE", "ASSIGN", "ADD", "MINUS", "MUL", "DIV", 
                      "POW", "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", 
                      "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "ID", "NUM", "WS" ]

    RULE_program = 0
    RULE_block = 1
    RULE_statement = 2
    RULE_assign_element = 3
    RULE_operations = 4
    RULE_get_element = 5
    RULE_queue_init = 6
    RULE_list_init = 7
    RULE_elem_init = 8
    RULE_tree = 9
    RULE_if_block = 10
    RULE_if_init = 11
    RULE_else = 12
    RULE_elif = 13
    RULE_compare = 14
    RULE_for_block = 15
    RULE_for_init = 16
    RULE_while_block = 17
    RULE_while_init = 18
    RULE_sub_program = 19
    RULE_sub_program_call = 20
    RULE_print = 21
    RULE_range = 22
    RULE_input = 23
    RULE_return_def = 24
    RULE_method = 25
    RULE_methods = 26
    RULE_variables = 27
    RULE_variables_and_num = 28
    RULE_type = 29
    RULE_operation_list = 30

    ruleNames =  [ "program", "block", "statement", "assign_element", "operations", 
                   "get_element", "queue_init", "list_init", "elem_init", 
                   "tree", "if_block", "if_init", "else", "elif", "compare", 
                   "for_block", "for_init", "while_block", "while_init", 
                   "sub_program", "sub_program_call", "print", "range", 
                   "input", "return_def", "method", "methods", "variables", 
                   "variables_and_num", "type", "operation_list" ]

    EOF = Token.EOF
    INPUT=1
    PRINT=2
    RANGE=3
    DEF=4
    FOR=5
    WHILE=6
    IN=7
    IF=8
    ELSE=9
    ELIF=10
    GET=11
    POP=12
    APPEND=13
    REMOVE=14
    CLEAR=15
    RETURN=16
    TWO_POINT=17
    POINT_FOR_M=18
    COMMA=19
    OPEN_CLOSE_EL=20
    OPEN_PAREN=21
    CLOSE_PAREN=22
    OPEN_BRACK=23
    CLOSE_BRACK=24
    OPEN_BRACE=25
    CLOSE_BRACE=26
    ASSIGN=27
    ADD=28
    MINUS=29
    MUL=30
    DIV=31
    POW=32
    LESS_THAN=33
    GREATER_THAN=34
    EQUALS=35
    GT_EQ=36
    LT_EQ=37
    NOT_EQ_1=38
    NOT_EQ_2=39
    ID=40
    NUM=41
    WS=42

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sub_program(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.Sub_programContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.Sub_programContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return ListLanguageParser.RULE_program

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

        localctx = ListLanguageParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 62
                self.sub_program()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3298534949230) != 0):
                self.state = 68
                self.statement()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return ListLanguageParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ListLanguageParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 74
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 77 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_element(self):
            return self.getTypedRuleContext(ListLanguageParser.Assign_elementContext,0)


        def print_(self):
            return self.getTypedRuleContext(ListLanguageParser.PrintContext,0)


        def if_block(self):
            return self.getTypedRuleContext(ListLanguageParser.If_blockContext,0)


        def sub_program_call(self):
            return self.getTypedRuleContext(ListLanguageParser.Sub_program_callContext,0)


        def for_block(self):
            return self.getTypedRuleContext(ListLanguageParser.For_blockContext,0)


        def return_def(self):
            return self.getTypedRuleContext(ListLanguageParser.Return_defContext,0)


        def range_(self):
            return self.getTypedRuleContext(ListLanguageParser.RangeContext,0)


        def while_block(self):
            return self.getTypedRuleContext(ListLanguageParser.While_blockContext,0)


        def input_(self):
            return self.getTypedRuleContext(ListLanguageParser.InputContext,0)


        def method(self):
            return self.getTypedRuleContext(ListLanguageParser.MethodContext,0)


        def getRuleIndex(self):
            return ListLanguageParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ListLanguageParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.assign_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.print_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.if_block()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                self.sub_program_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 83
                self.for_block()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 84
                self.return_def()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 85
                self.range_()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 86
                self.while_block()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 87
                self.input_()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 88
                self.method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ListLanguageParser.ASSIGN, 0)

        def get_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.Get_elementContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.Get_elementContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ListLanguageParser.ID)
            else:
                return self.getToken(ListLanguageParser.ID, i)

        def list_init(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.List_initContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.List_initContext,i)


        def elem_init(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.Elem_initContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.Elem_initContext,i)


        def queue_init(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.Queue_initContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.Queue_initContext,i)


        def tree(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.TreeContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.TreeContext,i)


        def operations(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.OperationsContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.OperationsContext,i)


        def input_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.InputContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.InputContext,i)


        def method(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.MethodContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.MethodContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ListLanguageParser.COMMA)
            else:
                return self.getToken(ListLanguageParser.COMMA, i)

        def getRuleIndex(self):
            return ListLanguageParser.RULE_assign_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_element" ):
                listener.enterAssign_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_element" ):
                listener.exitAssign_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_element" ):
                return visitor.visitAssign_element(self)
            else:
                return visitor.visitChildren(self)




    def assign_element(self):

        localctx = ListLanguageParser.Assign_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assign_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 96
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 91
                    self.get_element()
                    pass

                elif la_ == 2:
                    self.state = 92
                    self.match(ListLanguageParser.ID)
                    self.state = 94
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==19:
                        self.state = 93
                        self.match(ListLanguageParser.COMMA)


                    pass


                self.state = 98 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==40):
                    break

            self.state = 100
            self.match(ListLanguageParser.ASSIGN)
            self.state = 113 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 113
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        self.state = 101
                        self.list_init()
                        pass

                    elif la_ == 2:
                        self.state = 102
                        self.elem_init()
                        pass

                    elif la_ == 3:
                        self.state = 103
                        self.queue_init()
                        pass

                    elif la_ == 4:
                        self.state = 104
                        self.tree()
                        pass

                    elif la_ == 5:
                        self.state = 105
                        self.operations()
                        pass

                    elif la_ == 6:
                        self.state = 106
                        self.input_()
                        pass

                    elif la_ == 7:
                        self.state = 107
                        self.get_element()
                        pass

                    elif la_ == 8:
                        self.state = 108
                        self.method()
                        pass

                    elif la_ == 9:
                        self.state = 109
                        self.match(ListLanguageParser.ID)
                        self.state = 111
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==19:
                            self.state = 110
                            self.match(ListLanguageParser.COMMA)


                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 115 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ListLanguageParser.OPEN_PAREN)
            else:
                return self.getToken(ListLanguageParser.OPEN_PAREN, i)

        def variables_and_num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.Variables_and_numContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.Variables_and_numContext,i)


        def operation_list(self):
            return self.getTypedRuleContext(ListLanguageParser.Operation_listContext,0)


        def CLOSE_PAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ListLanguageParser.CLOSE_PAREN)
            else:
                return self.getToken(ListLanguageParser.CLOSE_PAREN, i)

        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(ListLanguageParser.ADD)
            else:
                return self.getToken(ListLanguageParser.ADD, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(ListLanguageParser.MINUS)
            else:
                return self.getToken(ListLanguageParser.MINUS, i)

        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(ListLanguageParser.MUL)
            else:
                return self.getToken(ListLanguageParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(ListLanguageParser.DIV)
            else:
                return self.getToken(ListLanguageParser.DIV, i)

        def getRuleIndex(self):
            return ListLanguageParser.RULE_operations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperations" ):
                listener.enterOperations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperations" ):
                listener.exitOperations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperations" ):
                return visitor.visitOperations(self)
            else:
                return visitor.visitChildren(self)




    def operations(self):

        localctx = ListLanguageParser.OperationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_operations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 117
                self.match(ListLanguageParser.OPEN_PAREN)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 123
                    self.variables_and_num()
                    self.state = 125
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        self.state = 124
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4026531840) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()



                else:
                    raise NoViableAltException(self)
                self.state = 129 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8321499136) != 0):
                self.state = 131
                self.operation_list()


            self.state = 137
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 134
                    self.match(ListLanguageParser.CLOSE_PAREN) 
                self.state = 139
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Get_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ListLanguageParser.ID, 0)

        def OPEN_BRACK(self):
            return self.getToken(ListLanguageParser.OPEN_BRACK, 0)

        def NUM(self):
            return self.getToken(ListLanguageParser.NUM, 0)

        def CLOSE_BRACK(self):
            return self.getToken(ListLanguageParser.CLOSE_BRACK, 0)

        def getRuleIndex(self):
            return ListLanguageParser.RULE_get_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGet_element" ):
                listener.enterGet_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGet_element" ):
                listener.exitGet_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGet_element" ):
                return visitor.visitGet_element(self)
            else:
                return visitor.visitChildren(self)




    def get_element(self):

        localctx = ListLanguageParser.Get_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_get_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(ListLanguageParser.ID)
            self.state = 141
            self.match(ListLanguageParser.OPEN_BRACK)
            self.state = 142
            self.match(ListLanguageParser.NUM)
            self.state = 143
            self.match(ListLanguageParser.CLOSE_BRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Queue_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(ListLanguageParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(ListLanguageParser.CLOSE_PAREN, 0)

        def elem_init(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.Elem_initContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.Elem_initContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ListLanguageParser.COMMA)
            else:
                return self.getToken(ListLanguageParser.COMMA, i)

        def getRuleIndex(self):
            return ListLanguageParser.RULE_queue_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueue_init" ):
                listener.enterQueue_init(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueue_init" ):
                listener.exitQueue_init(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueue_init" ):
                return visitor.visitQueue_init(self)
            else:
                return visitor.visitChildren(self)




    def queue_init(self):

        localctx = ListLanguageParser.Queue_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_queue_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(ListLanguageParser.OPEN_PAREN)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40 or _la==41:
                self.state = 146
                self.elem_init()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 147
                    self.match(ListLanguageParser.COMMA)


                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 155
            self.match(ListLanguageParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACK(self):
            return self.getToken(ListLanguageParser.OPEN_BRACK, 0)

        def CLOSE_BRACK(self):
            return self.getToken(ListLanguageParser.CLOSE_BRACK, 0)

        def elem_init(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.Elem_initContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.Elem_initContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ListLanguageParser.COMMA)
            else:
                return self.getToken(ListLanguageParser.COMMA, i)

        def getRuleIndex(self):
            return ListLanguageParser.RULE_list_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_init" ):
                listener.enterList_init(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_init" ):
                listener.exitList_init(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_init" ):
                return visitor.visitList_init(self)
            else:
                return visitor.visitChildren(self)




    def list_init(self):

        localctx = ListLanguageParser.List_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_list_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(ListLanguageParser.OPEN_BRACK)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40 or _la==41:
                self.state = 158
                self.elem_init()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 159
                    self.match(ListLanguageParser.COMMA)


                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 167
            self.match(ListLanguageParser.CLOSE_BRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elem_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(ListLanguageParser.TypeContext,0)


        def getRuleIndex(self):
            return ListLanguageParser.RULE_elem_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElem_init" ):
                listener.enterElem_init(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElem_init" ):
                listener.exitElem_init(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElem_init" ):
                return visitor.visitElem_init(self)
            else:
                return visitor.visitChildren(self)




    def elem_init(self):

        localctx = ListLanguageParser.Elem_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_elem_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TreeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACK(self):
            return self.getToken(ListLanguageParser.OPEN_BRACK, 0)

        def CLOSE_BRACK(self):
            return self.getToken(ListLanguageParser.CLOSE_BRACK, 0)

        def elem_init(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.Elem_initContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.Elem_initContext,i)


        def tree(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.TreeContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.TreeContext,i)


        def getRuleIndex(self):
            return ListLanguageParser.RULE_tree

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTree" ):
                listener.enterTree(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTree" ):
                listener.exitTree(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTree" ):
                return visitor.visitTree(self)
            else:
                return visitor.visitChildren(self)




    def tree(self):

        localctx = ListLanguageParser.TreeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_tree)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(ListLanguageParser.OPEN_BRACK)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40 or _la==41:
                self.state = 172
                self.elem_init()
                self.state = 173
                self.tree()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 174
                    self.tree()


                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 182
            self.match(ListLanguageParser.CLOSE_BRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_init(self):
            return self.getTypedRuleContext(ListLanguageParser.If_initContext,0)


        def elif_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.ElifContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.ElifContext,i)


        def else_(self):
            return self.getTypedRuleContext(ListLanguageParser.ElseContext,0)


        def getRuleIndex(self):
            return ListLanguageParser.RULE_if_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_block" ):
                listener.enterIf_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_block" ):
                listener.exitIf_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_block" ):
                return visitor.visitIf_block(self)
            else:
                return visitor.visitChildren(self)




    def if_block(self):

        localctx = ListLanguageParser.If_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_if_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.if_init()
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 185
                self.elif_()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 191
                self.else_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ListLanguageParser.IF, 0)

        def OPEN_PAREN(self):
            return self.getToken(ListLanguageParser.OPEN_PAREN, 0)

        def variables_and_num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.Variables_and_numContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.Variables_and_numContext,i)


        def compare(self):
            return self.getTypedRuleContext(ListLanguageParser.CompareContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(ListLanguageParser.CLOSE_PAREN, 0)

        def OPEN_BRACE(self):
            return self.getToken(ListLanguageParser.OPEN_BRACE, 0)

        def block(self):
            return self.getTypedRuleContext(ListLanguageParser.BlockContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(ListLanguageParser.CLOSE_BRACE, 0)

        def getRuleIndex(self):
            return ListLanguageParser.RULE_if_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_init" ):
                listener.enterIf_init(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_init" ):
                listener.exitIf_init(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_init" ):
                return visitor.visitIf_init(self)
            else:
                return visitor.visitChildren(self)




    def if_init(self):

        localctx = ListLanguageParser.If_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_if_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(ListLanguageParser.IF)
            self.state = 195
            self.match(ListLanguageParser.OPEN_PAREN)
            self.state = 196
            self.variables_and_num()
            self.state = 197
            self.compare()
            self.state = 198
            self.variables_and_num()
            self.state = 199
            self.match(ListLanguageParser.CLOSE_PAREN)
            self.state = 200
            self.match(ListLanguageParser.OPEN_BRACE)
            self.state = 201
            self.block()
            self.state = 202
            self.match(ListLanguageParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ListLanguageParser.ELSE, 0)

        def OPEN_PAREN(self):
            return self.getToken(ListLanguageParser.OPEN_PAREN, 0)

        def block(self):
            return self.getTypedRuleContext(ListLanguageParser.BlockContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(ListLanguageParser.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return ListLanguageParser.RULE_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse" ):
                listener.enterElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse" ):
                listener.exitElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse" ):
                return visitor.visitElse(self)
            else:
                return visitor.visitChildren(self)




    def else_(self):

        localctx = ListLanguageParser.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(ListLanguageParser.ELSE)
            self.state = 205
            self.match(ListLanguageParser.OPEN_PAREN)
            self.state = 206
            self.block()
            self.state = 207
            self.match(ListLanguageParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ListLanguageParser.ELIF, 0)

        def OPEN_PAREN(self):
            return self.getToken(ListLanguageParser.OPEN_PAREN, 0)

        def variables_and_num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.Variables_and_numContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.Variables_and_numContext,i)


        def compare(self):
            return self.getTypedRuleContext(ListLanguageParser.CompareContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(ListLanguageParser.CLOSE_PAREN, 0)

        def OPEN_BRACE(self):
            return self.getToken(ListLanguageParser.OPEN_BRACE, 0)

        def block(self):
            return self.getTypedRuleContext(ListLanguageParser.BlockContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(ListLanguageParser.CLOSE_BRACE, 0)

        def getRuleIndex(self):
            return ListLanguageParser.RULE_elif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif" ):
                listener.enterElif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif" ):
                listener.exitElif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif" ):
                return visitor.visitElif(self)
            else:
                return visitor.visitChildren(self)




    def elif_(self):

        localctx = ListLanguageParser.ElifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(ListLanguageParser.ELIF)
            self.state = 210
            self.match(ListLanguageParser.OPEN_PAREN)
            self.state = 211
            self.variables_and_num()
            self.state = 212
            self.compare()
            self.state = 213
            self.variables_and_num()
            self.state = 214
            self.match(ListLanguageParser.CLOSE_PAREN)
            self.state = 215
            self.match(ListLanguageParser.OPEN_BRACE)
            self.state = 216
            self.block()
            self.state = 217
            self.match(ListLanguageParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(ListLanguageParser.EQUALS, 0)

        def ADD(self):
            return self.getToken(ListLanguageParser.ADD, 0)

        def MINUS(self):
            return self.getToken(ListLanguageParser.MINUS, 0)

        def MUL(self):
            return self.getToken(ListLanguageParser.MUL, 0)

        def DIV(self):
            return self.getToken(ListLanguageParser.DIV, 0)

        def GREATER_THAN(self):
            return self.getToken(ListLanguageParser.GREATER_THAN, 0)

        def GT_EQ(self):
            return self.getToken(ListLanguageParser.GT_EQ, 0)

        def LESS_THAN(self):
            return self.getToken(ListLanguageParser.LESS_THAN, 0)

        def LT_EQ(self):
            return self.getToken(ListLanguageParser.LT_EQ, 0)

        def getRuleIndex(self):
            return ListLanguageParser.RULE_compare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompare" ):
                listener.enterCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompare" ):
                listener.exitCompare(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare" ):
                return visitor.visitCompare(self)
            else:
                return visitor.visitChildren(self)




    def compare(self):

        localctx = ListLanguageParser.CompareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_compare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 270314504192) != 0)):
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


    class For_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_init(self):
            return self.getTypedRuleContext(ListLanguageParser.For_initContext,0)


        def else_(self):
            return self.getTypedRuleContext(ListLanguageParser.ElseContext,0)


        def getRuleIndex(self):
            return ListLanguageParser.RULE_for_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_block" ):
                listener.enterFor_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_block" ):
                listener.exitFor_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_block" ):
                return visitor.visitFor_block(self)
            else:
                return visitor.visitChildren(self)




    def for_block(self):

        localctx = ListLanguageParser.For_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_for_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.for_init()
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 222
                self.else_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ListLanguageParser.FOR, 0)

        def OPEN_PAREN(self):
            return self.getToken(ListLanguageParser.OPEN_PAREN, 0)

        def variables(self):
            return self.getTypedRuleContext(ListLanguageParser.VariablesContext,0)


        def IN(self):
            return self.getToken(ListLanguageParser.IN, 0)

        def variables_and_num(self):
            return self.getTypedRuleContext(ListLanguageParser.Variables_and_numContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(ListLanguageParser.CLOSE_PAREN, 0)

        def OPEN_BRACE(self):
            return self.getToken(ListLanguageParser.OPEN_BRACE, 0)

        def block(self):
            return self.getTypedRuleContext(ListLanguageParser.BlockContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(ListLanguageParser.CLOSE_BRACE, 0)

        def getRuleIndex(self):
            return ListLanguageParser.RULE_for_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_init" ):
                listener.enterFor_init(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_init" ):
                listener.exitFor_init(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_init" ):
                return visitor.visitFor_init(self)
            else:
                return visitor.visitChildren(self)




    def for_init(self):

        localctx = ListLanguageParser.For_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_for_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(ListLanguageParser.FOR)
            self.state = 226
            self.match(ListLanguageParser.OPEN_PAREN)
            self.state = 227
            self.variables()
            self.state = 228
            self.match(ListLanguageParser.IN)
            self.state = 229
            self.variables_and_num()
            self.state = 230
            self.match(ListLanguageParser.CLOSE_PAREN)
            self.state = 231
            self.match(ListLanguageParser.OPEN_BRACE)
            self.state = 232
            self.block()
            self.state = 233
            self.match(ListLanguageParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def while_init(self):
            return self.getTypedRuleContext(ListLanguageParser.While_initContext,0)


        def else_(self):
            return self.getTypedRuleContext(ListLanguageParser.ElseContext,0)


        def getRuleIndex(self):
            return ListLanguageParser.RULE_while_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_block" ):
                listener.enterWhile_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_block" ):
                listener.exitWhile_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_block" ):
                return visitor.visitWhile_block(self)
            else:
                return visitor.visitChildren(self)




    def while_block(self):

        localctx = ListLanguageParser.While_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_while_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.while_init()
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 236
                self.else_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ListLanguageParser.WHILE, 0)

        def OPEN_PAREN(self):
            return self.getToken(ListLanguageParser.OPEN_PAREN, 0)

        def variables_and_num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.Variables_and_numContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.Variables_and_numContext,i)


        def compare(self):
            return self.getTypedRuleContext(ListLanguageParser.CompareContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(ListLanguageParser.CLOSE_PAREN, 0)

        def OPEN_BRACE(self):
            return self.getToken(ListLanguageParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(ListLanguageParser.CLOSE_BRACE, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.BlockContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.BlockContext,i)


        def getRuleIndex(self):
            return ListLanguageParser.RULE_while_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_init" ):
                listener.enterWhile_init(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_init" ):
                listener.exitWhile_init(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_init" ):
                return visitor.visitWhile_init(self)
            else:
                return visitor.visitChildren(self)




    def while_init(self):

        localctx = ListLanguageParser.While_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_while_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(ListLanguageParser.WHILE)
            self.state = 240
            self.match(ListLanguageParser.OPEN_PAREN)
            self.state = 241
            self.variables_and_num()
            self.state = 242
            self.compare()
            self.state = 243
            self.variables_and_num()
            self.state = 244
            self.match(ListLanguageParser.CLOSE_PAREN)
            self.state = 245
            self.match(ListLanguageParser.OPEN_BRACE)
            self.state = 247 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 246
                self.block()
                self.state = 249 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3298534949230) != 0)):
                    break

            self.state = 251
            self.match(ListLanguageParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_programContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(ListLanguageParser.DEF, 0)

        def ID(self):
            return self.getToken(ListLanguageParser.ID, 0)

        def OPEN_PAREN(self):
            return self.getToken(ListLanguageParser.OPEN_PAREN, 0)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.TypeContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.TypeContext,i)


        def CLOSE_PAREN(self):
            return self.getToken(ListLanguageParser.CLOSE_PAREN, 0)

        def OPEN_BRACE(self):
            return self.getToken(ListLanguageParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(ListLanguageParser.CLOSE_BRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ListLanguageParser.COMMA)
            else:
                return self.getToken(ListLanguageParser.COMMA, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.BlockContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.BlockContext,i)


        def getRuleIndex(self):
            return ListLanguageParser.RULE_sub_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub_program" ):
                listener.enterSub_program(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub_program" ):
                listener.exitSub_program(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub_program" ):
                return visitor.visitSub_program(self)
            else:
                return visitor.visitChildren(self)




    def sub_program(self):

        localctx = ListLanguageParser.Sub_programContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_sub_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(ListLanguageParser.DEF)
            self.state = 254
            self.match(ListLanguageParser.ID)
            self.state = 255
            self.match(ListLanguageParser.OPEN_PAREN)
            self.state = 256
            self.type_()
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 257
                self.match(ListLanguageParser.COMMA)
                self.state = 258
                self.type_()
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 264
            self.match(ListLanguageParser.CLOSE_PAREN)
            self.state = 265
            self.match(ListLanguageParser.OPEN_BRACE)
            self.state = 267 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 266
                self.block()
                self.state = 269 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3298534949230) != 0)):
                    break

            self.state = 271
            self.match(ListLanguageParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_program_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ListLanguageParser.ID, 0)

        def OPEN_PAREN(self):
            return self.getToken(ListLanguageParser.OPEN_PAREN, 0)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.TypeContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.TypeContext,i)


        def CLOSE_PAREN(self):
            return self.getToken(ListLanguageParser.CLOSE_PAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ListLanguageParser.COMMA)
            else:
                return self.getToken(ListLanguageParser.COMMA, i)

        def getRuleIndex(self):
            return ListLanguageParser.RULE_sub_program_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub_program_call" ):
                listener.enterSub_program_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub_program_call" ):
                listener.exitSub_program_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub_program_call" ):
                return visitor.visitSub_program_call(self)
            else:
                return visitor.visitChildren(self)




    def sub_program_call(self):

        localctx = ListLanguageParser.Sub_program_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_sub_program_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(ListLanguageParser.ID)
            self.state = 274
            self.match(ListLanguageParser.OPEN_PAREN)
            self.state = 275
            self.type_()
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 276
                self.match(ListLanguageParser.COMMA)
                self.state = 277
                self.type_()
                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 283
            self.match(ListLanguageParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(ListLanguageParser.PRINT, 0)

        def OPEN_PAREN(self):
            return self.getToken(ListLanguageParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(ListLanguageParser.CLOSE_PAREN, 0)

        def variables_and_num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ListLanguageParser.Variables_and_numContext)
            else:
                return self.getTypedRuleContext(ListLanguageParser.Variables_and_numContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ListLanguageParser.COMMA)
            else:
                return self.getToken(ListLanguageParser.COMMA, i)

        def getRuleIndex(self):
            return ListLanguageParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = ListLanguageParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(ListLanguageParser.PRINT)
            self.state = 286
            self.match(ListLanguageParser.OPEN_PAREN)
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40 or _la==41:
                self.state = 287
                self.variables_and_num()
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 288
                    self.match(ListLanguageParser.COMMA)


                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 296
            self.match(ListLanguageParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RANGE(self):
            return self.getToken(ListLanguageParser.RANGE, 0)

        def OPEN_PAREN(self):
            return self.getToken(ListLanguageParser.OPEN_PAREN, 0)

        def variables_and_num(self):
            return self.getTypedRuleContext(ListLanguageParser.Variables_and_numContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(ListLanguageParser.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return ListLanguageParser.RULE_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange" ):
                listener.enterRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange" ):
                listener.exitRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange" ):
                return visitor.visitRange(self)
            else:
                return visitor.visitChildren(self)




    def range_(self):

        localctx = ListLanguageParser.RangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(ListLanguageParser.RANGE)
            self.state = 299
            self.match(ListLanguageParser.OPEN_PAREN)
            self.state = 300
            self.variables_and_num()
            self.state = 301
            self.match(ListLanguageParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(ListLanguageParser.INPUT, 0)

        def OPEN_PAREN(self):
            return self.getToken(ListLanguageParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(ListLanguageParser.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return ListLanguageParser.RULE_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput" ):
                listener.enterInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput" ):
                listener.exitInput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput" ):
                return visitor.visitInput(self)
            else:
                return visitor.visitChildren(self)




    def input_(self):

        localctx = ListLanguageParser.InputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_input)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(ListLanguageParser.INPUT)
            self.state = 304
            self.match(ListLanguageParser.OPEN_PAREN)
            self.state = 305
            self.match(ListLanguageParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ListLanguageParser.RETURN, 0)

        def ID(self):
            return self.getToken(ListLanguageParser.ID, 0)

        def NUM(self):
            return self.getToken(ListLanguageParser.NUM, 0)

        def getRuleIndex(self):
            return ListLanguageParser.RULE_return_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_def" ):
                listener.enterReturn_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_def" ):
                listener.exitReturn_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_def" ):
                return visitor.visitReturn_def(self)
            else:
                return visitor.visitChildren(self)




    def return_def(self):

        localctx = ListLanguageParser.Return_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_return_def)
        try:
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.match(ListLanguageParser.RETURN)
                self.state = 308
                self.match(ListLanguageParser.ID)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.match(ListLanguageParser.NUM)
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


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(ListLanguageParser.VariablesContext,0)


        def POINT_FOR_M(self):
            return self.getToken(ListLanguageParser.POINT_FOR_M, 0)

        def methods(self):
            return self.getTypedRuleContext(ListLanguageParser.MethodsContext,0)


        def OPEN_PAREN(self):
            return self.getToken(ListLanguageParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(ListLanguageParser.CLOSE_PAREN, 0)

        def variables_and_num(self):
            return self.getTypedRuleContext(ListLanguageParser.Variables_and_numContext,0)


        def getRuleIndex(self):
            return ListLanguageParser.RULE_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod" ):
                listener.enterMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod" ):
                listener.exitMethod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = ListLanguageParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.variables()
            self.state = 313
            self.match(ListLanguageParser.POINT_FOR_M)
            self.state = 314
            self.methods()
            self.state = 315
            self.match(ListLanguageParser.OPEN_PAREN)
            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40 or _la==41:
                self.state = 316
                self.variables_and_num()


            self.state = 319
            self.match(ListLanguageParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GET(self):
            return self.getToken(ListLanguageParser.GET, 0)

        def POP(self):
            return self.getToken(ListLanguageParser.POP, 0)

        def APPEND(self):
            return self.getToken(ListLanguageParser.APPEND, 0)

        def REMOVE(self):
            return self.getToken(ListLanguageParser.REMOVE, 0)

        def CLEAR(self):
            return self.getToken(ListLanguageParser.CLEAR, 0)

        def getRuleIndex(self):
            return ListLanguageParser.RULE_methods

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethods" ):
                listener.enterMethods(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethods" ):
                listener.exitMethods(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethods" ):
                return visitor.visitMethods(self)
            else:
                return visitor.visitChildren(self)




    def methods(self):

        localctx = ListLanguageParser.MethodsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_methods)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 63488) != 0)):
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


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ListLanguageParser.ID, 0)

        def elem_init(self):
            return self.getTypedRuleContext(ListLanguageParser.Elem_initContext,0)


        def sub_program_call(self):
            return self.getTypedRuleContext(ListLanguageParser.Sub_program_callContext,0)


        def get_element(self):
            return self.getTypedRuleContext(ListLanguageParser.Get_elementContext,0)


        def getRuleIndex(self):
            return ListLanguageParser.RULE_variables

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariables" ):
                listener.enterVariables(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariables" ):
                listener.exitVariables(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = ListLanguageParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_variables)
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(ListLanguageParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.elem_init()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 325
                self.sub_program_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 326
                self.get_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variables_and_numContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(ListLanguageParser.VariablesContext,0)


        def NUM(self):
            return self.getToken(ListLanguageParser.NUM, 0)

        def getRuleIndex(self):
            return ListLanguageParser.RULE_variables_and_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariables_and_num" ):
                listener.enterVariables_and_num(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariables_and_num" ):
                listener.exitVariables_and_num(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables_and_num" ):
                return visitor.visitVariables_and_num(self)
            else:
                return visitor.visitChildren(self)




    def variables_and_num(self):

        localctx = ListLanguageParser.Variables_and_numContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_variables_and_num)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.variables()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.match(ListLanguageParser.NUM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(ListLanguageParser.NUM, 0)

        def ID(self):
            return self.getToken(ListLanguageParser.ID, 0)

        def getRuleIndex(self):
            return ListLanguageParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = ListLanguageParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            _la = self._input.LA(1)
            if not(_la==40 or _la==41):
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


    class Operation_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(ListLanguageParser.ADD, 0)

        def MINUS(self):
            return self.getToken(ListLanguageParser.MINUS, 0)

        def DIV(self):
            return self.getToken(ListLanguageParser.DIV, 0)

        def MUL(self):
            return self.getToken(ListLanguageParser.MUL, 0)

        def POW(self):
            return self.getToken(ListLanguageParser.POW, 0)

        def getRuleIndex(self):
            return ListLanguageParser.RULE_operation_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation_list" ):
                listener.enterOperation_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation_list" ):
                listener.exitOperation_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation_list" ):
                return visitor.visitOperation_list(self)
            else:
                return visitor.visitChildren(self)




    def operation_list(self):

        localctx = ListLanguageParser.Operation_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_operation_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8321499136) != 0)):
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




