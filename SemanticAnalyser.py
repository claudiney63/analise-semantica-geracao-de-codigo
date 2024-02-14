from dataclasses import dataclass

@dataclass
class Row:
    r_value : None
    r_type : str
    
    def __init__(self):
        pass
    
    def __str__(self):
        return f"{self.r_type}:{self.r_value}"
    
class SymbolTable:
    
    def __init__(self):
        self.st = {}

    def insert(self, key='', row=Row()):
        self.st[key] = row

    def remove():
        pass

    def check(self, key):
        if key in self.st:
            return True
        return False
    
    def print_table(self):
        for key in self.st:
            print(f"Chave: {key} Linha: {self.st[key]}")

class SemanticAnalyzer:
    def __init__(self, st=SymbolTable()):
        self.symbol_table = st

    # criar variavel
    def create(self, terminal=None, varType=''):
        if self.symbol_table.check(terminal.text):
            print(f"Erro! Linha {terminal.line}: Variável \'{terminal.text}\' já foi declarada.")
            return False
        else:
            row = Row()
            row.r_type = varType
            match varType:
                case 'int':
                    row.r_value = int(0)
                case 'float':
                    row.r_value = float(0.0)

            self.symbol_table.insert(terminal.text, row)
    
    # atribuir valor a variavel
    def assign(self, terminal=None, value=None):
        if self.symbol_table.check(terminal.text):
            row = self.symbol_table.st[terminal.text]
            if row.r_type == 'int':
                if not value.isdigit():
                    print(f"Erro: Atribuição de valor incorreto para variavel do tipo int, na linha {terminal.line}")
                    return False
            elif row.r_type == 'float':
                try:
                    float_value = float(value)
                except ValueError:
                    print(f"Erro: Atribuição de valor incorreto para variavel do tipo float, na linha {terminal.line}")
                    return False
                if not '.' in value:
                    print(f"Erro: Atribuição de valor incorreto para variavel do tipo float, na linha {terminal.line}")
                    return False
            row.r_value = value
            self.symbol_table.insert(terminal.text, row)
    
    def operation(self, terminal=None, value1=None, value2=None):
        if type(value1) != type(value2):
            print(f"Erro: Operação entre tipos diferentes, na linha {terminal.line}")
            return False
        else:
            if type(value1) == int:
                return value1 + value2
            else:
                return value1 + value2
            
    def isDeclared(self, terminal=None):
        if not self.symbol_table.check(terminal.text):
            print(f"Erro! Linha {terminal.line}: Variável \'{terminal.text}\' não declarada.")
            return False
        return True
    def check(self, terminal=None):
        pass

   #e=expressao ';' {self.at.assign($ID, $e.text)};

