grammar SimpAlg;

programa: 'var' '{' declaracoes '}' 'program' '{' comandos '}';

declaracoes: declaracao+;

declaracao: tipo lista_de_variaveis ';';

tipo: 'int' | 'float';

comandos: comando+;

comando: atribuicao | saida | entrada | condicional | repeticao;

atribuicao: ID '=' expressao ';';

saida: 'print' '(' lista_de_valores ')' ';';

entrada: 'scan' '(' lista_de_variaveis ')' ';';

condicional: 'if' '(' expressao_logica ')' '{' comandos '}' ('else' '{' comandos '}')?;

repeticao: 'while' '(' expressao_logica ')' '{' comandos '}';

expressao: termo(( '+' | '-' ) termo)* | op_unario termo;

termo: fator (( '*' | '/') fator)* | (INT | ID) (('%') (INT | ID))*;

fator: ID | INT | FLOAT | '(' expressao ')';

expressao_logica: '(' expressao_logica ')' | or_expr;

or_expr: and_expr ('or' and_expr)? | or_expr ('or' or_expr);

and_expr: relacional ('and' relacional)? | and_expr ('and' and_expr);

relacional: '!' relacional | '(' relacional (('and'| 'or') relacional)? ')' | relacional (('<' | '>' | '<=' | '>=' | '==' | '!=') relacional) | (ID | INT | FLOAT);

lista_de_valores: (ID | INT | FLOAT | STRING) (',' (ID | INT | FLOAT | STRING))*;

lista_de_variaveis: ID (',' ID)*;

op_unario: '+' | '-';

ID: [a-zA-Z_] [a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' ( ~["\r\n\\] | '\\' [rnt\\"'] )* '"';

Comment: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;