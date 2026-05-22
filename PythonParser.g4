parser grammar PythonParser;

options { tokenVocab=PythonLexer; }

// ─── REGRA PRINCIPAL ───
code: linha* EOF;

// ─── LINHA ───
linha: stat;

// ─── INSTRUÇÃO ───
stat: expr NEWLINE;

// ─── EXPRESSÕES ───
expr
    : expr POW      expr    # expPotencia
    | expr FLOORDIV expr    # expDivisaoInteira
    | expr MULT     expr    # expMultiplicacao
    | expr DIV      expr    # expDivisao
    | expr MOD      expr    # expModulo
    | expr PLUS     expr    # expAdicao
    | expr MINUS    expr    # expSubtracao
    | expr EQ       expr    # expIgual
    | expr NEQ      expr    # expDiferente
    | expr LT       expr    # expMenor
    | expr GT       expr    # expMaior
    | expr LEQ      expr    # expMenorIgual
    | expr GEQ      expr    # expMaiorIgual
    | NOT expr              # expNegacao
    | expr AND      expr    # expE
    | expr OR       expr    # expOu
    | LPAREN expr RPAREN    # expParenteses
    | INT_LIT               # expInteiro
    | FLOAT_LIT             # expDecimal
    | TRUE                  # expVerdadeiro
    | FALSE                 # expFalso
    | ID                    # expId
    ;