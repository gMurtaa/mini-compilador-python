if "." in __name__:
    from .PythonParser import PythonParser
    from .PythonParserVisitor import PythonParserVisitor
else:
    from PythonParser import PythonParser
    from PythonParserVisitor import PythonParserVisitor


class ReturnException(Exception):
    def __init__(self, value):
        self.value = value


class Compiler(PythonParserVisitor):

    def __init__(self):
        super(Compiler, self).__init__()
        self.vars = {}
        self.funcs = {}
        return None

    # ─── CODE ───
    def visitCode(self, ctx: PythonParser.CodeContext):
        return self.visitChildren(ctx)

    # ─── STAT: assignment, return, expression ───
    def visitStatAssignment(self, ctx: PythonParser.StatAssignmentContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.vars[name] = value
        return value

    def visitStatReturn(self, ctx: PythonParser.StatReturnContext):
        value = self.visit(ctx.expr())
        raise ReturnException(value)

    def visitStatExpr(self, ctx: PythonParser.StatExprContext):
        return self.visit(ctx.expr())

    # ─── CONDICIONAL ───
    def visitCondicional(self, ctx: PythonParser.CondicionalContext):
        n_elif = len(ctx.ELIF())

        if self.visit(ctx.expr(0)):
            return self.visit(ctx.bloco(0))

        for i in range(n_elif):
            if self.visit(ctx.expr(i + 1)):
                return self.visit(ctx.bloco(i + 1))

        if ctx.ELSE() is not None:
            return self.visit(ctx.bloco(n_elif + 1))

        return None

    # ─── BLOCO ───
    def visitBloco(self, ctx: PythonParser.BlocoContext):
        result = None
        for stat in ctx.stat():
            result = self.visit(stat)
        return result

    # ─── FUNC: guarda o contexto para execução posterior ───
    def visitFunc(self, ctx: PythonParser.FuncContext):
        func_name = ctx.ID().getText()
        self.funcs[func_name] = ctx
        return None

    # ─── PARAMS: devolve lista de nomes ───
    def visitParams(self, ctx: PythonParser.ParamsContext):
        return [ctx.ID(i).getText() for i in range(len(ctx.ID()))]

    # ─── FUNC_CALL (top-level) ───
    def visitFunc_call(self, ctx: PythonParser.Func_callContext):
        func_name = ctx.ID().getText()
        args = self._eval_args(ctx.args()) if ctx.args() else []
        return self._call_function(func_name, args)

    # ─── ARGS ───
    def visitArgs(self, ctx: PythonParser.ArgsContext):
        return [self.visit(expr) for expr in ctx.expr()]

    # ─── LOOP WHILE ───
    def visitLoop_while(self, ctx: PythonParser.Loop_whileContext):
        while self.visit(ctx.expr()):
            self.visit(ctx.bloco())
        return None

    # ─── LOOP FOR ───
    def visitLoop_for(self, ctx: PythonParser.Loop_forContext):
        var_name = ctx.ID().getText()
        iterable = self.visit(ctx.expr())
        for item in iterable:
            self.vars[var_name] = item
            self.visit(ctx.bloco())
        return None

    # ─── ESTRUTURAS DE DADOS ───
    def visitLista(self, ctx: PythonParser.ListaContext):
        return [self.visit(expr) for expr in ctx.expr()]

    def visitTupla(self, ctx: PythonParser.TuplaContext):
        return tuple(self.visit(expr) for expr in ctx.expr())

    def visitSet_lit(self, ctx: PythonParser.Set_litContext):
        return {self.visit(expr) for expr in ctx.expr()}

    def visitPar_chave_valor(self, ctx: PythonParser.Par_chave_valorContext):
        return (self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    def visitDicionario(self, ctx: PythonParser.DicionarioContext):
        result = {}
        for pair in ctx.par_chave_valor():
            k, v = self.visit(pair)
            result[k] = v
        return result

    # ─── EXPRESSÕES: LITERAIS ───
    def visitExpInteiro(self, ctx: PythonParser.ExpInteiroContext):
        return int(ctx.INT_LIT().getText())

    def visitExpDecimal(self, ctx: PythonParser.ExpDecimalContext):
        return float(ctx.FLOAT_LIT().getText())

    def visitExpString(self, ctx: PythonParser.ExpStringContext):
        text = ctx.STRING().getText()
        return text[1:-1]

    def visitExpVerdadeiro(self, ctx: PythonParser.ExpVerdadeiroContext):
        return True

    def visitExpFalso(self, ctx: PythonParser.ExpFalsoContext):
        return False

    def visitExpId(self, ctx: PythonParser.ExpIdContext):
        name = ctx.ID().getText()
        if name in self.vars:
            return self.vars[name]
        raise NameError(f"Variable '{name}' not defined")

    # ─── EXPRESSÕES: PARÊNTESES ───
    def visitExpParenteses(self, ctx: PythonParser.ExpParentesesContext):
        return self.visit(ctx.expr())

    # ─── EXPRESSÕES: ARITMÉTICA ───
    def visitExpAdicao(self, ctx: PythonParser.ExpAdicaoContext):
        return self.visit(ctx.expr(0)) + self.visit(ctx.expr(1))

    def visitExpSubtracao(self, ctx: PythonParser.ExpSubtracaoContext):
        return self.visit(ctx.expr(0)) - self.visit(ctx.expr(1))

    def visitExpMultiplicacao(self, ctx: PythonParser.ExpMultiplicacaoContext):
        return self.visit(ctx.expr(0)) * self.visit(ctx.expr(1))

    def visitExpDivisao(self, ctx: PythonParser.ExpDivisaoContext):
        return self.visit(ctx.expr(0)) / self.visit(ctx.expr(1))

    def visitExpDivisaoInteira(self, ctx: PythonParser.ExpDivisaoInteiraContext):
        return self.visit(ctx.expr(0)) // self.visit(ctx.expr(1))

    def visitExpModulo(self, ctx: PythonParser.ExpModuloContext):
        return self.visit(ctx.expr(0)) % self.visit(ctx.expr(1))

    def visitExpPotencia(self, ctx: PythonParser.ExpPotenciaContext):
        return self.visit(ctx.expr(0)) ** self.visit(ctx.expr(1))

    # ─── EXPRESSÕES: COMPARAÇÃO ───
    def visitExpIgual(self, ctx: PythonParser.ExpIgualContext):
        return self.visit(ctx.expr(0)) == self.visit(ctx.expr(1))

    def visitExpDiferente(self, ctx: PythonParser.ExpDiferenteContext):
        return self.visit(ctx.expr(0)) != self.visit(ctx.expr(1))

    def visitExpMenor(self, ctx: PythonParser.ExpMenorContext):
        return self.visit(ctx.expr(0)) < self.visit(ctx.expr(1))

    def visitExpMaior(self, ctx: PythonParser.ExpMaiorContext):
        return self.visit(ctx.expr(0)) > self.visit(ctx.expr(1))

    def visitExpMenorIgual(self, ctx: PythonParser.ExpMenorIgualContext):
        return self.visit(ctx.expr(0)) <= self.visit(ctx.expr(1))

    def visitExpMaiorIgual(self, ctx: PythonParser.ExpMaiorIgualContext):
        return self.visit(ctx.expr(0)) >= self.visit(ctx.expr(1))

    # ─── EXPRESSÕES: LÓGICAS ───
    def visitExpE(self, ctx: PythonParser.ExpEContext):
        return self.visit(ctx.expr(0)) and self.visit(ctx.expr(1))

    def visitExpOu(self, ctx: PythonParser.ExpOuContext):
        return self.visit(ctx.expr(0)) or self.visit(ctx.expr(1))

    def visitExpNegacao(self, ctx: PythonParser.ExpNegacaoContext):
        return not self.visit(ctx.expr(0))

    # ─── EXPRESSÕES: CHAMADA DE FUNÇÃO ───
    def visitExpFuncCall(self, ctx: PythonParser.ExpFuncCallContext):
        func_name = ctx.ID().getText()
        args = self._eval_args(ctx.args()) if ctx.args() else []
        return self._call_function(func_name, args)

    # ─── EXPRESSÕES: ESTRUTURAS DE DADOS ───
    def visitExpLista(self, ctx: PythonParser.ExpListaContext):
        return self.visit(ctx.lista())

    def visitExpTupla(self, ctx: PythonParser.ExpTuplaContext):
        return self.visit(ctx.tupla())

    def visitExpSet(self, ctx: PythonParser.ExpSetContext):
        return self.visit(ctx.set_lit())

    def visitExpDicionario(self, ctx: PythonParser.ExpDicionarioContext):
        return self.visit(ctx.dicionario())

    # ─── HELPERS ───
    def _eval_args(self, args_ctx):
        if args_ctx is None:
            return []
        return [self.visit(expr) for expr in args_ctx.expr()]

    def _call_function(self, func_name, args):
        if func_name in self.funcs:
            func_ctx = self.funcs[func_name]
            param_names = []
            if func_ctx.params():
                param_names = [func_ctx.params().ID(i).getText()
                               for i in range(len(func_ctx.params().ID()))]

            saved_vars = self.vars.copy()
            for name, val in zip(param_names, args):
                self.vars[name] = val

            try:
                result = self.visit(func_ctx.bloco())
            except ReturnException as r:
                result = r.value
            finally:
                self.vars = saved_vars

            return result

        builtin = (
            __builtins__.get(func_name) if isinstance(__builtins__, dict)
            else getattr(__builtins__, func_name, None)
        )
        if builtin is not None:
            return builtin(*args)
        raise NameError(f"Function '{func_name}' not defined")


del (PythonParser, PythonParserVisitor)
