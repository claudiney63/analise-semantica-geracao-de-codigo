# Trabalho de compiladores: Analise semântica e geracao de código intermediário
<p align="center">
    <a href="https://github.com/Ellemaamorim"><img src="https://badgen.net/badge/icon/Ellem%20Almeida/pink?icon=github&label" alt="Creator badge" /></a>
    <a href="https://github.com/claudiney63"><img src="https://badgen.net/badge/icon/Claudiney%20Ryan/red?icon=github&label" alt="Creator badge" /></a>
    <a href="https://github.com/viniciusmra"><img src="https://badgen.net/badge/icon/Vinícius%20Alves/blue?icon=github&label" alt="Creator badge" /></a>
</p>

Este repositório contém a implementação de um compilador desenvolvido como trabalho final da disciplina de Compiladores do curso de Ciência da Computação da UFPI (2023.2), com o professor Carlos André.

O compilador foi construído para realizar a análise semântica e a geração de código em uma linguagem simples (SimpAlg) que foi desenvolvida no trabalho anterior. A análise semântica verifica a unicidade das variáveis declaradas, a declaração prévia das variáveis nos comandos e a compatibilidade de tipos, incluindo a não permitir a operação % com números reais e fazer a conversão de inteiro para real, se necessário. O código gerado é em Python e utiliza a biblioteca goto-statement para permitir os desvios de controle utilizando rótulos e goto. Cada instrução gerada corresponde a uma única operação, seguindo os conceitos estudados sobre geração de código em compiladores.

## Índice
[Como instalar](#como-instalar)  
[Como gerar o analisador semântico](#como-gerar-o-analisador-semântico)  
[Como compilar um código](#como-compilar-um-código)  
[Como rodar o código intermediário em python](#como-rodar-o-código-intermediário-em-python)  
[Autores](#autores)

## Como instalar
Com o ANTLR4 devidamente instalado (ver README.md do repositório sobre a primeira parte do trabalho), é necessário instalar a biblioteca do ANTLR4 para python através do comando `pip install antlr4-python3-runtime`

## Como gerar o analisador semântico
Para usar o ANTLR4 para gerar o analisador léxico e sintático a partir da gramática `SimpAlg.g4`, é necessário rodar o seguinte comando no terminal:

~~~ bash
antlr4 -visitor -o output_dir SimpAlg.g4
~~~
Esse comando vai criar um pasta chamada `output_dir` e vai gerar o analisador léxico e sintático nessa pasta. Não é necessário informar a linguagem porque na gramatica ja tem essa opção habilitada (Python)

## Como compilar um código
Para compilar um código fonte da linguagem SimpAlg para Python, basta colocar o código dentro do arquivo `input.txt` e rodar o analisador semântico com o seguinte comando:

~~~ bash
python SimpAlg.py
~~~

O código em python será salvo em `output.py`, caso não haja nenhum erro no código fonte.

## Como rodar o código intermediário em python
Para rodar o código intermediário em python, é necessário instalar a biblioteca Goto-statement com o comando `pip install goto-statement` basta rodar o arquivo `output.py`.

ATENÇÃO, a biblioteca so funciona com versões antigas do python (2.6 a 3.6).

## Autores
<a href="https://github.com/Ellemaamorim"><img src="https://badgen.net/badge/icon/Ellem%20Almeida/pink?icon=github&label" alt="Creator badge" /></a>
<a href="https://github.com/claudiney63"><img src="https://badgen.net/badge/icon/Claudiney%20Ryan/red?icon=github&label" alt="Creator badge" /></a>
<a href="https://github.com/viniciusmra"><img src="https://badgen.net/badge/icon/Vinícius%20Alves/blue?icon=github&label" alt="Creator badge" /></a>
