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

    def create(self, terminal=None, varType=''):
        if self.symbol_table.check(terminal.text):
            print(f"Erro: Variavel {terminal.text} já declarada!, na linha {terminal.line}")
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
    
    # verificar se a variavel já foi declarada
    def check(self, terminal=None):
        pass

   

