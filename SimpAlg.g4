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
hasError = False
}

start: var program;

var : 'var' '{' declaracoes '}';

program :'program' '{' comandos '}' {

if (not self.at.isError()) and (not self.hasError): 
    with open('output.py', 'w') as file:
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

        print("\nO código intermediário foi gerado com sucesso e salvo no arquivo output.py.\n")
else:{print("\nO código intermediário não foi gerado pois o código fonte possui algum erro.\n")}
};

declaracoes: declaracao*;

declaracao: lista_de_declaracao ';';

lista_de_declaracao: t=tipo ID {self.at.create($ID, $t.text)} (',' ID {self.at.create($ID, $t.text)})*;

tipo: 'int' | 'float';

comandos returns [str code]: {if self.hasError: return}
    {$code = '';} (comando {if self.hasError: return} {if not($comando.code == None): $code = $code + '\n\t' + $comando.code;})* ;

comando returns [str code]: {if self.hasError: return}
    atribuicao      {if self.hasError: return}{if $atribuicao.text == None: $code = ""} {if not($atribuicao.text == None): $code = $atribuicao.code}
    | saida         {if self.hasError: return}{$code = $saida.code}
    | entrada       {if self.hasError: return}{$code = $entrada.code}
    | condicional   {if self.hasError: return}{if $condicional.code == None: $code = "ellem"} {if not($condicional.code == None): $code = $condicional.code}
    | repeticao     {if self.hasError: return}{if $repeticao.code == None: $code = ""} {if not($repeticao.code == None): $code = $repeticao.code};

// Comandos de atribuiçao
atribuicao returns [str code]: {if self.hasError: return}
    ID {if not self.at.isDeclared($ID): return} '=' expressao ';' {if self.hasError: return}
        {if(self.st.get_type($ID.text) == 'int' and $expressao.type == 'float'):  print(f"Erro semântico na linha {$ID.line}: Atribuição inválida. Esperado valor do tipo int, mas recebido {$expressao.type}.")}
        {if(self.st.get_type($ID.text) == 'int' and $expressao.type == 'float'): self.at.setError(True)}
        {if not($expressao.code == ""): $expressao.code = $expressao.code + "\n\t"}
        {$code = $expressao.code + $ID.text + " = " +  $expressao.variavel} ;

expressao returns [ int line, str type, str val, str code, str variavel, str variavelAnterior ]: {if self.hasError: return}
    t1=termo {if self.hasError: return} {$val = $t1.text} {$code = $t1.code} {$variavel = $t1.variavel} {$type = $t1.type} {$line = $termo.line} (op=( '+' | '-' ) t2=termo {$val = $t1.text + $op.text + $t2.text} 
        {$type = 'error'}
        {if($t1.type == "int" and $t2.type == "int"): $type = "int"}
        {if($t1.type == "float" or $t2.type == "float"): $type = "float"}
        {$variavelAnterior = $variavel}
        {$variavel = self.cg.new_temp()}
        {$code = $code + $t2.code + "\n\t" + $variavel + " = " +  $variavelAnterior + " " + $op.text + " " + $t2.variavel}
    )*
    | opU=op_unario termo {if self.hasError: return} {$val = $opU.text + $termo.text} {$type = $termo.type} {$line = $termo.line}
        {$variavelAnterior = $variavel}
        {$variavel = self.cg.new_temp()}
        {$code = $variavel + " = " + $opU.text + $termo.variavel};

op_unario: '+' | '-';

