// Generated from c:/Users/vinic/Documents/GitHub/analise-semantica-geracao-de-codigo/HelloCod.g4 by ANTLR 4.13.1

    import java.util.*;

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class HelloLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, Bool=13, Id=14, Cadeia=15, Num=16, NumReal=17, 
		Comment=18, WS=19;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "Bool", "Letra", "Digito", "Id", "Cadeia", 
			"Num", "NumReal", "Comment", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'real'", "';'", "'int'", "'='", "'if'", "'{'", "'}'", "'else'", 
			"'*'", "'+'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "Bool", "Id", "Cadeia", "Num", "NumReal", "Comment", "WS"
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


	public HelloLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "HelloCod.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0013\u0090\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0003\fV\b\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0005\u000f_\b\u000f\n\u000f\f\u000fb\t"+
		"\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0005\u0010h\b"+
		"\u0010\n\u0010\f\u0010k\t\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0004"+
		"\u0011p\b\u0011\u000b\u0011\f\u0011q\u0001\u0012\u0004\u0012u\b\u0012"+
		"\u000b\u0012\f\u0012v\u0001\u0012\u0001\u0012\u0004\u0012{\b\u0012\u000b"+
		"\u0012\f\u0012|\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0005"+
		"\u0013\u0083\b\u0013\n\u0013\f\u0013\u0086\t\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0002i\u0084\u0000\u0015\u0001\u0001\u0003\u0002\u0005\u0003"+
		"\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015"+
		"\u000b\u0017\f\u0019\r\u001b\u0000\u001d\u0000\u001f\u000e!\u000f#\u0010"+
		"%\u0011\'\u0012)\u0013\u0001\u0000\u0005\u0002\u0000AZaz\u0003\u0000\""+
		"\"nntt\u0002\u0000\n\n\\\\\u0001\u000009\u0002\u0000\n\n  \u0096\u0000"+
		"\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000"+
		"\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000"+
		"\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r"+
		"\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011"+
		"\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015"+
		"\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019"+
		"\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001"+
		"\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000"+
		"\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000"+
		"\u0001+\u0001\u0000\u0000\u0000\u00030\u0001\u0000\u0000\u0000\u00052"+
		"\u0001\u0000\u0000\u0000\u00076\u0001\u0000\u0000\u0000\t8\u0001\u0000"+
		"\u0000\u0000\u000b;\u0001\u0000\u0000\u0000\r=\u0001\u0000\u0000\u0000"+
		"\u000f?\u0001\u0000\u0000\u0000\u0011D\u0001\u0000\u0000\u0000\u0013F"+
		"\u0001\u0000\u0000\u0000\u0015H\u0001\u0000\u0000\u0000\u0017J\u0001\u0000"+
		"\u0000\u0000\u0019U\u0001\u0000\u0000\u0000\u001bW\u0001\u0000\u0000\u0000"+
		"\u001dY\u0001\u0000\u0000\u0000\u001f[\u0001\u0000\u0000\u0000!c\u0001"+
		"\u0000\u0000\u0000#o\u0001\u0000\u0000\u0000%t\u0001\u0000\u0000\u0000"+
		"\'~\u0001\u0000\u0000\u0000)\u008c\u0001\u0000\u0000\u0000+,\u0005r\u0000"+
		"\u0000,-\u0005e\u0000\u0000-.\u0005a\u0000\u0000./\u0005l\u0000\u0000"+
		"/\u0002\u0001\u0000\u0000\u000001\u0005;\u0000\u00001\u0004\u0001\u0000"+
		"\u0000\u000023\u0005i\u0000\u000034\u0005n\u0000\u000045\u0005t\u0000"+
		"\u00005\u0006\u0001\u0000\u0000\u000067\u0005=\u0000\u00007\b\u0001\u0000"+
		"\u0000\u000089\u0005i\u0000\u00009:\u0005f\u0000\u0000:\n\u0001\u0000"+
		"\u0000\u0000;<\u0005{\u0000\u0000<\f\u0001\u0000\u0000\u0000=>\u0005}"+
		"\u0000\u0000>\u000e\u0001\u0000\u0000\u0000?@\u0005e\u0000\u0000@A\u0005"+
		"l\u0000\u0000AB\u0005s\u0000\u0000BC\u0005e\u0000\u0000C\u0010\u0001\u0000"+
		"\u0000\u0000DE\u0005*\u0000\u0000E\u0012\u0001\u0000\u0000\u0000FG\u0005"+
		"+\u0000\u0000G\u0014\u0001\u0000\u0000\u0000HI\u0005(\u0000\u0000I\u0016"+
		"\u0001\u0000\u0000\u0000JK\u0005)\u0000\u0000K\u0018\u0001\u0000\u0000"+
		"\u0000LM\u0005t\u0000\u0000MN\u0005r\u0000\u0000NO\u0005u\u0000\u0000"+
		"OV\u0005e\u0000\u0000PQ\u0005f\u0000\u0000QR\u0005a\u0000\u0000RS\u0005"+
		"l\u0000\u0000ST\u0005s\u0000\u0000TV\u0005e\u0000\u0000UL\u0001\u0000"+
		"\u0000\u0000UP\u0001\u0000\u0000\u0000V\u001a\u0001\u0000\u0000\u0000"+
		"WX\u0007\u0000\u0000\u0000X\u001c\u0001\u0000\u0000\u0000YZ\u000209\u0000"+
		"Z\u001e\u0001\u0000\u0000\u0000[`\u0003\u001b\r\u0000\\_\u0003\u001b\r"+
		"\u0000]_\u0003\u001d\u000e\u0000^\\\u0001\u0000\u0000\u0000^]\u0001\u0000"+
		"\u0000\u0000_b\u0001\u0000\u0000\u0000`^\u0001\u0000\u0000\u0000`a\u0001"+
		"\u0000\u0000\u0000a \u0001\u0000\u0000\u0000b`\u0001\u0000\u0000\u0000"+
		"ci\u0005\"\u0000\u0000de\u0005\\\u0000\u0000eh\u0007\u0001\u0000\u0000"+
		"fh\b\u0002\u0000\u0000gd\u0001\u0000\u0000\u0000gf\u0001\u0000\u0000\u0000"+
		"hk\u0001\u0000\u0000\u0000ij\u0001\u0000\u0000\u0000ig\u0001\u0000\u0000"+
		"\u0000jl\u0001\u0000\u0000\u0000ki\u0001\u0000\u0000\u0000lm\u0005\"\u0000"+
		"\u0000m\"\u0001\u0000\u0000\u0000np\u0007\u0003\u0000\u0000on\u0001\u0000"+
		"\u0000\u0000pq\u0001\u0000\u0000\u0000qo\u0001\u0000\u0000\u0000qr\u0001"+
		"\u0000\u0000\u0000r$\u0001\u0000\u0000\u0000su\u0007\u0003\u0000\u0000"+
		"ts\u0001\u0000\u0000\u0000uv\u0001\u0000\u0000\u0000vt\u0001\u0000\u0000"+
		"\u0000vw\u0001\u0000\u0000\u0000wx\u0001\u0000\u0000\u0000xz\u0005.\u0000"+
		"\u0000y{\u0007\u0003\u0000\u0000zy\u0001\u0000\u0000\u0000{|\u0001\u0000"+
		"\u0000\u0000|z\u0001\u0000\u0000\u0000|}\u0001\u0000\u0000\u0000}&\u0001"+
		"\u0000\u0000\u0000~\u007f\u0005/\u0000\u0000\u007f\u0080\u0005*\u0000"+
		"\u0000\u0080\u0084\u0001\u0000\u0000\u0000\u0081\u0083\t\u0000\u0000\u0000"+
		"\u0082\u0081\u0001\u0000\u0000\u0000\u0083\u0086\u0001\u0000\u0000\u0000"+
		"\u0084\u0085\u0001\u0000\u0000\u0000\u0084\u0082\u0001\u0000\u0000\u0000"+
		"\u0085\u0087\u0001\u0000\u0000\u0000\u0086\u0084\u0001\u0000\u0000\u0000"+
		"\u0087\u0088\u0005*\u0000\u0000\u0088\u0089\u0005/\u0000\u0000\u0089\u008a"+
		"\u0001\u0000\u0000\u0000\u008a\u008b\u0006\u0013\u0000\u0000\u008b(\u0001"+
		"\u0000\u0000\u0000\u008c\u008d\u0007\u0004\u0000\u0000\u008d\u008e\u0001"+
		"\u0000\u0000\u0000\u008e\u008f\u0006\u0014\u0000\u0000\u008f*\u0001\u0000"+
		"\u0000\u0000\n\u0000U^`giqv|\u0084\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}