grammar SimpAlg;

options {
    language = Python3;
}

@members {
    self.decls = [];
    self.cmds = [];
}

programa: 'var' '{' declaracoes '}' 'program' '{' comandos '}' ;

declaracoes returns [list result]:
    decs=declaracao+ {$result = self.decs};

declaracao returns [str result]:
    tipo t=tipo vars_=lista_de_variaveis ';' { $result = f"{t.result} {vars_.result};" };

tipo returns [str result]:
    'int' {$result = "int";}
    | 'float' {$result = "float";};

comandos returns [list result]:
    cmds=comando+ {$result = self.cmds;};

comando returns [str result]:
    atr=atribuicao {$result = atr.result;}
    | s=saida {$result = s.result;}
    | e=entrada {$result = e.result;}
    | c=condicional {$result = c.result;}
    | r=repeticao {$result = r.result;};

atribuicao returns [str result]:
    ID '=' exp=expressao ';' {$result = f"{ID.text} = {exp.result};"};

saida returns [str result]:
    'print' '(' vals=lista_de_valores ')' ';' {$result = f'print({vals.result});';};

entrada returns [str result]:
    'scan' '(' vars=lista_de_variaveis ')' ';' {$result = f'scan({vars.result});';};

condicional returns [str result]:
    'if' '(' exp=expressao_logica ')' '{' cmds=comandos {cond_cmds = cmds.result} '}' ('else' '{' else_cmds=comandos {else_cmds = else_cmds.result} '}')?
        {$result = f"if {exp.result}:\n    {cond_cmds}" + (f"else:\n    {else_cmds}" if else_cmds else "");};

repeticao returns [str result]:
    'while' '(' exp=expressao_logica ')' '{' cmds=comandos {loop_cmds = cmds.result} '}'
    {$result = f"while {exp.result}:\n    {loop_cmds}";};

expressao returns [str result]:
    t=termo {$result = t.result;}
    | un=op_unario termo {$result = f"{un.text}{termo.result}";}
    | e=expressao '+' t=termo {$result = f"{e.result} + {t.result}";}
    | e=expressao '-' t=termo {$result = f"{e.result} - {t.result}";};

termo returns [str result]:
    f=fator {$result = f.result;}
    | e=termo '*' f=fator {$result = f"{e.result} * {f.result}";}
    | e=termo '/' f=fator {$result = f"{e.result} / {f.result}";};

fator returns [str result]:
    ID {$result = ID.text;}
    | INT {$result = INT.text;}
    | FLOAT {$result = FLOAT.text;}
    | '(' exp=expressao ')' {$result = f"({exp.result})";};

expressao_logica returns [str result]:
    e=expressao {$result = e.result;}
    | '(' exp=expressao_logica ')' {$result = f"({exp.result})";};

lista_de_valores returns [str result]:
    first=(ID | INT | FLOAT | STRING) (',' values=(ID | INT | FLOAT | STRING))* 
    {
        vals = [first.text]
        if values:
            for val in values:
                vals.append(val.text)
        $result = ", ".join(vals)
    };

lista_de_variaveis returns [str result]:
    first=ID (',' vars+=ID)* 
    {
        vars_list = [first.text]
        if $vars:
            for var in $vars:
                vars_list.append(var.text)
        $result = ", ".join(vars_list)
    };

op_unario: '+' | '-';

ID: [a-zA-Z_] [a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' ( ~["\r\n\\] | '\\' [rnt\\"'] )* '"';

Comment: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;
