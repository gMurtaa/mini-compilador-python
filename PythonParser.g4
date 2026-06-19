parser grammar PythonParser;

options { tokenVocab=PythonLexer; }

// ─── REGRA PRINCIPAL ───
code: (NEWLINE | stat | condicional | func | func_call | loop_while | loop_for)* EOF;

// ─── INSTRUÇÃO ───
stat
    : ID ASSIGN expr NEWLINE      # statAssignment
    | ID augop  expr NEWLINE      # statAugAssignment
    | RETURN expr NEWLINE         # statReturn
    | expr NEWLINE                # statExpr
    ;

// ─── OPERADORES DE ATRIBUIÇÃO COMPOSTA ───
augop
    : PLUS_EQ
    | MINUS_EQ
    | MULT_EQ
    | DIV_EQ
    | FLOORDIV_EQ
    | MOD_EQ
    | POW_EQ
    ;

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

// ─── ESTRUTURAS DE DADOS ───
lista
    : LBRACKET (expr (COMMA expr)*)? RBRACKET
    ;

tupla
    : LPAREN expr COMMA (expr COMMA)* expr? RPAREN
    | LPAREN expr COMMA RPAREN
    ;

set_lit
    : LBRACE expr (COMMA expr)* RBRACE
    ;

par_chave_valor
    : expr COLON expr
    ;

dicionario
    : LBRACE (par_chave_valor (COMMA par_chave_valor)*)? RBRACE
    ;

// ─── EXPRESSÕES (ordem = precedência, primeiro = maior) ───
expr
    : expr POW      expr            # expPotencia
    | MINUS expr                    # expNegativo
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
    | lista                         # expLista
    | tupla                         # expTupla
    | set_lit                       # expSet
    | dicionario                    # expDicionario
    | INT_LIT                       # expInteiro
    | FLOAT_LIT                     # expDecimal
    | STRING                        # expString
    | TRUE                          # expVerdadeiro
    | FALSE                         # expFalso
    | NONE                          # expNone
    | ID                            # expId
    ;
