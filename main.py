# crie um codigo que gere uma tabela de simbolos para codigo em python
# a tabela de simbolos deve conter o nome do simbolo, o tipo e o escopo
# o codigo deve ser capaz de identificar variaveis, funcoes e classes
# o codigo deve ser capaz de identificar o escopo de cada simbolo
# o codigo deve ser capaz de identificar o tipo de cada simbolo

# exemplo de codigo
# x = 10

# def funcao():
#     y = 20
#     print(x)

# class Classe:
#     z = 30
#     print(y)

# saida
# x | variavel | global
# y | variavel | funcao
# funcao | funcao | global
# Classe | classe | global
# z | variavel | Classe


import ast

class SymbolTableBuilder(ast.NodeVisitor):
    def __init__(self):
        self.symbols = []

    def visit_FunctionDef(self, node):
        self.symbols.append((node.name, 'função', 'global' if len(self.stack) == 0 else self.stack[-1]))
        self.stack.append(node.name)
        self.generic_visit(node)
        self.stack.pop()

    def visit_ClassDef(self, node):
        self.symbols.append((node.name, 'classe', 'global' if len(self.stack) == 0 else self.stack[-1]))
        self.stack.append(node.name)
        self.generic_visit(node)
        self.stack.pop()

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.symbols.append((target.id, 'variável', 'global' if len(self.stack) == 0 else self.stack[-1]))
        self.generic_visit(node)

def build_symbol_table(code):
    tree = ast.parse(code)
    symbol_builder = SymbolTableBuilder()
    symbol_builder.stack = []
    symbol_builder.visit(tree)
    return symbol_builder.symbols

if __name__ == "__main__":
    code = """
x = 10

def funcao():
    y = 20
    print(x)

class Classe:
    z = 30
    print(y)
"""
    symbols = build_symbol_table(code)
    for symbol in symbols:
        print(f"{symbol[0]} | {symbol[1]} | {symbol[2]}")
