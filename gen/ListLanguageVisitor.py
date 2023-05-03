# Generated from C:/University/6_sem/YAPIS/grammar\ListLanguage.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ListLanguageParser import ListLanguageParser
else:
    from ListLanguageParser import ListLanguageParser

# This class defines a complete generic visitor for a parse tree produced by ListLanguageParser.

class ListLanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ListLanguageParser#program.
    def visitProgram(self, ctx:ListLanguageParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#block.
    def visitBlock(self, ctx:ListLanguageParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#statement.
    def visitStatement(self, ctx:ListLanguageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#assign_element.
    def visitAssign_element(self, ctx:ListLanguageParser.Assign_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#operations.
    def visitOperations(self, ctx:ListLanguageParser.OperationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#get_element.
    def visitGet_element(self, ctx:ListLanguageParser.Get_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#queue_init.
    def visitQueue_init(self, ctx:ListLanguageParser.Queue_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#list_init.
    def visitList_init(self, ctx:ListLanguageParser.List_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#elem_init.
    def visitElem_init(self, ctx:ListLanguageParser.Elem_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#tree.
    def visitTree(self, ctx:ListLanguageParser.TreeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#if_block.
    def visitIf_block(self, ctx:ListLanguageParser.If_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#if_init.
    def visitIf_init(self, ctx:ListLanguageParser.If_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#else.
    def visitElse(self, ctx:ListLanguageParser.ElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#elif.
    def visitElif(self, ctx:ListLanguageParser.ElifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#compare.
    def visitCompare(self, ctx:ListLanguageParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#for_block.
    def visitFor_block(self, ctx:ListLanguageParser.For_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#for_init.
    def visitFor_init(self, ctx:ListLanguageParser.For_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#while_block.
    def visitWhile_block(self, ctx:ListLanguageParser.While_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#while_init.
    def visitWhile_init(self, ctx:ListLanguageParser.While_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#sub_program.
    def visitSub_program(self, ctx:ListLanguageParser.Sub_programContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#sub_program_call.
    def visitSub_program_call(self, ctx:ListLanguageParser.Sub_program_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#print.
    def visitPrint(self, ctx:ListLanguageParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#range.
    def visitRange(self, ctx:ListLanguageParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#input.
    def visitInput(self, ctx:ListLanguageParser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#return_def.
    def visitReturn_def(self, ctx:ListLanguageParser.Return_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#method.
    def visitMethod(self, ctx:ListLanguageParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#methods.
    def visitMethods(self, ctx:ListLanguageParser.MethodsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#variables.
    def visitVariables(self, ctx:ListLanguageParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#variables_and_num.
    def visitVariables_and_num(self, ctx:ListLanguageParser.Variables_and_numContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#type.
    def visitType(self, ctx:ListLanguageParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ListLanguageParser#operation_list.
    def visitOperation_list(self, ctx:ListLanguageParser.Operation_listContext):
        return self.visitChildren(ctx)



del ListLanguageParser