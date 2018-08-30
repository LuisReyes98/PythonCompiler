import ply.yacc as yacc
from lexicon import tokens
from semantic import *
global text

precedence = (
("left", "or"),
("left", "and"),
("right", "not"),
("right", "in"),
("right", "is"),
("right", "assign"),
("right", "increment", "decrement", "self_product", "self_division", "self_integer_division", "self_module", "self_power"),
("left", "equals", "non_equal"),
("left", "less", "greater", "less_equal", "greater_equal"),
("left", "plus", "minus"),
("left", "product", "division", "integer_division", "module"),
("left", "power"),
("left", "left_parenthesis", "right_parenthesis"),
)

def p_program(p):
	"""program : statement_list"""
	print("Program")
	p[0] = Program("Program", p[1])

def p_statement1(p):
	"""statement : block_statement"""
	print("Block statement")
	p[0] = NonTerminal("Block statement", p[1])

def p_block_statement1(p):
	"""block_statement : header newline inner_statement_list backspace"""
	print("Block statement 1")
	p[0] = NonTerminal("Block statement", p[1], p[3])

def p_block_statement2(p):
	"""block_statement : header newline inner_statement_list"""
	print("Block statement 2")
	p[0] = NonTerminal("Block statement", p[1], p[3])

def p_empty_block(p):
	"""block_statement : empty"""
	print("Null")
	p[0] = Null()

def p_header1(p):
	"""header : defined_function"""
	print("Header")
	p[0] = NonTerminal("Header", p[1])

def p_header2(p):
	"""header : conditional_statement"""
	print("Header")
	p[0] = NonTerminal("Header", p[1])

def p_header3(p):
	"""header : repetitive_statement"""
	print("Header")
	p[0] = NonTerminal("Header", p[1])

def p_defined_function(p):
	"""defined_function : def identifier left_parenthesis parameter right_parenthesis colon"""
	print("Defined function")
	p[0] = NonTerminal("Defined function", Terminal(p[2]), p[4])

def p_parameter1(p):
	"""parameter : identifier"""
	print("Function parameter 1")
	p[0] = NonTerminal("Function parameter 1", Terminal(p[1]))

def p_parameter2(p):
	"""parameter : parameter comma identifier"""
	print("Function parameter 2")
	p[0] = NonTerminal("Function parameter 1", p[1] , Terminal(p[3]))

def p_parameter3(p):
	"""parameter : empty"""
	print("No function parameters")
	p[0] = Null()

def p_conditional_statement1(p):
	"""conditional_statement : if boolean_expression colon"""
	print("If")
	p[0] = NonTerminal("If", p[2])

def p_conditional_statement2(p):
	"""conditional_statement : if boolean colon"""
	print("If")
	p[0] = NonTerminal("If", p[2])

def p_conditional_statement3(p):
	"""conditional_statement : elif boolean_expression colon"""
	print("Else-if")
	p[0] = NonTerminal("Else-if", p[2])

def p_conditional_statement4(p):
	"""conditional_statement : elif boolean colon"""
	print("Else-if")
	p[0] = NonTerminal("Else-if", p[2])

def p_conditional_statement5(p):
	"""conditional_statement : else colon"""
	print("Else")
	p[0] = NonTerminal("Else")

def p_repetitive_statement1(p):
	"""repetitive_statement : for identifier in identifier colon"""
	print("For loop")
	p[0] = NonTerminal("For loop", Terminal(p[2]), Terminal(p[4]))

def p_repetitive_statement2(p):
	"""repetitive_statement : while boolean_expression colon"""
	print("While loop")
	p[0] = NonTerminal("While loop", p[2])

def p_repetitive_statement3(p):
	"""repetitive_statement : while boolean colon"""
	print("While loop")
	p[0] = NonTerminal("While loop", p[2])

def p_inner_statement_list1(p):
	"""inner_statement_list : inner_statement newline"""
	print("Inner statement 1")
	p[0] = NonTerminal("Inner statement 1", p[1])

def p_inner_statement_list2(p):
	"""inner_statement_list : inner_statement"""
	print("Inner statement 2")
	p[0] = NonTerminal("Inner statement 2", p[1])

def p_inner_statement_list3(p):
	"""inner_statement_list : inner_statement_list inner_statement newline"""
	print("Inner statement 3")
	p[0] = NonTerminal("Inner statement 3", p[1], p[2])

