# Mini Compilador de Python
## Fase 1 — Símbolos e Palavras-chave do Python 3
*Analisador Léxico (Lexer) — Referência de Tokens*

---

## 1. Símbolos

### 1.1 Operadores Aritméticos

| Símbolo | Token (ANTLR) | Descrição |
|---------|---------------|-----------|
| `+` | `PLUS` | Adição |
| `-` | `MINUS` | Subtração |
| `*` | `MULT` | Multiplicação |
| `/` | `DIV` | Divisão |
| `%` | `MOD` | Módulo (resto) |
| `**` | `POW` | Potência |
| `//` | `FLOORDIV` | Divisão inteira |

### 1.2 Operadores Relacionais

| Símbolo | Token (ANTLR) | Descrição |
|---------|---------------|-----------|
| `==` | `EQ` | Igual a |
| `!=` | `NEQ` | Diferente de |
| `<` | `LT` | Menor que |
| `>` | `GT` | Maior que |
| `<=` | `LEQ` | Menor ou igual |
| `>=` | `GEQ` | Maior ou igual |

### 1.3 Operadores Booleanos (Símbolos)

| Símbolo | Token (ANTLR) | Descrição |
|---------|---------------|-----------|
| `&` | `BITAND` | AND bit a bit |
| `\|` | `BITOR` | OR bit a bit |
| `^` | `BITXOR` | XOR bit a bit |
| `~` | `BITNOT` | NOT bit a bit |
| `<<` | `LSHIFT` | Deslocamento esquerda |
| `>>` | `RSHIFT` | Deslocamento direita |

### 1.4 Símbolos de Atribuição

| Símbolo | Token (ANTLR) | Descrição |
|---------|---------------|-----------|
| `=` | `ASSIGN` | Atribuição simples |
| `+=` | `PLUS_EQ` | Atribuição com adição |
| `-=` | `MINUS_EQ` | Atribuição com subtração |
| `*=` | `MULT_EQ` | Atribuição com multiplicação |
| `/=` | `DIV_EQ` | Atribuição com divisão |
| `%=` | `MOD_EQ` | Atribuição com módulo |
| `**=` | `POW_EQ` | Atribuição com potência |
| `//=` | `FLOORDIV_EQ` | Atribuição com divisão inteira |

### 1.5 Símbolos Identificadores de Tipos de Dados

| Símbolo | Token (ANTLR) | Descrição |
|---------|---------------|-----------|
| `"..."` | `STRING_LIT` | String com aspas duplas |
| `'...'` | `STRING_LIT` | String com aspas simples |
| `0-9` | `INT_LIT` | Literal inteiro |
| `0.0` | `FLOAT_LIT` | Literal decimal (ponto flutuante) |
| `True / False` | `BOOL_LIT` | Literal booleano |
| `[...]` | `LBRACKET / RBRACKET` | Lista (list) |
| `{...}` | `LBRACE / RBRACE` | Dicionário / conjunto |
| `(...)` | `LPAREN / RPAREN` | Tuplo / agrupamento |

### 1.6 Símbolo Identificador de Início de Bloco

| Símbolo | Token (ANTLR) | Descrição |
|---------|---------------|-----------|
| `:` | `COLON` | Início de bloco (if, for, def, etc.) |
| `INDENT` | `INDENT` | Indentação (início de bloco) |
| `DEDENT` | `DEDENT` | Desindentação (fim de bloco) |

---

## 2. Palavras-chave

### 2.1 Identificadoras de Blocos

| Palavra-chave | Token (ANTLR) | Uso |
|---------------|---------------|-----|
| `if` | `IF` | Condicional |
| `elif` | `ELIF` | Condicional alternativa |
| `else` | `ELSE` | Bloco alternativo |
| `for` | `FOR` | Ciclo for |
| `while` | `WHILE` | Ciclo while |
| `def` | `DEF` | Definição de função |
| `class` | `CLASS` | Definição de classe |
| `try` | `TRY` | Bloco de tentativa |
| `except` | `EXCEPT` | Bloco de exceção |
| `finally` | `FINALLY` | Bloco final (try) |
| `with` | `WITH` | Gestor de contexto |
| `match` | `MATCH` | Correspondência de padrões (3.10+) |
| `case` | `CASE` | Caso (match) |

