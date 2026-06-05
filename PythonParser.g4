parser grammar PythonParser;

options { tokenVocab=PythonLexer; }

// ─── REGRA PRINCIPAL ───
code: (stat | condicional | func | func_call | loop_while | loop_for)* EOF;

// ─── INSTRUÇÃO ───
stat: expr NEWLINE;

// ─── CONDICIONAL ───
condicional
    : IF expr COLON NEWLINE bloco
      (ELIF expr COLON NEWLINE bloco)*
      (ELSE COLON NEWLINE bloco)?
    ;

// ─── BLOCO ───
bloco: stat+ ;

// ─── DEFINIÇÃO DE FUNÇÃO ───
func
    : DEF ID LPAREN params? RPAREN COLON NEWLINE bloco
    ;

params
    : ID (COMMA ID)*
    ;

// ─── CHAMADA DE FUNÇÃO (como instrução top-level) ───
func_call
    : ID LPAREN args? RPAREN NEWLINE
    ;

args
    : expr (COMMA expr)*
    ;

// ─── LOOP WHILE ───
loop_while
    : WHILE expr COLON NEWLINE bloco
    ;

// ─── LOOP FOR ───
loop_for
    : FOR ID IN expr COLON NEWLINE bloco
    ;

// ─── EXPRESSÕES ───
expr
    : expr POW      expr            # expPotencia
    | expr FLOORDIV expr            # expDivisaoInteira
    | expr MULT     expr            # expMultiplicacao
    | expr DIV      expr            # expDivisao
    | expr MOD      expr            # expModulo
    | expr PLUS     expr            # expAdicao
    | expr MINUS    expr            # expSubtracao
    | expr EQ       expr            # expIgual
    | expr NEQ      expr            # expDiferente
    | expr LT       expr            # expMenor
    | expr GT       expr            # expMaior
    | expr LEQ      expr            # expMenorIgual
    | expr GEQ      expr            # expMaiorIgual
    | NOT expr                      # expNegacao
    | expr AND      expr            # expE
    | expr OR       expr            # expOu
    | ID LPAREN args? RPAREN        # expFuncCall
    | LPAREN expr RPAREN            # expParenteses
    | INT_LIT                       # expInteiro
    | FLOAT_LIT                     # expDecimal
    | TRUE                          # expVerdadeiro
    | FALSE                         # expFalso
    | ID                            # expId
    ;