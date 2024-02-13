// Generated from C:/Users/Ellem/Documents/GitHub/analise-semantica-geracao-de-codigo/SimpAlg.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link SimpAlgParser}.
 */
public interface SimpAlgListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(SimpAlgParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(SimpAlgParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#declaracoes}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracoes(SimpAlgParser.DeclaracoesContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#declaracoes}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracoes(SimpAlgParser.DeclaracoesContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#declaracao}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracao(SimpAlgParser.DeclaracaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#declaracao}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracao(SimpAlgParser.DeclaracaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#tipo}.
	 * @param ctx the parse tree
	 */
	void enterTipo(SimpAlgParser.TipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#tipo}.
	 * @param ctx the parse tree
	 */
	void exitTipo(SimpAlgParser.TipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#comandos}.
	 * @param ctx the parse tree
	 */
	void enterComandos(SimpAlgParser.ComandosContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#comandos}.
	 * @param ctx the parse tree
	 */
	void exitComandos(SimpAlgParser.ComandosContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#comando}.
	 * @param ctx the parse tree
	 */
	void enterComando(SimpAlgParser.ComandoContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#comando}.
	 * @param ctx the parse tree
	 */
	void exitComando(SimpAlgParser.ComandoContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#atribuicao}.
	 * @param ctx the parse tree
	 */
	void enterAtribuicao(SimpAlgParser.AtribuicaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#atribuicao}.
	 * @param ctx the parse tree
	 */
	void exitAtribuicao(SimpAlgParser.AtribuicaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#saida}.
	 * @param ctx the parse tree
	 */
	void enterSaida(SimpAlgParser.SaidaContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#saida}.
	 * @param ctx the parse tree
	 */
	void exitSaida(SimpAlgParser.SaidaContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#entrada}.
	 * @param ctx the parse tree
	 */
	void enterEntrada(SimpAlgParser.EntradaContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#entrada}.
	 * @param ctx the parse tree
	 */
	void exitEntrada(SimpAlgParser.EntradaContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#condicional}.
	 * @param ctx the parse tree
	 */
	void enterCondicional(SimpAlgParser.CondicionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#condicional}.
	 * @param ctx the parse tree
	 */
	void exitCondicional(SimpAlgParser.CondicionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#repeticao}.
	 * @param ctx the parse tree
	 */
	void enterRepeticao(SimpAlgParser.RepeticaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#repeticao}.
	 * @param ctx the parse tree
	 */
	void exitRepeticao(SimpAlgParser.RepeticaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterExpressao(SimpAlgParser.ExpressaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitExpressao(SimpAlgParser.ExpressaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#termo}.
	 * @param ctx the parse tree
	 */
	void enterTermo(SimpAlgParser.TermoContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#termo}.
	 * @param ctx the parse tree
	 */
	void exitTermo(SimpAlgParser.TermoContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#fator}.
	 * @param ctx the parse tree
	 */
	void enterFator(SimpAlgParser.FatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#fator}.
	 * @param ctx the parse tree
	 */
	void exitFator(SimpAlgParser.FatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#expressao_logica}.
	 * @param ctx the parse tree
	 */
	void enterExpressao_logica(SimpAlgParser.Expressao_logicaContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#expressao_logica}.
	 * @param ctx the parse tree
	 */
	void exitExpressao_logica(SimpAlgParser.Expressao_logicaContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#or_expr}.
	 * @param ctx the parse tree
	 */
	void enterOr_expr(SimpAlgParser.Or_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#or_expr}.
	 * @param ctx the parse tree
	 */
	void exitOr_expr(SimpAlgParser.Or_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#and_expr}.
	 * @param ctx the parse tree
	 */
	void enterAnd_expr(SimpAlgParser.And_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#and_expr}.
	 * @param ctx the parse tree
	 */
	void exitAnd_expr(SimpAlgParser.And_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#relacional}.
	 * @param ctx the parse tree
	 */
	void enterRelacional(SimpAlgParser.RelacionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#relacional}.
	 * @param ctx the parse tree
	 */
	void exitRelacional(SimpAlgParser.RelacionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#lista_de_valores}.
	 * @param ctx the parse tree
	 */
	void enterLista_de_valores(SimpAlgParser.Lista_de_valoresContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#lista_de_valores}.
	 * @param ctx the parse tree
	 */
	void exitLista_de_valores(SimpAlgParser.Lista_de_valoresContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#lista_de_variaveis}.
	 * @param ctx the parse tree
	 */
	void enterLista_de_variaveis(SimpAlgParser.Lista_de_variaveisContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#lista_de_variaveis}.
	 * @param ctx the parse tree
	 */
	void exitLista_de_variaveis(SimpAlgParser.Lista_de_variaveisContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpAlgParser#op_unario}.
	 * @param ctx the parse tree
	 */
	void enterOp_unario(SimpAlgParser.Op_unarioContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpAlgParser#op_unario}.
	 * @param ctx the parse tree
	 */
	void exitOp_unario(SimpAlgParser.Op_unarioContext ctx);
}