grammar SimpAlg;

options {
    language = Python3;
}

@header {
from SemanticAnalyser import *
}

@parser :: members {
st = SymbolTable()
at = SemanticAnalyzer(st)
}

start: var program {print(self.st.print_table())};

var : 'var' '{' declaracoes '}';

program :'program' '{' comandos '}' ;

declaracoes: declaracao+;

declaracao: lista_de_declaracao ';';

lista_de_declaracao: t=tipo ID {self.at.create($ID, $t.text)} (',' ID {self.at.create($ID, $t.text)})*;

tipo: 'int' | 'float';

comandos: comando+;

comando: atribuicao | saida | entrada | condicional | repeticao;

// Comandos de atribuiçao
atribuicao: ID {self.at.isDeclared($ID)} '=' expressao ';' {self.at.assign($ID, $expressao.val)} ;

expressao returns [ str val ]: termo {$val = $termo.val} (( '+' | '-' ) termo)* | op_unario termo;

termo returns [ str val ]: fator {$val = $fator.val} (( '*' | '/') fator)* | (INT | ID) (('%') (INT | ID))*;

fator returns [ str val ]: ID {self.at.isDeclared($ID)} | INT {$val = $INT.text} | FLOAT {$val = $FLOAT.text} | '(' expressao ')';

//fatorInt returns [ int val ]: INT {$val = $INT.int};
//fatorFloat 

// Entrada e saída
saida: 'print' '(' lista_de_valores ')' ';';

entrada: 'scan' '(' lista_de_variaveis ')' ';';

condicional: 'if' '(' expressao_logica ')' '{' comandos '}' ('else' '{' comandos '}')?;

repeticao: 'while' '(' expressao_logica ')' '{' comandos '}';

expressao_logica: '(' expressao_logica ')' | or_expr;

or_expr: and_expr ('or' and_expr)? | or_expr ('or' or_expr);

and_expr: relacional ('and' relacional)? | and_expr ('and' and_expr);

relacional:
    '!' relacional
    | '(' relacional (('and'| 'or') relacional)? ')'
    | relacional (('<' | '>' | '<=' | '>=' | '==' | '!=') relacional)
    | (ID {self.at.isDeclared($ID)} | INT | FLOAT);

lista_de_valores: (ID {self.at.isDeclared($ID)} | INT | FLOAT | STRING) (',' (ID {self.at.isDeclared($ID)} | INT | FLOAT | STRING))*;

lista_de_variaveis: ID {self.at.isDeclared($ID)} (',' ID {self.at.isDeclared($ID)})*;

op_unario: '+' | '-';

ID: [a-zA-Z_] [a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' ( ~["\r\n\\] | '\\' [rnt\\"'] )* '"';

Comment: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;