# analise-semantica-geracao-de-codigo
Implementação da TDS para realização do restante do processo de compilação (Análise Semântica e Geração de Código).  Segundo trabalho da disciplina de compiladores.

# Como instalar

Com o ANTLR4 devidamente instalado (ver README.md do repositório sobre a primeira parte do trabalho), é necessário instalar a biblioteca do ANTLR4 para python através do comando `pip install antlr4-python3-runtime`

# Como rodar

Para usar o ANTLR4 para gerar o analisador léxico e sintático a partir da gramática `SimpAlg.g4`, é necessário rodar o seguinte comando no terminal:

~~~ bash
antlr4 -visitor -o output_dir SimpAlg.g4
~~~
Esse comando vai criar um pasta chamada `output_dir` e vai gerar o analisador léxico e sintático nessa pasta. Não é necessário informar a linguagem porque na gramatica ja tem essa opção habilitada (Python)

Depois disso, para rodar o analisador semântico, basta executar o seguinte comando:

~~~ bash
python SimpAlg.py
~~~