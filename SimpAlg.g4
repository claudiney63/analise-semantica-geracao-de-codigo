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
if not self.at.isError(): 
    with open('example.py', 'w') as file:
        file.write("\nfrom goto import with_goto\n")
        print("\nfrom goto import with_goto")
        
        file.write("@with_goto\n")
        print("@with_goto")
        
        file.write("def main():")
        print("def main():", end="")
        
        file.write(($comandos.code).replace("\n\t\n\t", "\n\t") + "\n")
        print(($comandos.code).replace("\n\t\n\t", "\n\t"))
        
        file.write("main()")
        print("main()")
};

declaracoes: declaracao*;

declaracao: lista_de_declaracao ';';

lista_de_declaracao: t=tipo ID {self.at.create($ID, $t.text)} (',' ID {self.at.create($ID, $t.text)})*;

tipo: 'int' | 'float';

comandos returns [str code]: 
    {$code = '';} (comando {$code = $code + '\n\t' + $comando.code;})* ;

comando returns [str code]:
    atribuicao      {$code = $atribuicao.code}
    | saida         {$code = $saida.code}
    | entrada       {$code = $entrada.code}
    | condicional   {$code = $condicional.code}
    | repeticao     {$code = $repeticao.code};

// Comandos de atribuiçao
atribuicao returns [str code]: 
    ID {self.at.isDeclared($ID)} '=' expressao ';' {self.at.assign($ID, $expressao.text)}
        {if not($expressao.code == ""): $expressao.code = $expressao.code + "\n\t"}
        {$code = $expressao.code + $ID.text + " = " +  $expressao.variavel} ;

expressao returns [ str val, str code, str variavel, str variavelAnterior ]:
    t1=termo {$val = $t1.text} {$code = $t1.code} {$variavel = $t1.variavel} (op=( '+' | '-' ) t2=termo {$val = $t1.text + $op.text + $t2.text} 
        {$variavelAnterior = $variavel}
        {$variavel = self.cg.new_temp()}
        {$code = $code + $t2.code + "\n\t" + $variavel + " = " +  $variavelAnterior + " " + $op.text + " " + $t2.variavel}
    )*
    | opU=op_unario termo {$val = $opU.text + $termo.text}
        {$variavelAnterior = $variavel}
        {$variavel = self.cg.new_temp()}
        {$code = $variavel + " = " + $opU.text + $termo.variavel};

op_unario: '+' | '-';

termo returns [ str val, str code, str variavel, str variavelAnterior]:
    f1=fator {$val = $f1.text} {$code = $f1.code} {$variavel = $f1.variavel} (op=('*'|'/') f2=fator {$val = $f1.text + $op.text + $f2.text}
        {$variavelAnterior = $variavel}
        {$variavel = self.cg.new_temp()}
        {$code = $code + $f2.code + "\n\t" + $variavel + " = " +  $variavelAnterior + " " + $op.text + " " + $f2.variavel}
    )*
    | f1=fator {$val = $f1.text} {$code = $f1.code} {$variavel = $f1.variavel} (('%') f2=fator {$val = $f1.text + " % " + $f2.text} 
        {$variavelAnterior = $variavel}
        {$variavel = self.cg.new_temp()}
        {$code = $code + $f2.code + "\n\t" + $variavel + " = " +  $variavelAnterior + " % " + $f2.variavel}
    )*;
// type1=( INT | ID ) {$val = $type1.text} {$code = ""} {$variavel = $type1.text}
// type2=(INT | ID) {$val = $type1.text + " % " + $type2.text}
fator returns [ str val, str code, str variavel]: 
    ID {self.at.isDeclared($ID)} {$code = ""} {$variavel = $ID.text} 
    | INT {$val = $INT.text} {$code = ""} {$variavel = $INT.text} 
    | FLOAT {$val = $FLOAT.text} {$code = ""} {$variavel = $FLOAT.text} 
    | '(' expressao {$code = $expressao.code} {$variavel = $expressao.variavel}')';


// Saída
saida returns [str code]: 'print' '(' lista_de_valores ')' ';' {$code = 'print(' + $lista_de_valores.code + ')'};

lista_de_valores returns [str code]:
    (ID {self.at.isDeclared($ID); $code = $ID.text } | INT | FLOAT | STRING) (',' (ID {self.at.isDeclared($ID); $code = $code + ', ' + $ID.text} | INT | FLOAT | STRING))*;


