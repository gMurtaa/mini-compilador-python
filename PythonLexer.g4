lexer grammar PythonLexer;

// Tokens virtuais para controlo de indentação (gerados por ação customizada)
tokens { INDENT, DEDENT }

// PALAVRAS-CHAVE — Identificadoras de Blocos
IF          : 'if' ;
ELIF        : 'elif' ;
ELSE        : 'else' ;
FOR         : 'for' ;
WHILE       : 'while' ;
DEF         : 'def' ;
CLASS       : 'class' ;
TRY         : 'try' ;
EXCEPT      : 'except' ;
FINALLY     : 'finally' ;
WITH        : 'with' ;
MATCH       : 'match' ;
CASE        : 'case' ;

// PALAVRAS-CHAVE — Tipos de Dados
NONE        : 'None' ;
TRUE        : 'True' ;
FALSE       : 'False' ;
INT_TYPE    : 'int' ;
FLOAT_TYPE  : 'float' ;
STR_TYPE    : 'str' ;
BOOL_TYPE   : 'bool' ;
LIST_TYPE   : 'list' ;
DICT_TYPE   : 'dict' ;
TUPLE_TYPE  : 'tuple' ;
SET_TYPE    : 'set' ;

// PALAVRAS-CHAVE — Funções Built-in
// int, float, str, list, dict partilham token com os tipos; distinção feita no Parser
PRINT       : 'print' ;
INPUT       : 'input' ;
LEN         : 'len' ;
RANGE       : 'range' ;
TYPE_FUNC   : 'type' ;
ABS         : 'abs' ;
MAX         : 'max' ;
MIN         : 'min' ;
SUM         : 'sum' ;
SORTED      : 'sorted' ;
OPEN        : 'open' ;

// PALAVRAS-CHAVE — Operadores Booleanos (palavras)
AND         : 'and' ;
OR          : 'or' ;
NOT         : 'not' ;
IS          : 'is' ;
IN          : 'in' ;

// PALAVRAS-CHAVE — Demais
IMPORT      : 'import' ;
FROM        : 'from' ;
AS          : 'as' ;
RETURN      : 'return' ;
PASS        : 'pass' ;
BREAK       : 'break' ;
CONTINUE    : 'continue' ;
GLOBAL      : 'global' ;
NONLOCAL    : 'nonlocal' ;
DEL         : 'del' ;
RAISE       : 'raise' ;
ASSERT      : 'assert' ;
YIELD       : 'yield' ;
LAMBDA      : 'lambda' ;
ASYNC       : 'async' ;
AWAIT       : 'await' ;

// LITERAIS
// FLOAT_LIT antes de INT_LIT — evita que "3.14" seja lido como INT + DOT + INT
FLOAT_LIT   : [0-9]+ '.' [0-9]*
            | '.' [0-9]+
            ;

INT_LIT     : [0-9]+ ;

STRING_LIT  : '"'  (~["\\\r\n])* '"'
            | '\'' (~['\\\r\n])* '\''
            ;

// SÍMBOLOS DE ATRIBUIÇÃO
POW_EQ      : '**=' ;
FLOORDIV_EQ : '//=' ;
PLUS_EQ     : '+=' ;
MINUS_EQ    : '-=' ;
MULT_EQ     : '*=' ;
DIV_EQ      : '/=' ;
MOD_EQ      : '%=' ;
ASSIGN      : '=' ;

// OPERADORES ARITMÉTICOS
POW         : '**' ;
FLOORDIV    : '//' ;
PLUS        : '+' ;
MINUS       : '-' ;
MULT        : '*' ;
DIV         : '/' ;
MOD         : '%' ;

// OPERADORES RELACIONAIS
EQ          : '==' ;
NEQ         : '!=' ;
LEQ         : '<=' ;
GEQ         : '>=' ;
LT          : '<' ;
GT          : '>' ;

// OPERADORES BIT A BIT
LSHIFT      : '<<' ;
RSHIFT      : '>>' ;
BITAND      : '&' ;
BITOR       : '|' ;
BITXOR      : '^' ;
BITNOT      : '~' ;

// SÍMBOLOS ESTRUTURAIS
LPAREN      : '(' ;
RPAREN      : ')' ;
LBRACKET    : '[' ;
RBRACKET    : ']' ;
LBRACE      : '{' ;
RBRACE      : '}' ;
COLON       : ':' ;
COMMA       : ',' ;
DOT         : '.' ;
SEMICOLON   : ';' ;

// NOVA LINHA E COMENTÁRIOS
NEWLINE     : '\r'? '\n' ;
COMMENT     : '#' ~[\r\n]* -> skip ;

// IDENTIFICADORES E ESPAÇOS EM BRANCO
ID          : LETTER (LETTER | DIGIT)* ;
fragment LETTER : [a-zA-Z_] ;
fragment DIGIT  : [0-9] ;
WS          : [ \t]+ -> skip ;
