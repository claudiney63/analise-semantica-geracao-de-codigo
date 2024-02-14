# analise-semantica-geracao-de-codigo
Implementação da TDS para realização do restante do processo de compilação (Análise Semântica e Geração de Código).  Segundo trabalho da disciplina de compiladores.

#
É necessário executar no terminal o seguinte comando: java -jar C:\caminho\para\antlr-4.x-complete.jar -Dlanguage=Python3 -visitor -o output_dir SuaGramatica.g4
Substituindo os diretorios pelo nome correto em seu computador.

# Como rodar
Para criar o analisador léxico

~~~
antlr4 -Dlanguage=Python3 -visitor -o output_dir SimpAlg.g4
~~~

