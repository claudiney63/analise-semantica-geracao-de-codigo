grammar SimpAlg;

options {
    language = Python3;
}

@header {
from SemanticAnalyser import *
from CodeGenerator import *
}

@parser :: members {
st = SymbolTable()
at = SemanticAnalyzer(st)
cg = CodeGenerator()
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

comandos returns [str code]: {$code = '\t';} (comando {$code = $code + $comando.code + '\n\t';})+ ;

comando returns [str code]:
    atribuicao {$code = $atribuicao.code}
    | saida {$code = $saida.code}
    | entrada {$code = $entrada.code}
    | condicional {$code = ''}
    | repeticao {$code = ''};

// Comandos de atribuiçao
atribuicao returns [str code]: ID {self.at.isDeclared($ID)} '=' expressao ';' {self.at.assign($ID, $expressao.text)} 
{$code = $expressao.code + "\n\t" + $ID.text + " = " +  $expressao.varivavel} ;

expressao returns [ str val, str code, str varivavel ]:
    t1=termo {$val = $t1.text} {$code = $t1.code} {$varivavel = $t1.varivavel} (op=( '+' | '-' ) t2=termo {$val = $t1.text + $op.text + $t2.text} 
    {$varivavel = self.cg.new_temp()}
    {$code = $code + $t2.code + "\n\t" + $varivavel + " = " +  $t1.varivavel + " " + op + " " + $t2.varivavel}
    )*
    | opU=op_unario termo {$val = $opU.text + $termo.text};

op_unario: '+' | '-';

termo returns [ str val, str code, str varivavel]:
    f1=fator {$val = $f1.text} {$code = ""} {$varivavel = $f1.text} (op=('*'|'/') f2=fator {$val = $f1.text + $op.text + $f2.text})*
    | type1=(INT | ID) {$val = $type1.text} {$code = ""} {$varivavel = $type1.text} (('%') type2=(INT | ID) {$val = $type1.text + " % " + $type2.text})*;

fator returns [ str val, str code, str varivavel]: ID {self.at.isDeclared($ID)} {$code = ""} {$varivavel = $ID.text} | INT {$val = $INT.text} {$code = ""} {$varivavel = $INT.text} | FLOAT {$val = $FLOAT.text} | '(' expressao ')';


// Saída
saida returns [str code]: 'print' '(' lista_de_valores ')' ';' {$code = 'print(' + $lista_de_valores.code + ')'};

lista_de_valores returns [str code]: (ID {self.at.isDeclared($ID); $code = $ID.text } | INT | FLOAT | STRING) (',' (ID {self.at.isDeclared($ID); $code = $code + ', ' + $ID.text} | INT | FLOAT | STRING))*;


// Entrada
entrada returns [str code]: 'scan' '(' lista_de_variaveis ')' ';'{$code = $lista_de_variaveis.code + ' = input("input: ").split()'};

lista_de_variaveis returns [str code]: ID {self.at.isDeclared($ID); $code = $ID.text} (',' ID {self.at.isDeclared($ID); $code = $code + ', ' + $ID.text})*;


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

ID: [a-zA-Z_] [a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' ( ~["\r\n\\] | '\\' [rnt\\"'] )* '"';

Comment: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;