// Entrada
entrada returns [str code]: 'scan' '(' lista_de_variaveis ')' ';'{$code = $lista_de_variaveis.code + ' = input("input: ").split()'};

lista_de_variaveis returns [str code]: ID {self.at.isDeclared($ID); $code = $ID.text} (',' ID {self.at.isDeclared($ID); $code = $code + ', ' + $ID.text})*;


// Condicional (if)
condicional returns [str code, str labelif, str labelelse]: 
    'if' '(' expressao_logica ')' '{' cif=comandos '}' 
        {$labelif = self.cg.new_label()}
        {$code = $expressao_logica.code + "\n\t"}
        {$code = $code + "if " + $expressao_logica.variavel + " : goto " + $labelif + "\n\t"}
        {$code = $code + "label "+ $labelif + $cif.code }
    ('else' '{' celse=comandos '}'
        {$labelelse = self.cg.new_label()}
        {$code = $expressao_logica.code + "\n\t"}
        {$code = $code + "if " + $expressao_logica.variavel + " : goto " + $labelif}
        {$code = $code + $celse.code + "\n\t"}
        {$code = $code + "goto " + $labelelse + "\n\t"}
        {$code = $code + "label "+ $labelif + $cif.code + "\n\t"}
        {$code = $code + "label " + $labelelse }
    )?;


// Repetição (while)
repeticao returns [str code, str whilelabel, str iflabel, str endlabel]:
    'while' '(' expressao_logica ')' '{' comandos '}'
        {$whilelabel = self.cg.new_label()}
        {$iflabel = self.cg.new_label()}
        {$endlabel = self.cg.new_label()}
        {$code = "label " + $whilelabel + "\n\t" }
        {$code = $code + $expressao_logica.code + "\n\t"}
        {$code = $code + "if " + $expressao_logica.variavel + " : goto " + $iflabel + "\n\t"}
        {$code = $code + "goto " + $endlabel + "\n\t"}
        {$code = $code + "label " + $iflabel}
        {$code = $code + $comandos.code + "\n\t"}
        {$code = $code + "goto " + $whilelabel + "\n\t"}
        {$code = $code + "label " + $endlabel};

expressao_logica returns [str code, str variavel]: '(' expressao_logica ')' {$code = $expressao_logica.code} {$variavel = $expressao_logica.variavel} 
    | or_expr {$code = $or_expr.code} {$variavel = $or_expr.variavel};

or_expr returns [str code, str variavel]: 
    e1=and_expr {$variavel = $and_expr.variavel} {$code = $and_expr.code} 
    ('or' e2=and_expr
        {$variavel = self.cg.new_temp()} {$code = $e1.code + "\n\t" + $e2.code + "\n\t" + $variavel + " = " + $e1.variavel + " or " + $e2.variavel}
    )?
    | e3=or_expr 'or' e4=or_expr
        {$variavel = self.cg.new_temp()} {$code = $e3.code + "\n\t" + $e4.code + "\n\t" + $variavel + " = " + $e3.variavel + " or " + $e4.variavel};

and_expr returns [str code, str variavel]: 
    r1=relacional {$variavel = $r1.variavel} {$code = $r1.code} 
    ('and' r2=relacional 
        {$variavel = self.cg.new_temp()} {$code = $r1.code + "\n\t" + $r2.code + "\n\t" + $variavel + " = " + $r1.variavel + " and " + $r2.variavel}
    )? 
    | e1=and_expr 'and' e2=and_expr
        {$variavel = self.cg.new_temp()} {$code = $e1.code + "\n\t" + $e2.code + "\n\t" + $variavel + " = " + $e1.variavel + " and " + $e2.variavel};

relacional returns [str code, str variavel]:
    '!' relacional 
        {$variavel = self.cg.new_temp()}
        {$code = $relacional.code + "\n\t" + $variavel + " = not " + $relacional.variavel}
    | '(' expressao_logica ')' {$variavel = $expressao_logica.variavel} {$code = $expressao_logica.code}
    | t1=terminal op=('<' | '>' | '<=' | '>=' | '==' | '!=') t2=terminal
        {$variavel = self.cg.new_temp()}
        {$code = $variavel + " = " + $t1.text + " " + $op.text + " " + $t2.text};

terminal: (ID {self.at.isDeclared($ID)} | INT | FLOAT);

ID: [a-zA-Z_] [a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' ( ~["\r\n\\] | '\\' [rnt\\"'] )* '"';

Comment: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;