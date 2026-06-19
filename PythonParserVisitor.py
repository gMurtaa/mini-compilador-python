# Generated from PythonParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete generic visitor for a parse tree produced by PythonParser.

class PythonParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PythonParser#code.
    def visitCode(self, ctx:PythonParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#statAssignment.
    def visitStatAssignment(self, ctx:PythonParser.StatAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#statReturn.
    def visitStatReturn(self, ctx:PythonParser.StatReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#statExpr.
    def visitStatExpr(self, ctx:PythonParser.StatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#condicional.
    def visitCondicional(self, ctx:PythonParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#bloco.
    def visitBloco(self, ctx:PythonParser.BlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#func.
    def visitFunc(self, ctx:PythonParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#params.
    def visitParams(self, ctx:PythonParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#func_call.
    def visitFunc_call(self, ctx:PythonParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#args.
    def visitArgs(self, ctx:PythonParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#loop_while.
    def visitLoop_while(self, ctx:PythonParser.Loop_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#loop_for.
    def visitLoop_for(self, ctx:PythonParser.Loop_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#lista.
    def visitLista(self, ctx:PythonParser.ListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#tupla.
    def visitTupla(self, ctx:PythonParser.TuplaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#set_lit.
    def visitSet_lit(self, ctx:PythonParser.Set_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#par_chave_valor.
    def visitPar_chave_valor(self, ctx:PythonParser.Par_chave_valorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#dicionario.
    def visitDicionario(self, ctx:PythonParser.DicionarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expDecimal.
    def visitExpDecimal(self, ctx:PythonParser.ExpDecimalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expPotencia.
    def visitExpPotencia(self, ctx:PythonParser.ExpPotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expModulo.
    def visitExpModulo(self, ctx:PythonParser.ExpModuloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expParenteses.
    def visitExpParenteses(self, ctx:PythonParser.ExpParentesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expInteiro.
    def visitExpInteiro(self, ctx:PythonParser.ExpInteiroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expMultiplicacao.
    def visitExpMultiplicacao(self, ctx:PythonParser.ExpMultiplicacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expAdicao.
    def visitExpAdicao(self, ctx:PythonParser.ExpAdicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expString.
    def visitExpString(self, ctx:PythonParser.ExpStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expTupla.
    def visitExpTupla(self, ctx:PythonParser.ExpTuplaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expMaiorIgual.
    def visitExpMaiorIgual(self, ctx:PythonParser.ExpMaiorIgualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expMenor.
    def visitExpMenor(self, ctx:PythonParser.ExpMenorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expFuncCall.
    def visitExpFuncCall(self, ctx:PythonParser.ExpFuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expDiferente.
    def visitExpDiferente(self, ctx:PythonParser.ExpDiferenteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expMaior.
    def visitExpMaior(self, ctx:PythonParser.ExpMaiorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expDivisao.
    def visitExpDivisao(self, ctx:PythonParser.ExpDivisaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expDicionario.
    def visitExpDicionario(self, ctx:PythonParser.ExpDicionarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expId.
    def visitExpId(self, ctx:PythonParser.ExpIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expDivisaoInteira.
    def visitExpDivisaoInteira(self, ctx:PythonParser.ExpDivisaoInteiraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expOu.
    def visitExpOu(self, ctx:PythonParser.ExpOuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expLista.
    def visitExpLista(self, ctx:PythonParser.ExpListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expE.
    def visitExpE(self, ctx:PythonParser.ExpEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expMenorIgual.
    def visitExpMenorIgual(self, ctx:PythonParser.ExpMenorIgualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expNegacao.
    def visitExpNegacao(self, ctx:PythonParser.ExpNegacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expSet.
    def visitExpSet(self, ctx:PythonParser.ExpSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expIgual.
    def visitExpIgual(self, ctx:PythonParser.ExpIgualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expFalso.
    def visitExpFalso(self, ctx:PythonParser.ExpFalsoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expSubtracao.
    def visitExpSubtracao(self, ctx:PythonParser.ExpSubtracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expVerdadeiro.
    def visitExpVerdadeiro(self, ctx:PythonParser.ExpVerdadeiroContext):
        return self.visitChildren(ctx)



del PythonParser