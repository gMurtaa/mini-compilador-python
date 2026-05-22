parser grammar PythonParser;

options { tokenVocab=PythonLexer; }

// ─── REGRA PRINCIPAL ───
code: stat* EOF;

// ─── INSTRUÇÃO ───
stat: expr '\n';

// ─── EXPRESSÕES ───
expr
    : ID                          # ids
    | numeros                     # numerosExpr
    | operacoesComExpressoes      # operacoesExpr
    | expressoesEntreParenteses   # parentesesExpr
    ;

// ─── NÚMEROS ───
numeros
    : INT_LIT
    | FLOAT_LIT
    ;

// ─── OPERAÇÕES COM EXPRESSÕES ───
operacoesComExpressoes
    : expr PLUS     expr
    | expr MINUS    expr
    | expr MULT     expr
    | expr DIV      expr
    | expr MOD      expr
    | expr POW      expr
    | expr FLOORDIV expr
    | expr EQ       expr
    | expr NEQ      expr
    | expr LT       expr
    | expr GT       expr
    | expr LEQ      expr
    | expr GEQ      expr
    ;

// ─── EXPRESSÕES ENTRE PARÊNTESES ───
expressoesEntreParenteses
    : LPAREN expr RPAREN
    ;
