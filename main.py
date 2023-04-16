from antlr4 import *
from gen.ListLanguageLexer import ListLanguageLexer
from gen.ListLanguageParser import ListLanguageParser
from gen.ListLanguageVisitor import ListLanguageVisitor
from ListErrorListener import ListErrorListener
from ListErrorStrategy import ListErrorStrategy


def main():
    with open('test.txt', 'r') as test_file:
        test = test_file.read()
        input_stream = InputStream(test)
    lexer = ListLanguageLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ListLanguageParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(ListErrorListener())
    parser.resetErrHandler(ListErrorStrategy())
    tree = parser.program()
    visitor = ListLanguageVisitor()
    output = visitor.visit(tree)
    print(tree)
    return output


if __name__ == '__main__':
    main()


# from antlr4 import *
# from gen.ListLanguageLexer import ListLanguageLexer
# from gen.ListLanguageParser import ListLanguageParser
#
# from ListErrorListener import ListErrorListener
#
#
# with open('test.txt', 'r') as text_file:
#     test = text_file.read()
#     print(test)
#     input_stream = InputStream(test)
# lexer = ListLanguageLexer(input_stream)
# tokens = CommonTokenStream(lexer)
# parser = ListLanguageParser(tokens)
# parser.removeErrorListeners()
# error_listener = ListErrorListener()
# parser.addErrorListener(error_listener)
# tree = parser.program()
