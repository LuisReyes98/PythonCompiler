import ply.lex as lex
from keyword import kwlist
operators = ["plus", "minus", "product", "division", "integer_division", "module", "power", "equals", "non_equal", "less", "greater", 
"less_equal", "greater_equal"]
delimiters = ["left_parenthesis", "right_parenthesis", "left_bracket", "right_bracket", "left_brace", "right_brace", "period", "comma", "colon", 
"semicolon", "at", "assign", "increment", "decrement", "self_product", "self_division", "self_integer_division", "self_module", "self_power"]
others = ["identifier", "identation", "backspace", "float", "integer", "string", "newline"]
tokens = kwlist + operators + delimiters + others
t_ignore = ' '
t_plus = r'\+'
t_minus = r'-'
t_product = r'\*'
t_division = r'/'
t_integer_division = r'//'
t_module = r'%'
t_power = r'\*\*'
t_equals = r'=='
t_non_equal = r'!='
t_less = r'<'
t_greater = r'>'
t_less_equal = r'<='
t_greater_equal = r'>='
t_left_parenthesis = r'\('
t_right_parenthesis = r'\)'
t_left_bracket = r'\['
t_right_bracket = r']'
t_left_brace = r'{'
t_right_brace = r'}'
t_period = r'\.'
t_comma = r','
t_colon = r':'
t_semicolon = r';'
t_assign = r'='
t_increment = r'\+='
t_decrement = r'-='
t_self_product = r'\*='
t_self_division = r'/='
t_self_integer_division = r'//='
t_self_module = r'%='
t_self_power = r'\*\*='
def t_False(t):
	r'False'
	return t
def t_None(t):
	r'None'
	return t
def t_True(t):
	r'True'
	return t
def t_and(t):
	r'and'
	return t
def t_as(t):
	r'as'
	return t
def t_assert(t):
	r'assert'
	return t
def t_break(t):
	r'break'
	return t
def t_class(t):
	r'class'
	return t
def t_continue(t):
	r'continue'
	return t
def t_def(t):
	r'def'
	return t
def t_del(t):
	r'del'
	return t
def t_elif(t):
	r'elif'
	return t
def t_else(t):
	r'else'
	return t
def t_except(t):
	r'except'
	return t
def t_finally(t):
	r'finally'
	return t
def t_for(t):
	r'for'
	return t
def t_from(t):
	r'from'
	return t
def t_global(t):
	r'global'
	return t
def t_if(t):
	r'if'
	return t
def t_import(t):
	r'import'
	return t
def t_lambda(t):
	r'lambda'
	return t
def t_nonlocal(t):
	r'nonlocal'
	return t
def t_not(t):
	r'not'
	return t
def t_or(t):
	r'or'
	return t
def t_pass(t):
	r'pass'
	return t
def t_raise(t):
	r'raise'
	return t
def t_return(t):
	r'return'
	return t
def t_try(t):
	r'try'
	return t
def t_while(t):
	r'while'
	return t
def t_with(t):
	r'with'
	return t
def t_yield(t):
	r'yield'
	return t
def t_identifier(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	return t
def t_in(t):
	r'in'
	return t
def t_is(t):
	r'is'
	return t
def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    return t
def t_identation(t):
	r'\t'
	return t
def t_backspace(t):
	r'\r'
	return t
def t_float(t):
	r'-?\d+\.\d*'
	t.value = float(t.value)
	return t
def t_integer(t):
	r'-?\d+'
	t.value = int(t.value)
	return t
def t_string(t):
	r'(\" | \').*(\" | \')'
	return t
def t_error(t):
	print("Invalid token %s at line %d, position %d" % (t.value, t.lineno, t.lexpos))
	t.lexer.skip(1)

def main():
	texto=""
	file = open("input.py", "r")
	content = file.read()
	file.close()
	analyzer = lex.lex()
	analyzer.input(content)	
	while True:
		token = analyzer.token()
		if not token : break
		print(token)
		texto+=token.__str__()+"\n"
	return texto