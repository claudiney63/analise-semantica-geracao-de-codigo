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
def new_temp(self):
    self.cont += 1
    return f"_t{self.cont}"

def new_label(self):
    self.cont += 1
    return f".l{self.cont}"
}

start: var program {print(self.st.print_table())};

var : 'var' '{' declaracoes '}';

program :'program' '{' comandos '}' {
print("\nfrom goto import with_goto")
print("@with_goto")
print("def main(): ")
print($comandos.code)
print("main()")
};

declaracoes: declaracao+;

declaracao: lista_de_declaracao ';';

lista_de_declaracao: t=tipo ID {self.at.create($ID, $t.text)} (',' ID {self.at.create($ID, $t.text)})*;

tipo: 'int' | 'float';

comandos returns [str code]: {$code = "";} comando+ {$code += $comando.code;};

comando returns [str code]: atribuicao | saida {$code = '\t' + $saida.code} | entrada | condicional | repeticao;

// Comandos de atribuiçao
atribuicao: ID {self.at.isDeclared($ID)} '=' expressao ';' {self.at.assign($ID, $expressao.text)} ;

expressao returns [ str val ]: t1=termo {$val = $t1.text} (op=( '+' | '-' ) t2=termo {$val = $t1.text + $op.text + $t2.text})* | op_unario termo;

termo returns [ str val ]: f1=fator {$val = $f1.text} (op=('*'|'/') f2=fator {$val = $f1.text + $op.text + $f2.text})* | (INT | ID) (('%') (INT | ID))*;

fator returns [ str val ]: ID {self.at.isDeclared($ID)} | INT {$val = $INT.text} | FLOAT {$val = $FLOAT.text} | '(' expressao ')';

//fatorInt returns [ int val ]: INT {$val = $INT.int};
//fatorFloat 

// Entrada e saída
saida returns [str code]: 'print' '(' lista_de_valores ')' ';' {$code = 'print(' + $lista_de_valores.code + ')'};

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

lista_de_valores returns [str code]: (ID {self.at.isDeclared($ID); $code = $ID.text } | INT | FLOAT | STRING) (',' (ID {self.at.isDeclared($ID)} | INT | FLOAT | STRING))*;

lista_de_variaveis: ID {self.at.isDeclared($ID)} (',' ID {self.at.isDeclared($ID)})*;

op_unario: '+' | '-';

ID: [a-zA-Z_] [a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' ( ~["\r\n\\] | '\\' [rnt\\"'] )* '"';

Comment: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;