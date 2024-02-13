// Generated from c:/Users/claud/GitHub/analise-semantica-geracao-de-codigo/SimpAlg.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class SimpAlgParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, ID=31, INT=32, 
		FLOAT=33, STRING=34, Comment=35, WS=36;
	public static final int
		RULE_programa = 0, RULE_declaracoes = 1, RULE_declaracao = 2, RULE_tipo = 3, 
		RULE_comandos = 4, RULE_comando = 5, RULE_atribuicao = 6, RULE_saida = 7, 
		RULE_entrada = 8, RULE_condicional = 9, RULE_repeticao = 10, RULE_expressao = 11, 
		RULE_termo = 12, RULE_fator = 13, RULE_expressao_logica = 14, RULE_or_expr = 15, 
		RULE_and_expr = 16, RULE_relacional = 17, RULE_lista_de_valores = 18, 
		RULE_lista_de_variaveis = 19, RULE_op_unario = 20;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "declaracoes", "declaracao", "tipo", "comandos", "comando", 
			"atribuicao", "saida", "entrada", "condicional", "repeticao", "expressao", 
			"termo", "fator", "expressao_logica", "or_expr", "and_expr", "relacional", 
			"lista_de_valores", "lista_de_variaveis", "op_unario"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'var'", "'{'", "'}'", "'program'", "';'", "'int'", "'float'", 
			"'='", "'print'", "'('", "')'", "'scan'", "'if'", "'else'", "'while'", 
			"'+'", "'-'", "'*'", "'/'", "'%'", "'or'", "'and'", "'!'", "'<'", "'>'", 
			"'<='", "'>='", "'=='", "'!='", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, "ID", "INT", "FLOAT", "STRING", 
			"Comment", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "SimpAlg.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SimpAlgParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public DeclaracoesContext declaracoes() {
			return getRuleContext(DeclaracoesContext.class,0);
		}
		public ComandosContext comandos() {
			return getRuleContext(ComandosContext.class,0);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			match(T__0);
			setState(43);
			match(T__1);
			setState(44);
			declaracoes();
			setState(45);
			match(T__2);
			setState(46);
			match(T__3);
			setState(47);
			match(T__1);
			setState(48);
			comandos();
			setState(49);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracoesContext extends ParserRuleContext {
		public List<DeclaracaoContext> declaracao() {
			return getRuleContexts(DeclaracaoContext.class);
		}
		public DeclaracaoContext declaracao(int i) {
			return getRuleContext(DeclaracaoContext.class,i);
		}
		public DeclaracoesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracoes; }
	}

	public final DeclaracoesContext declaracoes() throws RecognitionException {
		DeclaracoesContext _localctx = new DeclaracoesContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declaracoes);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(51);
				declaracao();
				}
				}
				setState(54); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__5 || _la==T__6 );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracaoContext extends ParserRuleContext {
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public Lista_de_variaveisContext lista_de_variaveis() {
			return getRuleContext(Lista_de_variaveisContext.class,0);
		}
		public DeclaracaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracao; }
	}

	public final DeclaracaoContext declaracao() throws RecognitionException {
		DeclaracaoContext _localctx = new DeclaracaoContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_declaracao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(56);
			tipo();
			setState(57);
			lista_de_variaveis();
			setState(58);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TipoContext extends ParserRuleContext {
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			_la = _input.LA(1);
			if ( !(_la==T__5 || _la==T__6) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComandosContext extends ParserRuleContext {
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public ComandosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comandos; }
	}

	public final ComandosContext comandos() throws RecognitionException {
		ComandosContext _localctx = new ComandosContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_comandos);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(62);
				comando();
				}
				}
				setState(65); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 2147529216L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComandoContext extends ParserRuleContext {
		public AtribuicaoContext atribuicao() {
			return getRuleContext(AtribuicaoContext.class,0);
		}
		public SaidaContext saida() {
			return getRuleContext(SaidaContext.class,0);
		}
		public EntradaContext entrada() {
			return getRuleContext(EntradaContext.class,0);
		}
		public CondicionalContext condicional() {
			return getRuleContext(CondicionalContext.class,0);
		}
		public RepeticaoContext repeticao() {
			return getRuleContext(RepeticaoContext.class,0);
		}
		public ComandoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando; }
	}

	public final ComandoContext comando() throws RecognitionException {
		ComandoContext _localctx = new ComandoContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_comando);
		try {
			setState(72);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(67);
				atribuicao();
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 2);
				{
				setState(68);
				saida();
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 3);
				{
				setState(69);
				entrada();
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 4);
				{
				setState(70);
				condicional();
				}
				break;
			case T__14:
				enterOuterAlt(_localctx, 5);
				{
				setState(71);
				repeticao();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtribuicaoContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(SimpAlgParser.ID, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public AtribuicaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atribuicao; }
	}

	public final AtribuicaoContext atribuicao() throws RecognitionException {
		AtribuicaoContext _localctx = new AtribuicaoContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_atribuicao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			match(ID);
			setState(75);
			match(T__7);
			setState(76);
			expressao();
			setState(77);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SaidaContext extends ParserRuleContext {
		public Lista_de_valoresContext lista_de_valores() {
			return getRuleContext(Lista_de_valoresContext.class,0);
		}
		public SaidaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_saida; }
	}

	public final SaidaContext saida() throws RecognitionException {
		SaidaContext _localctx = new SaidaContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_saida);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			match(T__8);
			setState(80);
			match(T__9);
			setState(81);
			lista_de_valores();
			setState(82);
			match(T__10);
			setState(83);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EntradaContext extends ParserRuleContext {
		public Lista_de_variaveisContext lista_de_variaveis() {
			return getRuleContext(Lista_de_variaveisContext.class,0);
		}
		public EntradaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entrada; }
	}

	public final EntradaContext entrada() throws RecognitionException {
		EntradaContext _localctx = new EntradaContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_entrada);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			match(T__11);
			setState(86);
			match(T__9);
			setState(87);
			lista_de_variaveis();
			setState(88);
			match(T__10);
			setState(89);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondicionalContext extends ParserRuleContext {
		public Expressao_logicaContext expressao_logica() {
			return getRuleContext(Expressao_logicaContext.class,0);
		}
		public List<ComandosContext> comandos() {
			return getRuleContexts(ComandosContext.class);
		}
		public ComandosContext comandos(int i) {
			return getRuleContext(ComandosContext.class,i);
		}
		public CondicionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicional; }
	}

	public final CondicionalContext condicional() throws RecognitionException {
		CondicionalContext _localctx = new CondicionalContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_condicional);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			match(T__12);
			setState(92);
			match(T__9);
			setState(93);
			expressao_logica();
			setState(94);
			match(T__10);
			setState(95);
			match(T__1);
			setState(96);
			comandos();
			setState(97);
			match(T__2);
			setState(103);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__13) {
				{
				setState(98);
				match(T__13);
				setState(99);
				match(T__1);
				setState(100);
				comandos();
				setState(101);
				match(T__2);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RepeticaoContext extends ParserRuleContext {
		public Expressao_logicaContext expressao_logica() {
			return getRuleContext(Expressao_logicaContext.class,0);
		}
		public ComandosContext comandos() {
			return getRuleContext(ComandosContext.class,0);
		}
		public RepeticaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_repeticao; }
	}

	public final RepeticaoContext repeticao() throws RecognitionException {
		RepeticaoContext _localctx = new RepeticaoContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_repeticao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			match(T__14);
			setState(106);
			match(T__9);
			setState(107);
			expressao_logica();
			setState(108);
			match(T__10);
			setState(109);
			match(T__1);
			setState(110);
			comandos();
			setState(111);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressaoContext extends ParserRuleContext {
		public List<TermoContext> termo() {
			return getRuleContexts(TermoContext.class);
		}
		public TermoContext termo(int i) {
			return getRuleContext(TermoContext.class,i);
		}
		public Op_unarioContext op_unario() {
			return getRuleContext(Op_unarioContext.class,0);
		}
		public ExpressaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressao; }
	}

	public final ExpressaoContext expressao() throws RecognitionException {
		ExpressaoContext _localctx = new ExpressaoContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_expressao);
		int _la;
		try {
			setState(124);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__9:
			case ID:
			case INT:
			case FLOAT:
				enterOuterAlt(_localctx, 1);
				{
				setState(113);
				termo();
				setState(118);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__15 || _la==T__16) {
					{
					{
					setState(114);
					_la = _input.LA(1);
					if ( !(_la==T__15 || _la==T__16) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(115);
					termo();
					}
					}
					setState(120);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case T__15:
			case T__16:
				enterOuterAlt(_localctx, 2);
				{
				setState(121);
				op_unario();
				setState(122);
				termo();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermoContext extends ParserRuleContext {
		public List<FatorContext> fator() {
			return getRuleContexts(FatorContext.class);
		}
		public FatorContext fator(int i) {
			return getRuleContext(FatorContext.class,i);
		}
		public List<TerminalNode> INT() { return getTokens(SimpAlgParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(SimpAlgParser.INT, i);
		}
		public List<TerminalNode> ID() { return getTokens(SimpAlgParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(SimpAlgParser.ID, i);
		}
		public TermoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termo; }
	}

	public final TermoContext termo() throws RecognitionException {
		TermoContext _localctx = new TermoContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_termo);
		int _la;
		try {
			setState(142);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(126);
				fator();
				setState(131);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__17 || _la==T__18) {
					{
					{
					setState(127);
					_la = _input.LA(1);
					if ( !(_la==T__17 || _la==T__18) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(128);
					fator();
					}
					}
					setState(133);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(134);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==INT) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(139);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__19) {
					{
					{
					{
					setState(135);
					match(T__19);
					}
					setState(136);
					_la = _input.LA(1);
					if ( !(_la==ID || _la==INT) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					}
					setState(141);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FatorContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(SimpAlgParser.ID, 0); }
		public TerminalNode INT() { return getToken(SimpAlgParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(SimpAlgParser.FLOAT, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public FatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fator; }
	}

	public final FatorContext fator() throws RecognitionException {
		FatorContext _localctx = new FatorContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_fator);
		try {
			setState(151);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(144);
				match(ID);
				}
				break;
			case INT:
				enterOuterAlt(_localctx, 2);
				{
				setState(145);
				match(INT);
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 3);
				{
				setState(146);
				match(FLOAT);
				}
				break;
			case T__9:
				enterOuterAlt(_localctx, 4);
				{
				setState(147);
				match(T__9);
				setState(148);
				expressao();
				setState(149);
				match(T__10);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expressao_logicaContext extends ParserRuleContext {
		public Expressao_logicaContext expressao_logica() {
			return getRuleContext(Expressao_logicaContext.class,0);
		}
		public Or_exprContext or_expr() {
			return getRuleContext(Or_exprContext.class,0);
		}
		public Expressao_logicaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressao_logica; }
	}

	public final Expressao_logicaContext expressao_logica() throws RecognitionException {
		Expressao_logicaContext _localctx = new Expressao_logicaContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_expressao_logica);
		try {
			setState(158);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(153);
				match(T__9);
				setState(154);
				expressao_logica();
				setState(155);
				match(T__10);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(157);
				or_expr(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Or_exprContext extends ParserRuleContext {
		public List<And_exprContext> and_expr() {
			return getRuleContexts(And_exprContext.class);
		}
		public And_exprContext and_expr(int i) {
			return getRuleContext(And_exprContext.class,i);
		}
		public List<Or_exprContext> or_expr() {
			return getRuleContexts(Or_exprContext.class);
		}
		public Or_exprContext or_expr(int i) {
			return getRuleContext(Or_exprContext.class,i);
		}
		public Or_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_or_expr; }
	}

	public final Or_exprContext or_expr() throws RecognitionException {
		return or_expr(0);
	}

	private Or_exprContext or_expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Or_exprContext _localctx = new Or_exprContext(_ctx, _parentState);
		Or_exprContext _prevctx = _localctx;
		int _startState = 30;
		enterRecursionRule(_localctx, 30, RULE_or_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(161);
			and_expr(0);
			setState(164);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(162);
				match(T__20);
				setState(163);
				and_expr(0);
				}
				break;
			}
			}
			_ctx.stop = _input.LT(-1);
			setState(171);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Or_exprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_or_expr);
					setState(166);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					{
					setState(167);
					match(T__20);
					setState(168);
					or_expr(0);
					}
					}
					} 
				}
				setState(173);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class And_exprContext extends ParserRuleContext {
		public List<RelacionalContext> relacional() {
			return getRuleContexts(RelacionalContext.class);
		}
		public RelacionalContext relacional(int i) {
			return getRuleContext(RelacionalContext.class,i);
		}
		public List<And_exprContext> and_expr() {
			return getRuleContexts(And_exprContext.class);
		}
		public And_exprContext and_expr(int i) {
			return getRuleContext(And_exprContext.class,i);
		}
		public And_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_and_expr; }
	}

	public final And_exprContext and_expr() throws RecognitionException {
		return and_expr(0);
	}

	private And_exprContext and_expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		And_exprContext _localctx = new And_exprContext(_ctx, _parentState);
		And_exprContext _prevctx = _localctx;
		int _startState = 32;
		enterRecursionRule(_localctx, 32, RULE_and_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(175);
			relacional(0);
			setState(178);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				setState(176);
				match(T__21);
				setState(177);
				relacional(0);
				}
				break;
			}
			}
			_ctx.stop = _input.LT(-1);
			setState(185);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new And_exprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_and_expr);
					setState(180);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					{
					setState(181);
					match(T__21);
					setState(182);
					and_expr(0);
					}
					}
					} 
				}
				setState(187);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RelacionalContext extends ParserRuleContext {
		public List<RelacionalContext> relacional() {
			return getRuleContexts(RelacionalContext.class);
		}
		public RelacionalContext relacional(int i) {
			return getRuleContext(RelacionalContext.class,i);
		}
		public TerminalNode ID() { return getToken(SimpAlgParser.ID, 0); }
		public TerminalNode INT() { return getToken(SimpAlgParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(SimpAlgParser.FLOAT, 0); }
		public RelacionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relacional; }
	}

	public final RelacionalContext relacional() throws RecognitionException {
		return relacional(0);
	}

	private RelacionalContext relacional(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		RelacionalContext _localctx = new RelacionalContext(_ctx, _parentState);
		RelacionalContext _prevctx = _localctx;
		int _startState = 34;
		enterRecursionRule(_localctx, 34, RULE_relacional, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(200);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__22:
				{
				setState(189);
				match(T__22);
				setState(190);
				relacional(4);
				}
				break;
			case T__9:
				{
				setState(191);
				match(T__9);
				setState(192);
				relacional(0);
				setState(195);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__20 || _la==T__21) {
					{
					setState(193);
					_la = _input.LA(1);
					if ( !(_la==T__20 || _la==T__21) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(194);
					relacional(0);
					}
				}

				setState(197);
				match(T__10);
				}
				break;
			case ID:
			case INT:
			case FLOAT:
				{
				setState(199);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 15032385536L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(207);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new RelacionalContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_relacional);
					setState(202);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					{
					setState(203);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1056964608L) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(204);
					relacional(0);
					}
					}
					} 
				}
				setState(209);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Lista_de_valoresContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(SimpAlgParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(SimpAlgParser.ID, i);
		}
		public List<TerminalNode> INT() { return getTokens(SimpAlgParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(SimpAlgParser.INT, i);
		}
		public List<TerminalNode> FLOAT() { return getTokens(SimpAlgParser.FLOAT); }
		public TerminalNode FLOAT(int i) {
			return getToken(SimpAlgParser.FLOAT, i);
		}
		public List<TerminalNode> STRING() { return getTokens(SimpAlgParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(SimpAlgParser.STRING, i);
		}
		public Lista_de_valoresContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista_de_valores; }
	}

	public final Lista_de_valoresContext lista_de_valores() throws RecognitionException {
		Lista_de_valoresContext _localctx = new Lista_de_valoresContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_lista_de_valores);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(210);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 32212254720L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(215);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__29) {
				{
				{
				setState(211);
				match(T__29);
				setState(212);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 32212254720L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(217);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Lista_de_variaveisContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(SimpAlgParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(SimpAlgParser.ID, i);
		}
		public Lista_de_variaveisContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista_de_variaveis; }
	}

	public final Lista_de_variaveisContext lista_de_variaveis() throws RecognitionException {
		Lista_de_variaveisContext _localctx = new Lista_de_variaveisContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_lista_de_variaveis);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(218);
			match(ID);
			setState(223);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__29) {
				{
				{
				setState(219);
				match(T__29);
				setState(220);
				match(ID);
				}
				}
				setState(225);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Op_unarioContext extends ParserRuleContext {
		public Op_unarioContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op_unario; }
	}

	public final Op_unarioContext op_unario() throws RecognitionException {
		Op_unarioContext _localctx = new Op_unarioContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_op_unario);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(226);
			_la = _input.LA(1);
			if ( !(_la==T__15 || _la==T__16) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 15:
			return or_expr_sempred((Or_exprContext)_localctx, predIndex);
		case 16:
			return and_expr_sempred((And_exprContext)_localctx, predIndex);
		case 17:
			return relacional_sempred((RelacionalContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean or_expr_sempred(Or_exprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean and_expr_sempred(And_exprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean relacional_sempred(RelacionalContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001$\u00e5\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0004\u00015\b\u0001\u000b\u0001\f\u00016\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0004\u0004@\b\u0004\u000b\u0004\f\u0004A\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005I\b\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003\th\b\t\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0005\u000bu\b\u000b\n\u000b\f\u000bx\t\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b}\b\u000b\u0001\f\u0001"+
		"\f\u0001\f\u0005\f\u0082\b\f\n\f\f\f\u0085\t\f\u0001\f\u0001\f\u0001\f"+
		"\u0005\f\u008a\b\f\n\f\f\f\u008d\t\f\u0003\f\u008f\b\f\u0001\r\u0001\r"+
		"\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u0098\b\r\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u009f\b\u000e"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u00a5\b\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u00aa\b\u000f\n\u000f"+
		"\f\u000f\u00ad\t\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0003\u0010\u00b3\b\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0005\u0010"+
		"\u00b8\b\u0010\n\u0010\f\u0010\u00bb\t\u0010\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00c4"+
		"\b\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00c9\b\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0005\u0011\u00ce\b\u0011\n\u0011"+
		"\f\u0011\u00d1\t\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0005\u0012"+
		"\u00d6\b\u0012\n\u0012\f\u0012\u00d9\t\u0012\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0005\u0013\u00de\b\u0013\n\u0013\f\u0013\u00e1\t\u0013\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0000\u0003\u001e \"\u0015\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \""+
		"$&(\u0000\b\u0001\u0000\u0006\u0007\u0001\u0000\u0010\u0011\u0001\u0000"+
		"\u0012\u0013\u0001\u0000\u001f \u0001\u0000\u0015\u0016\u0001\u0000\u001f"+
		"!\u0001\u0000\u0018\u001d\u0001\u0000\u001f\"\u00e9\u0000*\u0001\u0000"+
		"\u0000\u0000\u00024\u0001\u0000\u0000\u0000\u00048\u0001\u0000\u0000\u0000"+
		"\u0006<\u0001\u0000\u0000\u0000\b?\u0001\u0000\u0000\u0000\nH\u0001\u0000"+
		"\u0000\u0000\fJ\u0001\u0000\u0000\u0000\u000eO\u0001\u0000\u0000\u0000"+
		"\u0010U\u0001\u0000\u0000\u0000\u0012[\u0001\u0000\u0000\u0000\u0014i"+
		"\u0001\u0000\u0000\u0000\u0016|\u0001\u0000\u0000\u0000\u0018\u008e\u0001"+
		"\u0000\u0000\u0000\u001a\u0097\u0001\u0000\u0000\u0000\u001c\u009e\u0001"+
		"\u0000\u0000\u0000\u001e\u00a0\u0001\u0000\u0000\u0000 \u00ae\u0001\u0000"+
		"\u0000\u0000\"\u00c8\u0001\u0000\u0000\u0000$\u00d2\u0001\u0000\u0000"+
		"\u0000&\u00da\u0001\u0000\u0000\u0000(\u00e2\u0001\u0000\u0000\u0000*"+
		"+\u0005\u0001\u0000\u0000+,\u0005\u0002\u0000\u0000,-\u0003\u0002\u0001"+
		"\u0000-.\u0005\u0003\u0000\u0000./\u0005\u0004\u0000\u0000/0\u0005\u0002"+
		"\u0000\u000001\u0003\b\u0004\u000012\u0005\u0003\u0000\u00002\u0001\u0001"+
		"\u0000\u0000\u000035\u0003\u0004\u0002\u000043\u0001\u0000\u0000\u0000"+
		"56\u0001\u0000\u0000\u000064\u0001\u0000\u0000\u000067\u0001\u0000\u0000"+
		"\u00007\u0003\u0001\u0000\u0000\u000089\u0003\u0006\u0003\u00009:\u0003"+
		"&\u0013\u0000:;\u0005\u0005\u0000\u0000;\u0005\u0001\u0000\u0000\u0000"+
		"<=\u0007\u0000\u0000\u0000=\u0007\u0001\u0000\u0000\u0000>@\u0003\n\u0005"+
		"\u0000?>\u0001\u0000\u0000\u0000@A\u0001\u0000\u0000\u0000A?\u0001\u0000"+
		"\u0000\u0000AB\u0001\u0000\u0000\u0000B\t\u0001\u0000\u0000\u0000CI\u0003"+
		"\f\u0006\u0000DI\u0003\u000e\u0007\u0000EI\u0003\u0010\b\u0000FI\u0003"+
		"\u0012\t\u0000GI\u0003\u0014\n\u0000HC\u0001\u0000\u0000\u0000HD\u0001"+
		"\u0000\u0000\u0000HE\u0001\u0000\u0000\u0000HF\u0001\u0000\u0000\u0000"+
		"HG\u0001\u0000\u0000\u0000I\u000b\u0001\u0000\u0000\u0000JK\u0005\u001f"+
		"\u0000\u0000KL\u0005\b\u0000\u0000LM\u0003\u0016\u000b\u0000MN\u0005\u0005"+
		"\u0000\u0000N\r\u0001\u0000\u0000\u0000OP\u0005\t\u0000\u0000PQ\u0005"+
		"\n\u0000\u0000QR\u0003$\u0012\u0000RS\u0005\u000b\u0000\u0000ST\u0005"+
		"\u0005\u0000\u0000T\u000f\u0001\u0000\u0000\u0000UV\u0005\f\u0000\u0000"+
		"VW\u0005\n\u0000\u0000WX\u0003&\u0013\u0000XY\u0005\u000b\u0000\u0000"+
		"YZ\u0005\u0005\u0000\u0000Z\u0011\u0001\u0000\u0000\u0000[\\\u0005\r\u0000"+
		"\u0000\\]\u0005\n\u0000\u0000]^\u0003\u001c\u000e\u0000^_\u0005\u000b"+
		"\u0000\u0000_`\u0005\u0002\u0000\u0000`a\u0003\b\u0004\u0000ag\u0005\u0003"+
		"\u0000\u0000bc\u0005\u000e\u0000\u0000cd\u0005\u0002\u0000\u0000de\u0003"+
		"\b\u0004\u0000ef\u0005\u0003\u0000\u0000fh\u0001\u0000\u0000\u0000gb\u0001"+
		"\u0000\u0000\u0000gh\u0001\u0000\u0000\u0000h\u0013\u0001\u0000\u0000"+
		"\u0000ij\u0005\u000f\u0000\u0000jk\u0005\n\u0000\u0000kl\u0003\u001c\u000e"+
		"\u0000lm\u0005\u000b\u0000\u0000mn\u0005\u0002\u0000\u0000no\u0003\b\u0004"+
		"\u0000op\u0005\u0003\u0000\u0000p\u0015\u0001\u0000\u0000\u0000qv\u0003"+
		"\u0018\f\u0000rs\u0007\u0001\u0000\u0000su\u0003\u0018\f\u0000tr\u0001"+
		"\u0000\u0000\u0000ux\u0001\u0000\u0000\u0000vt\u0001\u0000\u0000\u0000"+
		"vw\u0001\u0000\u0000\u0000w}\u0001\u0000\u0000\u0000xv\u0001\u0000\u0000"+
		"\u0000yz\u0003(\u0014\u0000z{\u0003\u0018\f\u0000{}\u0001\u0000\u0000"+
		"\u0000|q\u0001\u0000\u0000\u0000|y\u0001\u0000\u0000\u0000}\u0017\u0001"+
		"\u0000\u0000\u0000~\u0083\u0003\u001a\r\u0000\u007f\u0080\u0007\u0002"+
		"\u0000\u0000\u0080\u0082\u0003\u001a\r\u0000\u0081\u007f\u0001\u0000\u0000"+
		"\u0000\u0082\u0085\u0001\u0000\u0000\u0000\u0083\u0081\u0001\u0000\u0000"+
		"\u0000\u0083\u0084\u0001\u0000\u0000\u0000\u0084\u008f\u0001\u0000\u0000"+
		"\u0000\u0085\u0083\u0001\u0000\u0000\u0000\u0086\u008b\u0007\u0003\u0000"+
		"\u0000\u0087\u0088\u0005\u0014\u0000\u0000\u0088\u008a\u0007\u0003\u0000"+
		"\u0000\u0089\u0087\u0001\u0000\u0000\u0000\u008a\u008d\u0001\u0000\u0000"+
		"\u0000\u008b\u0089\u0001\u0000\u0000\u0000\u008b\u008c\u0001\u0000\u0000"+
		"\u0000\u008c\u008f\u0001\u0000\u0000\u0000\u008d\u008b\u0001\u0000\u0000"+
		"\u0000\u008e~\u0001\u0000\u0000\u0000\u008e\u0086\u0001\u0000\u0000\u0000"+
		"\u008f\u0019\u0001\u0000\u0000\u0000\u0090\u0098\u0005\u001f\u0000\u0000"+
		"\u0091\u0098\u0005 \u0000\u0000\u0092\u0098\u0005!\u0000\u0000\u0093\u0094"+
		"\u0005\n\u0000\u0000\u0094\u0095\u0003\u0016\u000b\u0000\u0095\u0096\u0005"+
		"\u000b\u0000\u0000\u0096\u0098\u0001\u0000\u0000\u0000\u0097\u0090\u0001"+
		"\u0000\u0000\u0000\u0097\u0091\u0001\u0000\u0000\u0000\u0097\u0092\u0001"+
		"\u0000\u0000\u0000\u0097\u0093\u0001\u0000\u0000\u0000\u0098\u001b\u0001"+
		"\u0000\u0000\u0000\u0099\u009a\u0005\n\u0000\u0000\u009a\u009b\u0003\u001c"+
		"\u000e\u0000\u009b\u009c\u0005\u000b\u0000\u0000\u009c\u009f\u0001\u0000"+
		"\u0000\u0000\u009d\u009f\u0003\u001e\u000f\u0000\u009e\u0099\u0001\u0000"+
		"\u0000\u0000\u009e\u009d\u0001\u0000\u0000\u0000\u009f\u001d\u0001\u0000"+
		"\u0000\u0000\u00a0\u00a1\u0006\u000f\uffff\uffff\u0000\u00a1\u00a4\u0003"+
		" \u0010\u0000\u00a2\u00a3\u0005\u0015\u0000\u0000\u00a3\u00a5\u0003 \u0010"+
		"\u0000\u00a4\u00a2\u0001\u0000\u0000\u0000\u00a4\u00a5\u0001\u0000\u0000"+
		"\u0000\u00a5\u00ab\u0001\u0000\u0000\u0000\u00a6\u00a7\n\u0001\u0000\u0000"+
		"\u00a7\u00a8\u0005\u0015\u0000\u0000\u00a8\u00aa\u0003\u001e\u000f\u0000"+
		"\u00a9\u00a6\u0001\u0000\u0000\u0000\u00aa\u00ad\u0001\u0000\u0000\u0000"+
		"\u00ab\u00a9\u0001\u0000\u0000\u0000\u00ab\u00ac\u0001\u0000\u0000\u0000"+
		"\u00ac\u001f\u0001\u0000\u0000\u0000\u00ad\u00ab\u0001\u0000\u0000\u0000"+
		"\u00ae\u00af\u0006\u0010\uffff\uffff\u0000\u00af\u00b2\u0003\"\u0011\u0000"+
		"\u00b0\u00b1\u0005\u0016\u0000\u0000\u00b1\u00b3\u0003\"\u0011\u0000\u00b2"+
		"\u00b0\u0001\u0000\u0000\u0000\u00b2\u00b3\u0001\u0000\u0000\u0000\u00b3"+
		"\u00b9\u0001\u0000\u0000\u0000\u00b4\u00b5\n\u0001\u0000\u0000\u00b5\u00b6"+
		"\u0005\u0016\u0000\u0000\u00b6\u00b8\u0003 \u0010\u0000\u00b7\u00b4\u0001"+
		"\u0000\u0000\u0000\u00b8\u00bb\u0001\u0000\u0000\u0000\u00b9\u00b7\u0001"+
		"\u0000\u0000\u0000\u00b9\u00ba\u0001\u0000\u0000\u0000\u00ba!\u0001\u0000"+
		"\u0000\u0000\u00bb\u00b9\u0001\u0000\u0000\u0000\u00bc\u00bd\u0006\u0011"+
		"\uffff\uffff\u0000\u00bd\u00be\u0005\u0017\u0000\u0000\u00be\u00c9\u0003"+
		"\"\u0011\u0004\u00bf\u00c0\u0005\n\u0000\u0000\u00c0\u00c3\u0003\"\u0011"+
		"\u0000\u00c1\u00c2\u0007\u0004\u0000\u0000\u00c2\u00c4\u0003\"\u0011\u0000"+
		"\u00c3\u00c1\u0001\u0000\u0000\u0000\u00c3\u00c4\u0001\u0000\u0000\u0000"+
		"\u00c4\u00c5\u0001\u0000\u0000\u0000\u00c5\u00c6\u0005\u000b\u0000\u0000"+
		"\u00c6\u00c9\u0001\u0000\u0000\u0000\u00c7\u00c9\u0007\u0005\u0000\u0000"+
		"\u00c8\u00bc\u0001\u0000\u0000\u0000\u00c8\u00bf\u0001\u0000\u0000\u0000"+
		"\u00c8\u00c7\u0001\u0000\u0000\u0000\u00c9\u00cf\u0001\u0000\u0000\u0000"+
		"\u00ca\u00cb\n\u0002\u0000\u0000\u00cb\u00cc\u0007\u0006\u0000\u0000\u00cc"+
		"\u00ce\u0003\"\u0011\u0000\u00cd\u00ca\u0001\u0000\u0000\u0000\u00ce\u00d1"+
		"\u0001\u0000\u0000\u0000\u00cf\u00cd\u0001\u0000\u0000\u0000\u00cf\u00d0"+
		"\u0001\u0000\u0000\u0000\u00d0#\u0001\u0000\u0000\u0000\u00d1\u00cf\u0001"+
		"\u0000\u0000\u0000\u00d2\u00d7\u0007\u0007\u0000\u0000\u00d3\u00d4\u0005"+
		"\u001e\u0000\u0000\u00d4\u00d6\u0007\u0007\u0000\u0000\u00d5\u00d3\u0001"+
		"\u0000\u0000\u0000\u00d6\u00d9\u0001\u0000\u0000\u0000\u00d7\u00d5\u0001"+
		"\u0000\u0000\u0000\u00d7\u00d8\u0001\u0000\u0000\u0000\u00d8%\u0001\u0000"+
		"\u0000\u0000\u00d9\u00d7\u0001\u0000\u0000\u0000\u00da\u00df\u0005\u001f"+
		"\u0000\u0000\u00db\u00dc\u0005\u001e\u0000\u0000\u00dc\u00de\u0005\u001f"+
		"\u0000\u0000\u00dd\u00db\u0001\u0000\u0000\u0000\u00de\u00e1\u0001\u0000"+
		"\u0000\u0000\u00df\u00dd\u0001\u0000\u0000\u0000\u00df\u00e0\u0001\u0000"+
		"\u0000\u0000\u00e0\'\u0001\u0000\u0000\u0000\u00e1\u00df\u0001\u0000\u0000"+
		"\u0000\u00e2\u00e3\u0007\u0001\u0000\u0000\u00e3)\u0001\u0000\u0000\u0000"+
		"\u00146AHgv|\u0083\u008b\u008e\u0097\u009e\u00a4\u00ab\u00b2\u00b9\u00c3"+
		"\u00c8\u00cf\u00d7\u00df";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}