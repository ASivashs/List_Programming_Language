from colorama import Fore
from ast import literal_eval

from gen.ListLanguageVisitor import ListLanguageVisitor
from gen.ListLanguageParser import ListLanguageParser


class ListErrorVisitor(ListLanguageVisitor):

    def __init__(self, parser):
        self.variable_list = dict()
        self.subprogram_list = dict()
        self.visit(parser)

    def visitAssign_element(self, ctx:ListLanguageParser.Assign_elementContext):
        if ctx.ID():
            text = ctx.getText()
            assign = get_assign(text)
            if assign[0] != assign[1]:
                self.add_element_to_variables(assign[0], assign[1])

    def visitIf_block(self, ctx:ListLanguageParser.If_blockContext):
        self.visit(ctx.if_init())
        self.visit(ctx.elif_())

    def visitIf_init(self, ctx:ListLanguageParser.If_initContext):
        text = ctx.getText()
        text = text[text.find('(')+1:text.find(')')]
        if "==" in text:
            text = text.split("==")
        if ">=" in text:
            text = text.split(">=")
        if "<=" in text:
            text = text.split("<=")
        if "<>" in text:
            text = text.split("<>")
        if "!=" in text:
            text = text.split("!=")
        if '>' in text:
            text = text.split('>')
        if '<' in text:
            text = text.split('<')
        if text[0] not in self.variable_list.keys():
            if text[0] in self.variable_list.keys():
                text_type0 = self.variable_list[text[0]]["type"]
            else:
                text_type0 = get_type(text[0])
            if text[1] in self.variable_list.keys():
                text_type1 = self.variable_list[text[1]]["type"]
            else:
                text_type1 = get_type(text[1])

            if text_type0 != text_type1:
                print(f"{Fore.LIGHTRED_EX}Incorrect compare type in '{ctx.getText()}'. "
                      f"You cannot compare type '{text_type0}' and '{text_type1}'.{Fore.RESET}\n")
        else:
            print(f"{Fore.LIGHTRED_EX}Element doesnt exist in '{ctx.getText()}'.")

    def visitElif(self, ctx:ListLanguageParser.ElifContext):
        text = ctx.getText()
        text = text[text.find('(')+1:text.find(')')]
        if "==" in text:
            text = text.split("==")
        if ">=" in text:
            text = text.split(">=")
        if "<=" in text:
            text = text.split("<=")
        if "<>" in text:
            text = text.split("<>")
        if "!=" in text:
            text = text.split("!=")
        if '>' in text:
            text = text.split('>')
        if '<' in text:
            text = text.split('<')
        if text[0] in self.variable_list.keys():
            text_type0 = self.variable_list[text[0]]["type"]
        else:
            text_type0 = get_type(text[0])
        if text[1] in self.variable_list.keys():
            text_type1 = self.variable_list[text[1]]["type"]
        else:
            text_type1 = get_type(text[1])
        if text_type0 != text_type1:
            print(f"{Fore.LIGHTRED_EX}Incorrect compare type. "
                  f"You cannot compare type {text_type0} and {text_type1}.{Fore.RESET}\n")

    def visitWhile_block(self, ctx:ListLanguageParser.While_blockContext):
        self.visit(ctx.while_init())

    def visitWhile_init(self, ctx:ListLanguageParser.While_initContext):
        text = ctx.getText()
        text = text[text.find('(')+1:text.find(')')]
        if "==" in text:
            text = text.split("==")
        if ">=" in text:
            text = text.split(">=")
        if "<=" in text:
            text = text.split("<=")
        if "<>" in text:
            text = text.split("<>")
        if "!=" in text:
            text = text.split("!=")
        if '>' in text:
            text = text.split('>')
        if '<' in text:
            text = text.split('<')
        if text[0] in self.variable_list.keys():
            text_type0 = self.variable_list[text[0]]["type"]
        else:
            text_type0 = get_type(text[0])
        if text[1] in self.variable_list.keys():
            text_type1 = self.variable_list[text[1]]["type"]
        else:
            text_type1 = get_type(text[1])
        if text_type0 != text_type1:
            print(f"{Fore.LIGHTRED_EX}Incorrect compare type in '{ctx.getText()}'. "
                  f"You cannot compare type '{text_type0}' and '{text_type1}'.{Fore.RESET}\n")

    def visitFor_block(self, ctx:ListLanguageParser.For_blockContext):
        self.visit(ctx.for_init())

    def visitFor_init(self, ctx:ListLanguageParser.For_initContext):
        text = ctx.getText()
        text = text[text.find('(')+1:text.find(')')]
        text = text.split("in")
        if text[0] in self.variable_list.keys():
            text_type0 = self.variable_list[text[0]]["type"]
        else:
            text_type0 = get_type(text[0])
        if text[1] in self.variable_list.keys():
            text_type1 = self.variable_list[text[1]]["type"]
        else:
            text_type1 = get_type(text[1])
        if text_type0 != text_type1:
            print(f"{Fore.LIGHTRED_EX}Incorrect compare type in '{ctx.getText()}'. "
                  f"You cannot compare type '{text_type0}' and '{text_type1}'.{Fore.RESET}\n")

    # def visitSub_program(self, ctx:ListLanguageParser.Sub_programContext):
    #     text = ctx.getText()
    #     subprogramm_name = text[2:text.find(')')]
    #     subprogramm_args = text[text.find('(')+1:text.find(')')]
    #     if subprogramm_name not in self.variable_list.keys():
    #         if ',' in subprogramm_args:
    #             subprogramm_args = subprogramm_args.split(',')
    #         if subprogramm_name not in self.subprogram_list.keys():
    #             self.add_subprogramm_to_subprogramm_list(subprogramm_name, subprogramm_args)
    #         if subprogramm_name in self.subprogram_list.keys():
    #             self.subprogram_list[subprogramm_name] = subprogramm_args

    # def visitSub_program_call(self, ctx:ListLanguageParser.Sub_program_callContext):
    #     text = ctx.getText()
    #     subprogramm_name = text.split('(')[0]
    #     if subprogramm_name not in self.subprogram_list.keys():
    #         print(f"{Fore.LIGHTRED_EX}Subprogramm with this name doesnt exist.{Fore.RESET}")
    #     subprogramm_args = text[text.find('(') + 1:text.find(')')]
    #     if ',' in subprogramm_args:
    #         subprogramm_args = subprogramm_args.split(',')
    #     else:
    #         subprogramm_args = [subprogramm_args]
    #     if len(subprogramm_args) != len(self.subprogram_list[subprogramm_name]):
    #         print(f"{Fore.LIGHTRED_EX}Incorrect count of arguments in subprogramm."
    #               f" This element contain {len(subprogramm_args)}.{Fore.RESET}")

    def add_element_to_variables(self, variable_name: str, variable: str):
        self.variable_list[variable_name] = {
            "type": get_type(variable),
            "variable": variable,
        }

    def add_subprogramm_to_subprogramm_list(self, subprogramm_name: str, arguments: list):
        self.subprogram_list[subprogramm_name] = arguments


def get_type(expression: str):
    if expression.isdigit():
        return "int"
    if expression.isalpha():
        return "str"
    if any(operation in expression for operation in ('+', '-', '*', '/')):
        return "operation"
    if '[' in expression:
        return "list"
    if '(' in expression:
        return "queue"


def translate_to_python_obj(expression: str):
    try:
        obj = literal_eval(expression)
        return obj
    except Exception:
        return expression


def check_iterable_obj(expression: str):
    if expression.find('['):
        return False
    return True


def get_assign(assign: str):
    assign = assign.split('=')
    return assign
