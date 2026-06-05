if "." in __name__:
    from .PythonParser import PythonParser
    from .PythonParserVisitor import PythonParserVisitor
else:
    from PythonParser import PythonParser
    from PythonParserVisitor import PythonParserVisitor

class Compiler(PythonParserVisitor):

    def __init__(self):
        super(Compiler, self).__init__()
        self.vars = {}
        return None
    
    # Visit a parse tree produced by PythonParser#code.
    def visitCode(self, ctx:PythonParser.CodeContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#stat.
    def visitStat(self, ctx:PythonParser.StatContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#condicional.
    def visitCondicional(self, ctx:PythonParser.CondicionalContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#bloco.
    def visitBloco(self, ctx:PythonParser.BlocoContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#func.
    def visitFunc(self, ctx:PythonParser.FuncContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#params.
    def visitParams(self, ctx:PythonParser.ParamsContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#func_call.
    def visitFunc_call(self, ctx:PythonParser.Func_callContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#args.
    def visitArgs(self, ctx:PythonParser.ArgsContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#loop_while.
    def visitLoop_while(self, ctx:PythonParser.Loop_whileContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#loop_for.
    def visitLoop_for(self, ctx:PythonParser.Loop_forContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#lista.
    def visitLista(self, ctx:PythonParser.ListaContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#tupla.
    def visitTupla(self, ctx:PythonParser.TuplaContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#set_lit.
    def visitSet_lit(self, ctx:PythonParser.Set_litContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#par_chave_valor.
    def visitPar_chave_valor(self, ctx:PythonParser.Par_chave_valorContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#dicionario.
    def visitDicionario(self, ctx:PythonParser.DicionarioContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expDecimal.
    def visitExpDecimal(self, ctx:PythonParser.ExpDecimalContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expPotencia.
    def visitExpPotencia(self, ctx:PythonParser.ExpPotenciaContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expModulo.
    def visitExpModulo(self, ctx:PythonParser.ExpModuloContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expParenteses.
    def visitExpParenteses(self, ctx:PythonParser.ExpParentesesContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expInteiro.
    def visitExpInteiro(self, ctx:PythonParser.ExpInteiroContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expMultiplicacao.
    def visitExpMultiplicacao(self, ctx:PythonParser.ExpMultiplicacaoContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expAdicao.
    def visitExpAdicao(self, ctx:PythonParser.ExpAdicaoContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expString.
    def visitExpString(self, ctx:PythonParser.ExpStringContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expTupla.
    def visitExpTupla(self, ctx:PythonParser.ExpTuplaContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expMaiorIgual.
    def visitExpMaiorIgual(self, ctx:PythonParser.ExpMaiorIgualContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expMenor.
    def visitExpMenor(self, ctx:PythonParser.ExpMenorContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expFuncCall.
    def visitExpFuncCall(self, ctx:PythonParser.ExpFuncCallContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expDiferente.
    def visitExpDiferente(self, ctx:PythonParser.ExpDiferenteContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expMaior.
    def visitExpMaior(self, ctx:PythonParser.ExpMaiorContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expDivisao.
    def visitExpDivisao(self, ctx:PythonParser.ExpDivisaoContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expDicionario.
    def visitExpDicionario(self, ctx:PythonParser.ExpDicionarioContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expId.
    def visitExpId(self, ctx:PythonParser.ExpIdContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expDivisaoInteira.
    def visitExpDivisaoInteira(self, ctx:PythonParser.ExpDivisaoInteiraContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expOu.
    def visitExpOu(self, ctx:PythonParser.ExpOuContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expLista.
    def visitExpLista(self, ctx:PythonParser.ExpListaContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expE.
    def visitExpE(self, ctx:PythonParser.ExpEContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expMenorIgual.
    def visitExpMenorIgual(self, ctx:PythonParser.ExpMenorIgualContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expNegacao.
    def visitExpNegacao(self, ctx:PythonParser.ExpNegacaoContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expSet.
    def visitExpSet(self, ctx:PythonParser.ExpSetContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expIgual.
    def visitExpIgual(self, ctx:PythonParser.ExpIgualContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expFalso.
    def visitExpFalso(self, ctx:PythonParser.ExpFalsoContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expSubtracao.
    def visitExpSubtracao(self, ctx:PythonParser.ExpSubtracaoContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expVerdadeiro.
    def visitExpVerdadeiro(self, ctx:PythonParser.ExpVerdadeiroContext):
        print(("Here", ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

del (PythonParser, PythonParserVisitor)