def p_inner_statement_list4(p):
	"""inner_statement_list : inner_statement_list inner_statement"""
	print("Inner statement 4")
	p[0] = NonTerminal("Inner statement 4", p[1], p[2])

def p_inner_statement1(p):
	"""inner_statement : identation statement"""
	print("Inner statement")
	p[0] = NonTerminal("Inner statement", p[2])

def p_inner_statement2(p):
	"""inner_statement : identation inner_statement"""
	print("Inner statement")
	p[0] = NonTerminal("Inner statement", p[2])

def p_statement_list1(p):
	"""statement_list : statement newline"""
	print("Statement 1")
	p[0] = NonTerminal("Statement 1", p[1])

def p_statement_list2(p):
	"""statement_list : statement"""
	print("Statement 2")
	p[0] = NonTerminal("Statement 2", p[1])

def p_statement_list3(p):
	"""statement_list : statement_list statement newline"""
	print("Statement 3")
	p[0] = NonTerminal("Statement 3", p[1], p[2])

def p_statement_list4(p):
	"""statement_list : statement_list statement"""
	print("Statement 4")
	p[0] = NonTerminal("Statement 4", p[1], p[2])

def p_empty_statement_list(p):
	"""statement_list : empty"""
	print("Null")
	p[0] = Null()

def p_statement2(p):
	"""statement : assign_value"""
	print("Assign statement")
	p[0] = NonTerminal("Assign statement", p[1])

def p_assign_value(p):
	"""assign_value : identifier assign_operator value"""
	print("Assign value")
	p[0] = NonTerminal("Assign value", Terminal(p[1]), p[2], p[3])

def p_assign_operator1(p):
	"""assign_operator : assign"""
	print("Assign")
	p[0] = NonTerminal("Assign", Terminal(p[1]))

def p_assign_operator2(p):
	"""assign_operator : update"""
	print("Update")
	p[0] = NonTerminal("Update", p[1])

def p_update1(p):
	"""update : increment"""
	print("Increment or self string concatenation")
	p[0] = NonTerminal("Increment or self string concatenation", Terminal(p[1]))

def p_update2(p):
	"""update : decrement"""
	print("Decrement")
	p[0] = NonTerminal("Decrement", Terminal(p[1]))

def p_update3(p):
	"""update : self_product"""
	print("Self product")
	p[0] = NonTerminal("Self product", Terminal(p[1]))

def p_update4(p):
	"""update : self_division"""
	print("Self division")
	p[0] = NonTerminal("Self division", Terminal(p[1]))

def p_update5(p):
	"""update : self_integer_division"""
	print("Self integer division")
	p[0] = NonTerminal("Self integer division", Terminal(p[1]))

def p_update6(p):
	"""update : self_module"""
	print("Self module")
	p[0] = NonTerminal("Self module", Terminal(p[1]))

def p_update7(p):
	"""update : self_power"""
	print("Self power")
	p[0] = NonTerminal("Self power", Terminal(p[1]))

def p_value1(p):
	"""value : number"""
	print("Number")
	p[0] = NonTerminal("Number", p[1])

def p_number1(p):
	"""number : float"""
	print("Float")
	p[0] = NonTerminal("Float", Terminal(p[1]))

def p_number2(p):
	"""number : integer"""
	print("Integer")
	p[0] = NonTerminal("Integer", Terminal(p[1]))

def p_number3(p):
	"""number : identifier"""
	print("Variable")
	p[0] = NonTerminal("Variable", Terminal(p[1]))

def p_value2(p):
	"""value : boolean"""
	print("Boolean")
	p[0] = NonTerminal("Boolean", p[1])

def p_boolean1(p):
	"""boolean : True"""
	print("True")
	p[0] = NonTerminal("True", Terminal(p[1]))

def p_boolean2(p):
	"""boolean : False"""
	print("False")
	p[0] = NonTerminal("False", Terminal(p[1]))

def p_boolean3(p):
	"""boolean : identifier"""
	print("Variable")
	p[0] = NonTerminal("Variable", Terminal(p[1]))

def p_value3(p):
	"""value : text"""
	print("Text")
	p[0] = NonTerminal("Text", p[1])

def p_text1(p):
	"""text : string"""
	print("String")
	p[0] = NonTerminal("String", Terminal(p[1]))

def p_text2(p):
	"""text : formatted_string"""
	print("Formatted string")
	p[0] = NonTerminal("Formatted string", p[1])

def p_text3(p):
	"""text : identifier"""
	print("Variable")
	p[0] = NonTerminal("Variable", Terminal(p[1]))

