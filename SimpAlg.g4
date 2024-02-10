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

expressao: termo (( '+' | '-' ) termo)*;

termo: fator (( '*' | '/' ) fator)*;

fator: ID | INT | FLOAT | STRING | '(' expressao ')' | '!' fator;

expressao_logica: '(' expressao_logica ')' | relacional (( 'and' | 'or' ) relacional)*;

relacional: '!' relacional | '(' relacional (('and'| 'or') relacional)? ')' | expressao (('<' | '>' | '<=' | '>=' | '==' | '!=') expressao) ;

lista_de_valores: expressao (',' expressao)*;

lista_de_variaveis: ID (',' ID)*;

ID: [a-zA-Z_] [a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: ('"' ( ~["\r\n\\] | '\\' [rnt\\"'] )* '"' | '“' ( ~["\r\n\\] | '\\' [rnt\\"'] )* '”');

Comment: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;
