from antlr4 import *
from gen.ListLanguageLexer import ListLanguageLexer
from gen.ListLanguageParser import ListLanguageParser

from ListLanguageErrors import ListLanguageErrorListener

with open('test.txt', 'r') as text_file:
    test = text_file.read()
    input_stram = InputStream(test)
lexer = ListLanguageLexer(input_stram)
tokens = CommonTokenStream(lexer)
parser = ListLanguageParser(tokens)
error_listener = ListLanguageErrorListener()
parser.removeErrorListeners()
parser.addErrorListener(error_listener)
tree = parser.program()
