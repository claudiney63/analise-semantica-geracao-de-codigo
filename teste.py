from antlr4 import *
from SimpAlgLexer import SimpAlgLexer
from SimpAlgParser import SimpAlgParser

class SimpAlgPrintVisitor(ParseTreeVisitor):
    def __init__(self):
        self.indentation = 0

    def visitTerminal(self, node: TerminalNode):
        print("  " * self.indentation + node.symbol.text)

    def visitChildren(self, node: RuleNode):
        self.indentation += 1
        result = self.defaultResult()
        n = node.getChildCount()  # Correção aqui
        for i in range(n):
            c = node.getChild(i)
            childResult = c.accept(self)
            result = self.aggregateResult(result, childResult)
        self.indentation -= 1
        return result

    def defaultResult(self):
        return None

    def aggregateResult(self, aggregate, nextResult):
        return nextResult if nextResult is not None else aggregate

def main():
    input_str = "var { int x } program { x = 10; y = 3.14; print(x, y); }"
    input_stream = InputStream(input_str)
    lexer = SimpAlgLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SimpAlgParser(token_stream)
    tree = parser.programa()

    # Imprime a árvore sintática
    print("Árvore Sintática:")
    print(tree.toStringTree(recog=parser))

    # Use o visitor personalizado para imprimir a árvore de forma mais legível
    print("\nÁrvore Sintática (formatada):")
    visitor = SimpAlgPrintVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()