def p_formatted_string(p):
	"""formatted_string : text module left_parenthesis element right_parenthesis"""
	print("Formatted string")
	p[0] = NonTerminal("Formatted string", Terminal(p[1]), Terminal(p[2]), p[4])

def p_value4(p):
	"""value : expression"""
	print("Expression")
	p[0] = NonTerminal("Expression", p[1])

def p_expression1(p):
	"""expression : arithmetic_expression"""
	print("Arithmetic expression")
	p[0] = NonTerminal("Arithmetic expression", p[1])

def p_arithmetic_expression1(p):
	"""arithmetic_expression : number arithmetic_operator number"""
	print("Arithmetic expression 1")
	p[0] = NonTerminal("Arithmetic expression 1", p[1], p[2], p[3])

def p_arithmetic_expression2(p):
	"""arithmetic_expression : arithmetic_expression arithmetic_operator number"""
	print("Arithmetic expression 2")
	p[0] = NonTerminal("Arithmetic expression 2", p[1], p[2], p[3])

def p_arithmetic_operator1(p):
	"""arithmetic_operator : plus"""
	print("Sum")
	p[0] = NonTerminal("Sum", Terminal(p[1]))

def p_arithmetic_operator2(p):
	"""arithmetic_operator : minus"""
	print("Difference")
	p[0] = NonTerminal("Difference", Terminal(p[1]))

def p_arithmetic_operator3(p):
	"""arithmetic_operator : product"""
	print("Product")
	p[0] = NonTerminal("Product", Terminal(p[1]))

def p_arithmetic_operator4(p):
	"""arithmetic_operator : division"""
	print("Division")
	p[0] = NonTerminal("Division", Terminal(p[1]))

def p_arithmetic_operator5(p):
	"""arithmetic_operator : integer_division"""
	print("Integer division")
	p[0] = NonTerminal("Integer division", Terminal(p[1]))

def p_arithmetic_operator6(p):
	"""arithmetic_operator : module"""
	print("Module")
	p[0] = NonTerminal("Module", Terminal(p[1]))

def p_arithmetic_operator7(p):
	"""arithmetic_operator : power"""
	print("Power")
	p[0] = NonTerminal("Power", Terminal(p[1]))

def p_expression2(p):
	"""expression : boolean_expression"""
	print("Boolean expression")
	p[0] = NonTerminal("Boolean expression", p[1])

def p_boolean_expression1(p):
	"""boolean_expression : number relational_operator number"""
	print("Boolean expression 1")
	p[0] = NonTerminal("Boolean expression 1", p[1], p[2], p[3])

def p_boolean_expression2(p):
	"""boolean_expression : arithmetic_expression relational_operator number"""
	print("Boolean expression 2")
	p[0] = NonTerminal("Boolean expression 2", p[1], p[2], p[3])

def p_boolean_expression3(p):
	"""boolean_expression : number relational_operator arithmetic_expression"""
	print("Boolean expression 3")
	p[0] = NonTerminal("Boolean expression 3", p[1], p[2], p[3])

def p_boolean_expression4(p):
	"""boolean_expression : arithmetic_expression relational_operator arithmetic_expression"""
	print("Boolean expression 4")
	p[0] = NonTerminal("Boolean expression 4", p[1], p[2], p[3])

def p_boolean_expression5(p):
	"""boolean_expression : boolean boolean_operator boolean"""
	print("Boolean expression 5")
	p[0] = NonTerminal("Boolean expression 5", p[1], p[2], p[3])

def p_boolean_expression6(p):
	"""boolean_expression : not boolean"""
	print("Boolean expression 6")
	p[0] = NonTerminal("Boolean expression 6", Terminal(p[1]), p[2])

def p_boolean_expression7(p):
	"""boolean_expression : not boolean_expression"""
	print("Boolean epxression 7")
	p[0] = NonTerminal("Boolean expression 7", Terminal(p[1]), p[2])

def p_boolean_expression8(p):
	"""boolean_expression : boolean_expression boolean_operator boolean"""
	print("Boolean expression 8")
	p[0] = NonTerminal("Boolean expression 8", p[1], p[2], p[3])

def p_boolean_expression9(p):
	"""boolean_expression : boolean_expression relational_operator number"""
	print("Boolean expression 9")
	p[0] = NonTerminal("Boolean expression 9", p[1], p[2], p[3])

