from antlr4.error.ErrorListener import ErrorListener


class ListLanguageErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f'line {line}: {column} {msg}'
        raise Exception(error_msg)
