class TabelaSimbolos:
    def __init__(self):
        self.tabela = {}

    def adicionar_simbolo(self, nome, tipo):
        if nome in self.tabela:
            print(f"Erro semântico: O símbolo '{nome}' já foi declarado anteriormente.")
        else:
            self.tabela[nome] = tipo

    def obter_tipo(self, nome):
        if nome in self.tabela:
            return self.tabela[nome]
        else:
            print(f"Erro semântico: O símbolo '{nome}' não foi encontrado na tabela de símbolos.")
            return None

class SimpAlgInterpreter:
    def __init__(self):
        self.tabela_simbolos = TabelaSimbolos()

    def interpreta_programa(self, arvore):
        # Interpretar declarações de variáveis
        declaracoes = arvore[0]
        self.interpreta_declaracoes(declaracoes)

        # Interpretar comandos
        comandos = arvore[1]
        for comando in comandos:
            self.interpreta_comando(comando)

    def interpreta_declaracoes(self, declaracoes):
        for declaracao in declaracoes:
            tipo = declaracao[0]
            variaveis = declaracao[1]
            for variavel in variaveis:
                self.tabela_simbolos.adicionar_simbolo(variavel, tipo)

    def interpreta_comando(self, comando):
        tipo_comando = comando[0]
        if tipo_comando == 'atribuicao':
            self.interpreta_atribuicao(comando[1])
        elif tipo_comando == 'saida':
            self.interpreta_saida(comando[1])
        elif tipo_comando == 'entrada':
            self.interpreta_entrada(comando[1])
        elif tipo_comando == 'condicional':
            self.interpreta_condicional(comando[1])
        elif tipo_comando == 'repeticao':
            self.interpreta_repeticao(comando[1])

    def interpreta_atribuicao(self, atribuicao):
        nome_variavel = atribuicao[0]
        tipo_variavel = self.tabela_simbolos.obter_tipo(nome_variavel)
        if tipo_variavel is not None:
            expressao = atribuicao[1]
            tipo_expressao = self.interpreta_expressao(expressao)
            if tipo_variavel != tipo_expressao:
                print(f"Erro semântico: Atribuição inválida para '{nome_variavel}'. Tipos incompatíveis.")

    def interpreta_saida(self, saida):
        for valor in saida:
            self.interpreta_expressao(valor)

    def interpreta_entrada(self, entrada):
        for variavel in entrada:
            nome_variavel = variavel
            tipo_variavel = self.tabela_simbolos.obter_tipo(nome_variavel)
            if tipo_variavel is None:
                print(f"Erro semântico: Variável '{nome_variavel}' não declarada.")

    def interpreta_condicional(self, condicional):
        expressao_logica = condicional[0]
        comandos_if = condicional[1]
        comandos_else = condicional[2] if len(condicional) > 2 else None
        self.interpreta_expressao_logica(expressao_logica)
        for comando in comandos_if:
            self.interpreta_comando(comando)
        if comandos_else:
            for comando in comandos_else:
                self.interpreta_comando(comando)

    def interpreta_repeticao(self, repeticao):
        expressao_logica = repeticao[0]
        comandos = repeticao[1]
        self.interpreta_expressao_logica(expressao_logica)
        for comando in comandos:
            self.interpreta_comando(comando)

    def interpreta_expressao(self, expressao):
        if isinstance(expressao, str):
            # Se a expressão for uma variável, retornar o tipo da variável da tabela de símbolos
            return self.tabela_simbolos.obter_tipo(expressao)
        elif isinstance(expressao, list):
            # Se a expressão for uma lista (operação), interpretar recursivamente os operandos
            operador = expressao[0]
            if operador in ['+', '-', '*', '/']:
                tipo_operando_esquerdo = self.interpreta_expressao(expressao[1])
                tipo_operando_direito = self.interpreta_expressao(expressao[2])
                # Verificar se os tipos dos operandos são compatíveis (neste exemplo, consideramos que são)
                # Aqui seria o lugar para fazer a verificação real dos tipos e o cálculo da expressão
                return tipo_operando_esquerdo  # Retornar o tipo do resultado da expressão
            # Caso a expressão não seja uma operação válida, retornar None
        return None  # Retornar None se a expressão não for válida

    def interpreta_expressao_logica(self, expressao_logica):
        if isinstance(expressao_logica, str):
            # Se a expressão lógica for uma variável, retornar o tipo da variável da tabela de símbolos
            return self.tabela_simbolos.obter_tipo(expressao_logica)
        elif isinstance(expressao_logica, list):
            # Se a expressão lógica for uma lista (operação), interpretar recursivamente os operandos
            operador = expressao_logica[0]
            if operador in ['and', 'or']:
                tipo_operando_esquerdo = self.interpreta_expressao_logica(expressao_logica[1])
                tipo_operando_direito = self.interpreta_expressao_logica(expressao_logica[2])
                # Verificar se os tipos dos operandos são compatíveis (neste exemplo, consideramos que são)
                # Aqui seria o lugar para fazer a verificação real dos tipos e a avaliação da expressão lógica
                return tipo_operando_esquerdo  # Retornar o tipo do resultado da expressão lógica
            # Caso a expressão lógica não seja uma operação válida, retornar None
        return None  # Retornar None se a expressão lógica não for válida

# Exemplo de código-fonte SimpAlg
codigo_fonte = """
var {
    int x, y;
}
program {
    x = 10;
    y = x + 5;
    print(x, y);
}
"""

# Tokenize (não implementado)
tokens = [
    'var', '{', 'int', 'x', ',', 'y', ';', '}', 'program', '{',
    'x', '=', '10', ';', 'y', '=', 'x', '+', '5', ';',
    'print', '(', 'x', ',', 'y', ')', ';', '}'
]

# Árvore sintática abstrata gerada manualmente
arvore_sintatica = [
    (['int', ['x', 'y']]),
    (['=', 'x', ['10']]),
    (['=', 'y', ['+', 'x', '5']]),
    (['print', ['x', 'y']])
]

interpreter = SimpAlgInterpreter()
interpreter.interpreta_programa(arvore_sintatica)
