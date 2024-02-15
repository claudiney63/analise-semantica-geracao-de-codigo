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

    def remove(self):
        pass

    def check(self, key):
        return key in self.st
    
    def get_all_values(self):
        return {key: row.r_value for key, row in self.st.items()}

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
            variables = self.symbol_table.get_all_values()  # Obtém um dicionário com os valores de todas as variáveis
            try:
                value = eval(value, variables)  # Fornece o dicionário de variáveis para eval()
            except (NameError, SyntaxError):
                print(f"Erro: Valor '{value}' não é uma expressão válida na linha {terminal.line}")
                return False

            if row.r_type == 'int':
                if not isinstance(value, int):
                    print(f"Erro: Atribuição de valor incorreto para variável do tipo int, na linha {terminal.line}")
                    return False
            elif row.r_type == 'float':
                try:
                    value = float(value)
                except ValueError:
                    print(f"Erro: Atribuição de valor incorreto para variável do tipo float, na linha {terminal.line}")
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
    
    def atribuicao(self, value = None):
        pass
   #e=expressao ';' {self.at.assign($ID, $e.text)};

