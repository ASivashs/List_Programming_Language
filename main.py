from antlr4 import *
from gen.ListLanguageLexer import ListLanguageLexer
from gen.ListLanguageParser import ListLanguageParser

from ListErrorListener import ListErrorListener


def main():
    with open('test.txt', 'r') as text_file:
        test = text_file.read()
        input_stream = InputStream(test)
    lexer = ListLanguageLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ListLanguageParser(stream)
    parser.removeErrorListeners()
    syntax_error_listener = ListErrorListener()
    parser.addErrorListener(syntax_error_listener)
    tree = parser.program()


if __name__ == "__main__":
    main()


# Main for version with strategy

# with open('test.txt', 'r') as text_file:
#     test = text_file.read()
#     # print(test)
#     input_stream = InputStream(test)
# lexer = ListLanguageLexer(input_stream)
# tokens = CommonTokenStream(lexer)
# parser = ListLanguageParser(tokens)
# parser.removeErrorListeners()
# parser.addErrorListener(ListErrorListener)
# error_listener = ListErrorListener()
# parser.addErrorListener(error_listener)
# tree = parser.program()