def p_boolean_expression10(p):
	"""boolean_expression : boolean_expression relational_operator arithmetic_expression"""
	print("Boolean expression 10")
	p[0] = NonTerminal("Boolean expression 10", p[1], p[2], p[3])

def p_relational_operator1(p):
	"""relational_operator : equals"""
	print("Equals")
	p[0] = NonTerminal("Equals", Terminal(p[1]))

def p_relational_operator2(p):
	"""relational_operator : non_equal"""
	print("Not equal")
	p[0] = NonTerminal("Non_equal", Terminal(p[1]))

def p_relational_operator3(p):
	"""relational_operator : less"""
	print("Less")
	p[0] = NonTerminal("Less", Terminal(p[1]))

def p_relational_operator4(p):
	"""relational_operator : greater"""
	print("Greater")
	p[0] = NonTerminal("Greater", Terminal(p[1]))

def p_relational_operator5(p):
	"""relational_operator : less_equal"""
	print("Less equal")
	p[0] = NonTerminal("Less equal", Terminal(p[1]))

def p_relational_operator6(p):
	"""relational_operator : greater_equal"""
	print("Greater equal")
	p[0] = NonTerminal("Greater equal", Terminal(p[1]))

def p_boolean_operator1(p):
	"""boolean_operator : and"""
	print("And")
	p[0] = NonTerminal("And", Terminal(p[1]))

def p_boolean_operator2(p):
	"""boolean_operator : or"""
	print("Or")
	p[0] = NonTerminal("Or", Terminal(p[1]))

def p_expression_3(p):
	"""expression : string_concatenation"""
	print("String concatenation")
	p[0] = NonTerminal("String concatenation", p[1])

def p_string_concatenation1(p):
	"""string_concatenation : text plus text"""
	print("String concatenation 1")
	p[0] = NonTerminal("String concatenation 1", p[1], Terminal(p[2]), p[3])

def p_string_concatenation2(p):
	"""string_concatenation : string_concatenation plus text"""
	print("String concatenation 2")
	p[0] = NonTerminal("String concatenation 2", p[1], Terminal(p[2]), p[3])

def p_value5(p):
	"""value : list"""
	print("List")
	p[0] = NonTerminal("List", p[1])

def p_value6(p):
	"""value : function_call"""
	print("Function")
	p[0] = NonTerminal("Function", p[1])

def p_value7(p):
	"""value : None"""
	print("None")
	p[0] = Terminal(p[1])

def p_list(p):
	"""list : left_bracket element right_bracket"""
	print("List statement")
	p[0] = NonTerminal("List statement", p[2])

def p_element1(p):
	"""element : value"""
	print("Element")
	p[0] = NonTerminal("Element", p[1])

def p_element2(p):
	"""element : element comma value"""
	print("Elements")
	p[0] = NonTerminal("Elements", p[1], p[3])

def p_statement4(p):
	"""statement : function_call"""
	print("Function call statement")
	p[0] = NonTerminal("Function call statement", p[1])

def p_function_call(p):
	"""function_call : identifier left_parenthesis argument right_parenthesis"""
	print("Function call")
	p[0] = NonTerminal("Function call", Terminal(p[1]), p[3])

def p_argument1(p):
	"""argument : value"""
	print("Function call argument")
	p[0] = NonTerminal("Function call argument", p[1])

def p_argument2(p):
	"""argument : argument comma value"""
	print("Function call argument")
	p[0] = NonTerminal("Function call argument", p[1], p[3])

def p_argument3(p):
	"""argument : empty"""
	print("No function call arguments")
	p[0] = Null()

def p_statement5(p):
	"""statement : return value"""
	print("Return statement")
	p[0] = NonTerminal("Return statement", Terminal(p[1]), p[2])

def p_statement6(p):
	"""statement : break"""
	print("Break statement")
	p[0] = NonTerminal("Break statement", Terminal(p[1]))

def p_empty(p):
	"""empty :"""
	pass

def p_error(p):
	print("Invalid syntax %s" % p)

def main():
	text=""	
	file = open("input.py", "r")
	content = file.read()
	file.close()
	parser = yacc.yacc()
	#text+=(parser.parse(content).__str__())
	#text+=aux.translate()

	result = yacc.parse(content)
	text+=("\n"+result.translate())

	graphFile = open('graph.txt','w')
	graphFile.write(result.translate())
	graphFile.close()

	text+=("\n\nEl programa traducido se guardo en el archivo \"graph.txt\". Puedes visualizar el contenido del archivo en www.webgraphviz.com")

	return text
