# Generated from D:/.desktop_backup/temp/.3/PPL/BTL/tyc-compiler/src/grammar/TyC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TyCParser import TyCParser
else:
    from TyCParser import TyCParser

# This class defines a complete generic visitor for a parse tree produced by TyCParser.

class TyCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TyCParser#program.
    def visitProgram(self, ctx:TyCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#decl_list.
    def visitDecl_list(self, ctx:TyCParser.Decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#non_empty_decl_list.
    def visitNon_empty_decl_list(self, ctx:TyCParser.Non_empty_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#decl.
    def visitDecl(self, ctx:TyCParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#struct_decl.
    def visitStruct_decl(self, ctx:TyCParser.Struct_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#struct_member_decl_list.
    def visitStruct_member_decl_list(self, ctx:TyCParser.Struct_member_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#non_empty_struct_member_decl_list.
    def visitNon_empty_struct_member_decl_list(self, ctx:TyCParser.Non_empty_struct_member_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#struct_member_decl.
    def visitStruct_member_decl(self, ctx:TyCParser.Struct_member_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#struct_literal.
    def visitStruct_literal(self, ctx:TyCParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#struct_literal_members.
    def visitStruct_literal_members(self, ctx:TyCParser.Struct_literal_membersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr_list.
    def visitExpr_list(self, ctx:TyCParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#func_decl.
    def visitFunc_decl(self, ctx:TyCParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#return_type.
    def visitReturn_type(self, ctx:TyCParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#param_list.
    def visitParam_list(self, ctx:TyCParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#non_empty_param_list.
    def visitNon_empty_param_list(self, ctx:TyCParser.Non_empty_param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#param_decl.
    def visitParam_decl(self, ctx:TyCParser.Param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#statement_list.
    def visitStatement_list(self, ctx:TyCParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#non_empty_statement_list.
    def visitNon_empty_statement_list(self, ctx:TyCParser.Non_empty_statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#statement.
    def visitStatement(self, ctx:TyCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#block_statement.
    def visitBlock_statement(self, ctx:TyCParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#var_decl_statement.
    def visitVar_decl_statement(self, ctx:TyCParser.Var_decl_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#var_decl.
    def visitVar_decl(self, ctx:TyCParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#type_decl.
    def visitType_decl(self, ctx:TyCParser.Type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#if_statement.
    def visitIf_statement(self, ctx:TyCParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#if_else_statement.
    def visitIf_else_statement(self, ctx:TyCParser.If_else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#while_statement.
    def visitWhile_statement(self, ctx:TyCParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#for_statement.
    def visitFor_statement(self, ctx:TyCParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#for_init.
    def visitFor_init(self, ctx:TyCParser.For_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#for_cond.
    def visitFor_cond(self, ctx:TyCParser.For_condContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#for_update.
    def visitFor_update(self, ctx:TyCParser.For_updateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#switch_statement.
    def visitSwitch_statement(self, ctx:TyCParser.Switch_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#case_list.
    def visitCase_list(self, ctx:TyCParser.Case_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#non_empty_case_list.
    def visitNon_empty_case_list(self, ctx:TyCParser.Non_empty_case_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#case_element.
    def visitCase_element(self, ctx:TyCParser.Case_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#case_default.
    def visitCase_default(self, ctx:TyCParser.Case_defaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#break_statement.
    def visitBreak_statement(self, ctx:TyCParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#continue_statement.
    def visitContinue_statement(self, ctx:TyCParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#return_statement.
    def visitReturn_statement(self, ctx:TyCParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr_statement.
    def visitExpr_statement(self, ctx:TyCParser.Expr_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr.
    def visitExpr(self, ctx:TyCParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr_pred_0.
    def visitExpr_pred_0(self, ctx:TyCParser.Expr_pred_0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr_pred_1.
    def visitExpr_pred_1(self, ctx:TyCParser.Expr_pred_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr_pred_2.
    def visitExpr_pred_2(self, ctx:TyCParser.Expr_pred_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr_pred_3.
    def visitExpr_pred_3(self, ctx:TyCParser.Expr_pred_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr_pred_4.
    def visitExpr_pred_4(self, ctx:TyCParser.Expr_pred_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr_pred_5.
    def visitExpr_pred_5(self, ctx:TyCParser.Expr_pred_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr_pred_6.
    def visitExpr_pred_6(self, ctx:TyCParser.Expr_pred_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr_pred_7.
    def visitExpr_pred_7(self, ctx:TyCParser.Expr_pred_7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr_pred_8.
    def visitExpr_pred_8(self, ctx:TyCParser.Expr_pred_8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr_pred_9.
    def visitExpr_pred_9(self, ctx:TyCParser.Expr_pred_9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr_pred_10.
    def visitExpr_pred_10(self, ctx:TyCParser.Expr_pred_10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr_prefix_inc_or_dec.
    def visitExpr_prefix_inc_or_dec(self, ctx:TyCParser.Expr_prefix_inc_or_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr_postfix_inc_or_dec.
    def visitExpr_postfix_inc_or_dec(self, ctx:TyCParser.Expr_postfix_inc_or_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#inc_or_dec_expr.
    def visitInc_or_dec_expr(self, ctx:TyCParser.Inc_or_dec_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#assignment_expr.
    def visitAssignment_expr(self, ctx:TyCParser.Assignment_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr_member_access.
    def visitExpr_member_access(self, ctx:TyCParser.Expr_member_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#operand_func_call.
    def visitOperand_func_call(self, ctx:TyCParser.Operand_func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#operand_list.
    def visitOperand_list(self, ctx:TyCParser.Operand_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#non_empty_operand_list.
    def visitNon_empty_operand_list(self, ctx:TyCParser.Non_empty_operand_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#operand.
    def visitOperand(self, ctx:TyCParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#sub_expr.
    def visitSub_expr(self, ctx:TyCParser.Sub_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#explicit_type.
    def visitExplicit_type(self, ctx:TyCParser.Explicit_typeContext):
        return self.visitChildren(ctx)



del TyCParser