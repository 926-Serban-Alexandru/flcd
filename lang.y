%{
#include <stdio.h>
%}

%token LET INTEGER CHAR INTEGER_ARRAY BOOL STRING_ARRAY READ WRITE IF THEN ELSE WHILE FOR
%token PLUS MINUS TIMES MOD DIVIDE
%token LESS LESS_EQUAL EQUAL NOT_EQUAL GREATER_EQUAL GREATER
%token IDENTIFIER NUMBER STRING_LITERAL

%%

program: statement_list

statement_list: statement
             | statement_list statement

statement: let_declaration
         | assignment
         | read_statement
         | write_statement
         | if_statement
         | while_statement
         | for_statement

let_declaration: LET identifier_list ':' type ';'

identifier_list: identifier
               | identifier_list ',' identifier

type: INTEGER
    | CHAR
    | INTEGER_ARRAY '[' NUMBER ']'
    | BOOL
    | STRING_ARRAY '[' NUMBER ']'

assignment: identifier '=' expression ';'

read_statement: READ '(' identifier ')' ';'

write_statement: WRITE '(' string_literal identifier_list ')' ';'

if_statement: IF condition THEN '{' statement_list '}' ELSE '{' statement_list '}'

while_statement: WHILE condition '{' statement_list '}'

for_statement: FOR '(' assignment ';' condition ';' assignment ')' '{' statement_list '}'

condition: expression
         | expression LESS expression
         | expression LESS_EQUAL expression
         | expression EQUAL expression
         | expression NOT_EQUAL expression
         | expression GREATER_EQUAL expression
         | expression GREATER expression

expression: factor
          | expression PLUS factor
          | expression MINUS factor
          | expression TIMES factor
          | expression MOD factor
          | expression DIVIDE factor

factor: identifier
      | number

string_literal: '"' characters '"'

characters: /* empty */
          | characters letter_or_digit_or_symbol

letter_or_digit_or_symbol: LETTER
                      | DIGIT
                      | '=' | '+' | '-' | '*' | '%' | '/'

identifier: UNDERSCORE LETTER
          | UNDERSCORE LETTER_OR_DIGIT
          | LETTER LETTER_OR_DIGIT

number: NON_ZERO_DIGIT
      | NON_ZERO_DIGIT DIGIT
      | '0'

relational_operator: LESS
                 | LESS_EQUAL
                 | EQUAL
                 | NOT_EQUAL
                 | GREATER_EQUAL
                 | GREATER

LETTER: 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z' | 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
DIGIT: '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
NON_ZERO_DIGIT: '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
UNDERSCORE: '_'
LETTER_OR_DIGIT: LETTER | DIGIT

%%
