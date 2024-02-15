grammar Hello;

@header {
    import java.util.*;
}

@parser :: members {
    Map<String, Integer> tabela = new HashMap<String, Integer>();
//    ArrayList<String> code = new ArrayList<String>();
    int cont = 0;
    String newTemp() {
        cont++;
        return "_t" + Integer.toString(cont);
    }
    String newLabel() {
        cont++;
        return ".l" + Integer.toString(cont);
    }
}

// Sintaticas (letras minusculas)

prog : decl* cmds {
        System.out.println("\nfrom goto import with_goto");
        System.out.println("@with_goto");
        System.out.println("def main(): ");
        System.out.println($cmds.code);
        System.out.println("main()");
    } ;

decl : 'real' Id ';' {
        if (!tabela.containsKey($Id.text)) tabela.put($Id.text, 2);
        else System.out.println("erro: var já declarada");
    }
    | 'int' Id ';' {
        if (!tabela.containsKey($Id.text)) tabela.put($Id.text, 1);
        else System.out.println("erro: var já declarada");
    }
    ;

cmds returns [String code] : {$code = "";} (cmd {
        $code += $cmd.code;
    } )* ;

// ERRO --> $code += ...
cmd returns [String code] : Id '=' exp ';' {
        $code = $exp.code + "\n\t" + $Id.text + " = " +  $exp.var;
    }
    
    'if' Bool '{' a=cmds '}' 'else' '{' b=cmds '}' {
        // codigo da exp bool
        String tmp = newTemp();
        String lfalse = newLabel();
        String lend = newLabel();
        $code = "\n\t" + tmp + " = " + $Bool.text;
        $code += "\n\tif " + tmp + " == false: goto " + lfalse;
        $code += $a.code + "\n\tgoto " + lend;
        $code += "\n\tlabel " + lfalse + $b.code + "\n\tlabel " + lend;
    }
    ;

exp returns [String code, String var]:
    a=exp '*' b=exp {
        $var = newTemp();
        $code = $a.code + $b.code + "\n\t" + $var + " = " +  $a.var + " * " + $b.var;
    }
    | a=exp '+' b=exp {
        $var = newTemp();
        $code = $a.code + $b.code + "\n\t" + $var + " = " +  $a.var + " + " + $b.var;
    }
    | '(' a=exp ')' {
        $code = $a.code;
        $var = $a.var;
    }
    | Num {
        $code = "";
        $var = $Num.text;
    }
    | NumReal {
        $code = "";
        $var = $NumReal.text;
    }
    | Id {
        $code = "";
        $var = $Id.text;
    }
    ;

// Léxicas (começo com caixa alta)
Bool : 'true' | 'false';
fragment Letra:[A-Za-z];
fragment Digito: '0'..'9';
Id : Letra(Letra|Digito)* ;
Cadeia : '"' ( ('\\'('"'|'t'|'n')) | ~('\\' | '\n') )*? '"' ;
Num : [0-9]+;
NumReal : [0-9]+'.'[0-9]+;
Comment : '/*' .*? '*/' -> skip;
WS : (' ' | '\n') -> skip;


