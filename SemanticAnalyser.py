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
    
    def get_type(self, key):
        return self.st[key].r_type

    def print_table(self):
        for key in self.st:
            print(f"Chave: {key} Linha: {self.st[key]}")

class SemanticAnalyzer:
    def __init__(self, st=SymbolTable()):
        self.symbol_table = st
        self.error = False

    # criar variavel
    def create(self, terminal=None, varType=''):
        if self.symbol_table.check(terminal.text):
            print(f"Erro semântico na Linha {terminal.line}: Variável \'{terminal.text}\' já foi declarada.")
            self.setError(True)
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
                self.setError(True)
                return False

            if row.r_type == 'int':
                if not isinstance(value, int):
                    print(f"Erro semântico na Linha {terminal.line}: Atribuição de valor incorreto para variável do tipo int.")
                    self.setError(True)
                    return False
            elif row.r_type == 'float':
                try:
                    value = float(value)
                except ValueError:
                    print(f"Erro semântico na Linha {terminal.line}: Atribuição de valor incorreto para variável do tipo float.")
                    self.setError(True)
                    return False

            row.r_value = value
            self.symbol_table.insert(terminal.text, row)
            
    def isDeclared(self, terminal=None):
        if not self.symbol_table.check(terminal.text):
            print(f"Erro semântico na Linha {terminal.line}: Variável \'{terminal.text}\' não declarada.")
            self.setError(True)
            return False
        return True
    def check(self, terminal=None):
        pass
    
    def atribuicao(self, value = None):
        pass
    
    def setError(self, hasError):
        self.error = hasError

    def isError(self):
        return self.error

