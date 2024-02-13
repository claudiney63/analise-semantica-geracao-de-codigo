// Generated from C:/Users/Ellem/Documents/GitHub/analise-semantica-geracao-de-codigo/SimpAlg.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link SimpAlgParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface SimpAlgVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#programa}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrograma(SimpAlgParser.ProgramaContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#declaracoes}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaracoes(SimpAlgParser.DeclaracoesContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#declaracao}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaracao(SimpAlgParser.DeclaracaoContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#tipo}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTipo(SimpAlgParser.TipoContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#comandos}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComandos(SimpAlgParser.ComandosContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#comando}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComando(SimpAlgParser.ComandoContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#atribuicao}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtribuicao(SimpAlgParser.AtribuicaoContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#saida}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSaida(SimpAlgParser.SaidaContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#entrada}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEntrada(SimpAlgParser.EntradaContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#condicional}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCondicional(SimpAlgParser.CondicionalContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#repeticao}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRepeticao(SimpAlgParser.RepeticaoContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#expressao}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressao(SimpAlgParser.ExpressaoContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#termo}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTermo(SimpAlgParser.TermoContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#fator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFator(SimpAlgParser.FatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#expressao_logica}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressao_logica(SimpAlgParser.Expressao_logicaContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#or_expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOr_expr(SimpAlgParser.Or_exprContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#and_expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAnd_expr(SimpAlgParser.And_exprContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#relacional}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRelacional(SimpAlgParser.RelacionalContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#lista_de_valores}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLista_de_valores(SimpAlgParser.Lista_de_valoresContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#lista_de_variaveis}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLista_de_variaveis(SimpAlgParser.Lista_de_variaveisContext ctx);
	/**
	 * Visit a parse tree produced by {@link SimpAlgParser#op_unario}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOp_unario(SimpAlgParser.Op_unarioContext ctx);
}