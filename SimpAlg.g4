grammar SimpAlg;

options {
    language = Python3;
}

@members {
    decls = []
    cmds = []
}

programa: 'var' '{' declaracoes '}' 'program' '{' comandos '}' ;

declaracoes returns [List[str] result]:
    decs=declaracao+ {$result = $decs.result;};
    
declaracao returns [String result]:
    tipo t=tipo vars=lista_de_variaveis ';' { $result = f"{ $t.result } { $vars.result }" };

tipo returns [String result]:
    'int' {$result = "int"}
    | 'float' {$result = "float"};

comandos returns [List[str] result]:
    cmds=comando+ {$result = $cmds.result;};
    
comando returns [String result]:
    atr=atribuicao {$result = $atr.result}
    | s=saida {$result = $s.result}
    | e=entrada {$result = $e.result}
    | c=condicional {$result = $c.result}
    | r=repeticao {$result = $r.result};

atribuicao returns [String result]:
    ID '=' exp=expressao ';' {$result = f"{ $ID.text } = { $exp.result }"};

saida returns [String result]:
    'print' '(' vals=lista_de_valores ')' ';' {$result = f"print({ $vals.result })"};

entrada returns [String result]:
    'scan' '(' vars=lista_de_variaveis ')' ';' {$result = f"scan({ $vars.result })"};

condicional returns [String result]:
    'if' '(' exp=expressao_logica ')' '{' cmds=comandos {cond_cmds = $cmds.result} '}' ('else' '{' else_cmds=comandos {else_cmds = $else_cmds.result} '}')?
        {$result = f"if ({ $exp.result }) {{ { $cmds.result } }}" + (f" else {{ { $else_cmds.result } }}" if $else_cmds.result else "")};

repeticao returns [String result]:
    'while' '(' exp=expressao_logica ')' '{' cmds=comandos {loop_cmds.result = $cmds.result} '}'
    {$result = f"while ({ $exp.result }) {{ { $cmds.result } }}"};

expressao returns [String result]:
    t=termo {$result = $t.result}
    | un=op_unario termo {$result = f"{ $un.text }{ $termo.result }"}
    | e=expressao '+' t=termo {$result = f"{ $e.result } + { $t.result }"}
    | e=expressao '-' t=termo {$result = f"{ $e.result } - { $t.result }"};

termo returns [String result]:
    f=fator {$result = $f.result}
    | e=termo '*' f=fator {$result = f"{ $e.result } * { $f.result }"}
    | e=termo '/' f=fator {$result = f"{ $e.result } / { $f.result }"};

fator returns [String result]:
    ID {$result = $ID.text}
    | INT {$result = $INT.text}
    | FLOAT {$result = $FLOAT.text}
    | '(' exp=expressao ')' {$result = f"({ $exp.result })"};

expressao_logica returns [String result]:
    e=expressao {$result = $e.result}
    | '(' exp=expressao_logica ')' {$result = f"({ $exp.result })"};

lista_de_valores returns [String result]:
    first=(ID | INT | FLOAT | STRING) (',' values=(ID | INT | FLOAT | STRING))* 
    {
        vals = [ $first.text ]
        if $values:
            for val in $values:
                vals.append(val.text)
        $result = ", ".join(vals)
    };

lista_de_variaveis returns [String result]:
    first=ID (',' vars=ID)* 
    {
        vars = [ $first.text ]
        if $vars:
            for var in $vars:
                vars.append(var.text)
        $result = ", ".join(vars)
    };

op_unario: '+' | '-';

ID: [a-zA-Z_] [a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' ( ~["\r\n\\] | '\\' [rnt\\"'] )* '"';

Comment: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;
