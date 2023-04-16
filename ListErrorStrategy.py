from antlr4.error.Errors import RecognitionException, NoViableAltException, InputMismatchException, \
    FailedPredicateException
from antlr4.error.ErrorStrategy import DefaultErrorStrategy
from antlr4 import *

from gen.ListLanguageParser import ListLanguageParser


class ListErrorStrategy(DefaultErrorStrategy):
    def __init__(self):
        super().__init__()

    def reportError(self, recognizer: Parser, e: RecognitionException, localctx: ParserRuleContext = None):
        # if we've already reported an error and have not matched a token
        # yet successfully, don't report any errors.
        if self.inErrorRecoveryMode(recognizer):
            return  # don't report spurious errors
        self.beginErrorCondition(recognizer)
        if isinstance(e, NoViableAltException):
            msg = self.checkContext(localctx)
            self.reportNoViableAlternative(recognizer, e, msg)
        elif isinstance(e, InputMismatchException):
            msg = self.checkContext(localctx)
            self.reportInputMismatch(recognizer, e, msg)
        elif isinstance(e, FailedPredicateException):
            msg = self.checkContext(localctx)
            self.reportFailedPredicate(recognizer, e, msg)
        else:
            print("unknown recognition error type: " + type(e).__name__)
            recognizer.notifyErrorListeners(e.message, e.offendingToken, e)

    def checkContext(self, localctx: ParserRuleContext):
        msg = None
        print(type(localctx))

        # For
        if isinstance(localctx, ListLanguageParser.For_initContext):
            msg = "For statement mismatched input - {}. Expected expression like for(<>;<>;<>)..."
        elif isinstance(localctx, ListLanguageParser.For_blockContext):
            msg = "IF/Else statement mismatched input - {}. Expected for have another form."

        # If
        elif isinstance(localctx, ListLanguageParser.If_initContext):
            msg = "IF statement mismatched input - {}. Expected expression like if compare <elif> <else >."
        elif isinstance(localctx, ListLanguageParser.If_blockContext):
            msg = "IF/Else statement mismatched input - {}. Expected expression like if compare <elif> <else >."
        elif isinstance(localctx, ListLanguageParser.ElseContext):
            msg = "Else statement mismatched input - {}. Expected expression like if compare <elif> <else >."
        elif isinstance(localctx, ListLanguageParser.ElifContext):
            msg = "Elif statement mismatched input - {}. Expected expression like if compare <elif> <else >."
        elif isinstance(localctx, ListLanguageParser.CompareContext):
            msg = "Compare statement mismatched input - {}. Expected boolean expression."

        # While
        elif isinstance(localctx, ListLanguageParser.While_initContext):
            msg = "While statement mismatched form - {}. Expected while(boolExpr)..."
        elif isinstance(localctx, ListLanguageParser.While_blockContext):
            msg = "While statement mismatched form - {}. Expected while have another form."

        # Operations
        elif isinstance(localctx, ListLanguageParser.OperationsContext):
            msg = "Operations expression mismatched form - {}. Expected expression <type> ID [= value];"
        elif isinstance(localctx, ListLanguageParser.Assign_elementContext):
            msg = "Assign expression mismatched form - {}. Expected expression <type> ID [= value];"
        elif isinstance(localctx, ListLanguageParser.Get_elementContext):
            msg = "Get list element mismatched form - {}. Expected brackets."

        # Basic func
        elif isinstance(localctx, ListLanguageParser.PrintContext):
            msg = "Print function mismatched form - {}. Expected print(<value>);"
        elif isinstance(localctx, ListLanguageParser.RangeContext):
            msg = "Range function mismatched form - {}. Expected range(<value>);"
        elif isinstance(localctx, ListLanguageParser.InputContext):
            msg = "Input function mismatched form - {}. Expected input(<value>);"
        elif isinstance(localctx, ListLanguageParser.Return_defContext):
            msg = "Return function mismatched form - {}. Expected return value;"
        elif isinstance(localctx, ListLanguageParser.MethodContext):
            msg = "Method function mismatched form - {}. Expected <value>.method;"

        # Def
        elif isinstance(localctx, ListLanguageParser.Sub_programContext):
            msg = "Function definition mismatched form - {}. Expected <type> function ID (params)."
        elif isinstance(localctx, ListLanguageParser.Sub_program_callContext):
            msg = "Function definition mismatched form - {}. Expected <type> function ID (params)."

        # Variables and init
        elif isinstance(localctx, ListLanguageParser.MethodsContext):
            msg = "Variable or integer statement mismatched form - {}. Expected basic_type <name> value?"
        elif isinstance(localctx, ListLanguageParser.Variables_and_numContext):
            msg = "Variable or integer statement mismatched form - {}. Expected basic_type <name> value?"
        elif isinstance(localctx, ListLanguageParser.VariablesContext):
            msg = "Variable declaration mismatched form - {}. Expected basic_type <name> value?"
        elif isinstance(localctx, ListLanguageParser.Queue_initContext):
            msg = "Queue declaration mismatched form - {}. Expected basic_type <name> value?"
        elif isinstance(localctx, ListLanguageParser.List_initContext):
            msg = "List declaration mismatched form - {}. Expected basic_type <name> value?"
        elif isinstance(localctx, ListLanguageParser.Elem_initContext):
            msg = "Element declaration mismatched form - {}. Expected basic_type <name> value?"
        elif isinstance(localctx, ListLanguageParser.TreeContext):
            msg = "Tree declaration mismatched form - {}. Expected basic_type <name> value?"
        elif isinstance(localctx, ListLanguageParser.TypeContext):
            msg = "Type declaration mismatched form - {}. Expected basic_type <name> value?"
        elif isinstance(localctx, ListLanguageParser.Operation_listContext):
            msg = "Operation declaration mismatched form - {}. Expected basic_type <name> value?"
        return msg

    def reportNoViableAlternative(self, recognizer: Parser, e: NoViableAltException, msg: str = None):
        tokens = recognizer.getTokenStream()
        if tokens is not None:
            if e.startToken.type == Token.EOF:
                inp = "<EOF>"
            else:
                print("getText")
                inp = tokens.getText((e.startToken, e.offendingToken))
        else:
            inp = "<unknown input>"
        if msg:
            msg = msg.format(self.escapeWSAndQuote(inp))
        else:
            msg = "Name " + self.escapeWSAndQuote(inp) + " is not defined"
        recognizer.notifyErrorListeners(msg, e.offendingToken, e)

    def reportInputMismatch(self, recognizer: Parser, e: InputMismatchException, msg: str = None):
        if msg:
            msg = msg.format(self.getTokenErrorDisplay(e.offendingToken))
        if not msg:
            msg = "mismatched input " + self.getTokenErrorDisplay(e.offendingToken) \
                  + " expecting " + e.getExpectedTokens().toString(recognizer.literalNames, recognizer.symbolicNames)
        recognizer.notifyErrorListeners(msg, e.offendingToken, e)

    def reportFailedPredicate(self, recognizer, e, msg: str = None):
        rule_name = recognizer.ruleNames[recognizer._ctx.getRuleIndex()]
        msg = msg.format(rule_name)
        if not msg:
            msg = "rule " + rule_name + " " + e.message
        recognizer.notifyErrorListeners(msg, e.offendingToken, e)