termo returns [ int line, str type, str val, str code, str variavel, str variavelAnterior ]: {if self.hasError: return}
    f1=fator {if self.hasError: return} {$val = $f1.text} {$code = $f1.code} {$variavel = $f1.variavel} {$type = $fator.type} {$line = $fator.line} (op=('*'|'/') f2=fator {$val = $f1.text + $op.text + $f2.text}
        {if($f1.type == "int" and $f2.type == "int"): $type = "int"}
        {if($f1.type == "float" or $f2.type == "float"): $type = "float"}
        {$variavelAnterior = $variavel}
        {$variavel = self.cg.new_temp()}
        {$code = $code + $f2.code + "\n\t" + $variavel + " = " +  $variavelAnterior + " " + $op.text + " " + $f2.variavel}
    )*
    | f1=fator {if self.hasError: return} {$val = $f1.text} {$code = $f1.code} {$variavel = $f1.variavel} {$type = 'int'} {$line = $fator.line} (('%') f2=fator {$val = $f1.text + " % " + $f2.text}
        {if($f1.type == "float" or $f2.type == "float"): self.at.setError(True)}
        {if($f1.type == "float" or $f2.type == "float"): print(f"Erro semântico na linha {$f1.line}: Operação de módulo inválida. Ambos os operandos devem ser do tipo int, mas recebido {$f1.type} e {$f2.type}.")}
        {$variavelAnterior = $variavel}
        {$variavel = self.cg.new_temp()}
        {$code = $code + $f2.code + "\n\t" + $variavel + " = " +  $variavelAnterior + " % " + $f2.variavel}
    )*;

fator returns [int line, str type, str val, str code, str variavel]: {if self.hasError: return}
    ID {if not(self.at.isDeclared($ID)): $type = 'error'} {if not($type == 'error'): $type = self.st.get_type($ID.text)}  {$code = ""} {$variavel = $ID.text} {$line = $ID.line}
    | INT {$val = $INT.text} {$code = ""} {$variavel = $INT.text} {$type = "int"} {$line = $INT.line}
    | FLOAT {$val = $FLOAT.text} {$code = ""} {$variavel = $FLOAT.text} {$type = "float"} {$line = $FLOAT.line}
    | '(' expressao {$code = $expressao.code} {$variavel = $expressao.variavel}')'{$type = $expressao.type} {$line = $expressao.line}; 


// Saída
saida returns [str code]: {if self.hasError: return}
    'print' '(' lista_de_valores ')' ';' {if self.hasError: return} {$code = 'print(' + $lista_de_valores.code + ')'};

lista_de_valores returns [str code]: {if self.hasError: return}
    (ID {self.at.isDeclared($ID); $code = $ID.text} | INT {$code = $INT.text} | FLOAT {$code = $FLOAT.text} | STRING {$code = $STRING.text})
    (',' (ID {self.at.isDeclared($ID); $code = $code + ', ' + $ID.text} | INT {$code = $code + ', ' +  $INT.text} | FLOAT {$code = $code + ', ' +  $FLOAT.text} | STRING {$code = $code + ', ' +  $STRING.text}))*;


// Entrada
entrada returns [str code]: {if self.hasError: return}
    'scan' '(' lista_de_variaveis ')' ';'{if self.hasError: return} {$code = $lista_de_variaveis.code};

lista_de_variaveis returns [str code]: {if self.hasError: return}
    ID {self.at.isDeclared($ID); $code = $ID.text}
        {if(self.at.isDeclared($ID)): $code = $ID.text + " = " + self.st.get_type($ID.text) + "(input('input " + $ID.text + ":' ))"}
    (',' ID 
        {if(self.at.isDeclared($ID)): $code = $code + "\n\t" + $ID.text + " = " + self.st.get_type($ID.text) + "(input('input " + $ID.text + ":' ))"}    
    )*;