### 2.2 Tipos de Dados

| Palavra-chave | Token (ANTLR) | Tipo |
|---------------|---------------|------|
| `int` | `INT_TYPE` | Inteiro |
| `float` | `FLOAT_TYPE` | Decimal |
| `str` | `STR_TYPE` | Cadeia de caracteres |
| `bool` | `BOOL_TYPE` | Booleano |
| `list` | `LIST_TYPE` | Lista |
| `dict` | `DICT_TYPE` | Dicionário |
| `tuple` | `TUPLE_TYPE` | Tuplo |
| `set` | `SET_TYPE` | Conjunto |
| `None` | `NONE` | Valor nulo |
| `True` | `TRUE` | Booleano verdadeiro |
| `False` | `FALSE` | Booleano falso |

### 2.3 Funções Built-in

| Função | Token (ANTLR) | Descrição |
|--------|---------------|-----------|
| `print()` | `PRINT` | Imprimir no ecrã |
| `input()` | `INPUT` | Ler entrada do utilizador |
| `len()` | `LEN` | Comprimento de objeto |
| `range()` | `RANGE` | Gerar sequência numérica |
| `type()` | `TYPE` | Tipo de uma variável |
| `int()` | `INT_FUNC` | Converter para inteiro |
| `float()` | `FLOAT_FUNC` | Converter para decimal |
| `str()` | `STR_FUNC` | Converter para string |
| `list()` | `LIST_FUNC` | Converter para lista |
| `dict()` | `DICT_FUNC` | Converter para dicionário |
| `abs()` | `ABS` | Valor absoluto |
| `max()` | `MAX` | Valor máximo |
| `min()` | `MIN` | Valor mínimo |
| `sum()` | `SUM` | Soma de elementos |
| `sorted()` | `SORTED` | Ordenar elementos |
| `open()` | `OPEN` | Abrir ficheiro |

### 2.4 Operadores Booleanos (Palavras)

| Palavra-chave | Token (ANTLR) | Descrição |
|---------------|---------------|-----------|
| `and` | `AND` | Conjunção lógica |
| `or` | `OR` | Disjunção lógica |
| `not` | `NOT` | Negação lógica |
| `is` | `IS` | Identidade de objetos |
| `is not` | `IS_NOT` | Não identidade |
| `in` | `IN` | Pertença a coleção |
| `not in` | `NOT_IN` | Não pertença |

### 2.5 Demais Palavras-chave

| Palavra-chave | Token (ANTLR) | Descrição |
|---------------|---------------|-----------|
| `import` | `IMPORT` | Importar módulo |
| `from` | `FROM` | Importar de módulo |
| `as` | `AS` | Alias de importação |
| `return` | `RETURN` | Retornar valor de função |
| `pass` | `PASS` | Instrução vazia |
| `break` | `BREAK` | Interromper ciclo |
| `continue` | `CONTINUE` | Continuar próxima iteração |
| `global` | `GLOBAL` | Declarar variável global |
| `nonlocal` | `NONLOCAL` | Declarar variável não-local |
| `del` | `DEL` | Apagar variável ou elemento |
| `raise` | `RAISE` | Lançar exceção |
| `assert` | `ASSERT` | Verificação de condição |
| `yield` | `YIELD` | Gerar valor (generator) |
| `lambda` | `LAMBDA` | Função anónima |
| `async` | `ASYNC` | Função assíncrona |
| `await` | `AWAIT` | Aguardar operação assíncrona |

---

*Mini Compilador de Python — Fase 1 | TAC*
