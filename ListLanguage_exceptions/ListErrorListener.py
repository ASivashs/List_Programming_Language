from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import NoViableAltException, InputMismatchException, UnsupportedOperationException

from colorama import Fore


class ListErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, type_error):
        if isinstance(type_error, InputMismatchException):
            expected_tokens = type_error.getExpectedTokens().toString(recognizer.literalNames, recognizer.symbolicNames)
            offend_symbol = offendingSymbol.text
            print(f"{Fore.LIGHTRED_EX}Syntax error: mismatched input '{offend_symbol}' at line {line}, column {column}.\n"
                  f"Expected one of the following tokens: {expected_tokens}.{Fore.RESET}")
        elif isinstance(type_error, NoViableAltException):
            print(f"{Fore.LIGHTRED_EX}Syntax error: {msg} at line {line}, column {column}.{Fore.RESET}")
        else:
            print(f"{Fore.LIGHTRED_EX}Syntax error at line {line}, column {column}: {msg}.{Fore.RESET}")
        underline_error(recognizer, line, column)


def underline_error(recognizer, line, col):
    tokens = recognizer.getInputStream()
    input_str = str(tokens.tokenSource.inputStream)
    lines = input_str.split('\n')
    error_line = lines[line - 1]
    print(error_line)
    if error_line:
        print(' ' * col + Fore.LIGHTRED_EX + '^' + Fore.RESET)


#  Version with strategy

# class ListErrorListener(ErrorListener):
#     def __init__(self):
#         super().__init__()
#
#     def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
#         print(f"Error in line {line}: {column} - {msg}")