// Condicional (if)
condicional returns [str code, str labelif, str labelelse, str labelend]: {if self.hasError: return}
    'if' '(' expressao_logica ')' '{' cif=comandos '}' 
        {if self.hasError: return}
        {$labelif = self.cg.new_label()}
        {$labelend = self.cg.new_label()}
        {if not $expressao_logica.code: $expressao_logica.code = ""}
        {if not $expressao_logica.variavel: $expressao_logica.variavel = ""}
        {$code = $expressao_logica.code + "\n\t"}
        {$code = $code + "if " + $expressao_logica.variavel + " : goto " + $labelif + "\n\t"}
        {$code = $code + "goto " + $labelend + "\n\t"}
        {$code = $code + "label "+ $labelif + $cif.code }

    ('else' '{' celse=comandos '}'
        {if self.hasError: return}
        {$labelelse = self.cg.new_label()}
        {$code = $expressao_logica.code + "\n\t"}
        {$code = $code + "if " + $expressao_logica.variavel + " : goto " + $labelif}
        {$code = $code + $celse.code + "\n\t"}
        {$code = $code + "goto " + $labelelse + "\n\t"}
        {$code = $code + "label "+ $labelif + $cif.code + "\n\t"}
        {$code = $code + "label " + $labelelse }
    )?{$code = $code + "\n\tlabel " + $labelend};


// Repetição (while)
repeticao returns [str code, str whilelabel, str iflabel, str endlabel]: {if self.hasError: return}
    'while' '(' expressao_logica ')' '{' comandos '}'
        {if self.hasError: return}
        {if not $expressao_logica.code: $expressao_logica.code = ""}
        {if not $expressao_logica.variavel: $expressao_logica.variavel = ""}
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

expressao_logica returns [str code, str variavel]: {if self.hasError: return}
    '(' expressao_logica ')' {if self.hasError: return} {$code = $expressao_logica.code} {$variavel = $expressao_logica.variavel} 
    | or_expr {if self.hasError: return}{$code = $or_expr.code} {$variavel = $or_expr.variavel};

or_expr returns [str code, str variavel]: {if self.hasError: return}
    e1=and_expr {if self.hasError: return}{$variavel = $and_expr.variavel} {$code = $and_expr.code} 
    ('or' e2=and_expr
        {if self.hasError: return}{$variavel = self.cg.new_temp()} {if not(self.hasError): $code = $e1.code + "\n\t" + $e2.code + "\n\t" + $variavel + " = " + $e1.variavel + " or " + $e2.variavel}
    )?
    | e3=or_expr 'or' e4=or_expr
        {if self.hasError: return}{$variavel = self.cg.new_temp()} {if not(self.hasError): $code = $e3.code + "\n\t" + $e4.code + "\n\t" + $variavel + " = " + $e3.variavel + " or " + $e4.variavel};

and_expr returns [str code, str variavel]: {if self.hasError: return}
    r1=relacional {if self.hasError: return}{$variavel = $r1.variavel} {$code = $r1.code} 
    ('and' r2=relacional 
        {if self.hasError: return}{$variavel = self.cg.new_temp()} {if not(self.hasError): $code = $r1.code + "\n\t" + $r2.code + "\n\t" + $variavel + " = " + $r1.variavel + " and " + $r2.variavel}
    )? 
    | e1=and_expr 'and' e2=and_expr
        {if self.hasError: return}{$variavel = self.cg.new_temp()} {if not(self.hasError): $code = $e1.code + "\n\t" + $e2.code + "\n\t" + $variavel + " = " + $e1.variavel + " and " + $e2.variavel};

relacional returns [str code, str variavel]: {if self.hasError: return}
    '!' relacional
        {if self.hasError: return}
        {$variavel = self.cg.new_temp()}
        {if not(self.hasError): $code = $relacional.code + "\n\t" + $variavel + " = not " + $relacional.variavel}
    | '(' expressao_logica ')' {if self.hasError: return}{$variavel = $expressao_logica.variavel} {$code = $expressao_logica.code}
    | t1=terminal op=('<' | '>' | '<=' | '>=' | '==' | '!=') t2=terminal {if self.hasError: return}
        {$variavel = self.cg.new_temp()}
        {if not(self.hasError): $code = $variavel + " = " + $t1.text + " " + $op.text + " " + $t2.text};

terminal: {if self.hasError: return} 
    (ID {self.at.isDeclared($ID)} | INT | FLOAT);

ID: [a-zA-Z_] [a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' ( ~["\r\n\\] | '\\' [rnt\\"'] )* '"';

Comment: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;