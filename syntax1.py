import ply.yacc as yacc
from lexicon import tokens
from semantic import *
import sys

global texto

texto=""

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
	global texto
	"""program : statement_list"""
	texto+="Program"
	p[0] = Program("Program", p[1])

def p_statement1(p):
	global texto
	"""statement : block_statement"""
	texto+="Block statement"
	p[0] = NonTerminal("Block statement", p[1])

def p_block_statement1(p):
	global texto
	"""block_statement : header newline inner_statement_list backspace"""
	texto+="Block statement 1"
	p[0] = NonTerminal("Block statement", p[1], p[3])

def p_block_statement2(p):
	global texto
	"""block_statement : header newline inner_statement_list"""
	texto+="Block statement 2"
	p[0] = NonTerminal("Block statement", p[1], p[3])

def p_empty_block(p):
	global texto
	"""block_statement : empty"""
	texto+="Null"
	p[0] = Null()

def p_header1(p):
	global texto
	"""header : defined_function"""
	texto+="Header"
	p[0] = NonTerminal("Header", p[1])

def p_header2(p):
	global texto
	"""header : conditional_statement"""
	texto+="Header"
	p[0] = NonTerminal("Header", p[1])

def p_header3(p):
	global texto
	"""header : repetitive_statement"""
	texto+="Header"
	p[0] = NonTerminal("Header", p[1])

def p_defined_function(p):
	global texto
	"""defined_function : def identifier left_parenthesis parameter right_parenthesis colon"""
	texto+="Defined function"
	p[0] = NonTerminal("Defined function", Terminal(p[2]), p[4])

def p_parameter1(p):
	global texto
	"""parameter : identifier"""
	texto+="Function parameter 1"
	p[0] = NonTerminal("Function parameter 1", Terminal(p[1]))

def p_parameter2(p):
	global texto
	"""parameter : parameter comma identifier"""
	texto+="Function parameter 2"
	p[0] = NonTerminal("Function parameter 1", p[1] , Terminal(p[3]))

def p_parameter3(p):
	global texto
	"""parameter : empty"""
	texto+="No function parameters"
	p[0] = Null()

def p_conditional_statement1(p):
	global texto
	"""conditional_statement : if boolean_expression colon"""
	texto+="If"
	p[0] = NonTerminal("If", p[2])

def p_conditional_statement2(p):
	global texto
	"""conditional_statement : if boolean colon"""
	texto+="If"
	p[0] = NonTerminal("If", p[2])

def p_conditional_statement3(p):
	global texto
	"""conditional_statement : elif boolean_expression colon"""
	texto+="Else-if"
	p[0] = NonTerminal("Else-if", p[2])

def p_conditional_statement4(p):
	global texto
	"""conditional_statement : elif boolean colon"""
	texto+="Else-if"
	p[0] = NonTerminal("Else-if", p[2])

def p_conditional_statement5(p):
	global texto
	"""conditional_statement : else colon"""
	texto+="Else"
	p[0] = NonTerminal("Else")

def p_repetitive_statement1(p):
	global texto
	"""repetitive_statement : for identifier in identifier colon"""
	texto+="For loop"
	p[0] = NonTerminal("For loop", Terminal(p[2]), Terminal(p[4]))

def p_repetitive_statement2(p):
	global texto
	"""repetitive_statement : while boolean_expression colon"""
	texto+="While loop"
	p[0] = NonTerminal("While loop", p[2])

def p_repetitive_statement3(p):
	global texto
	"""repetitive_statement : while boolean colon"""
	texto+="While loop"
	p[0] = NonTerminal("While loop", p[2])

def p_inner_statement_list1(p):
	global texto
	"""inner_statement_list : inner_statement newline"""
	texto+="Inner statement 1"
	p[0] = NonTerminal("Inner statement 1", p[1])

def p_inner_statement_list2(p):
	global texto
	"""inner_statement_list : inner_statement"""
	texto+="Inner statement 2"
	p[0] = NonTerminal("Inner statement 2", p[1])

def p_inner_statement_list3(p):
	global texto
	"""inner_statement_list : inner_statement_list inner_statement newline"""
	texto+="Inner statement 3"
	p[0] = NonTerminal("Inner statement 3", p[1], p[2])

def p_inner_statement_list4(p):
	global texto
	"""inner_statement_list : inner_statement_list inner_statement"""
	texto+="Inner statement 4"
	p[0] = NonTerminal("Inner statement 4", p[1], p[2])

def p_inner_statement1(p):
	global texto
	"""inner_statement : identation statement"""
	texto+="Inner statement"
	p[0] = NonTerminal("Inner statement", p[2])

def p_inner_statement2(p):
	global texto
	"""inner_statement : identation inner_statement"""
	texto+="Inner statement"
	p[0] = NonTerminal("Inner statement", p[2])

def p_statement_list1(p):
	global texto
	"""statement_list : statement newline"""
	texto+="Statement 1"
	p[0] = NonTerminal("Statement 1", p[1])

def p_statement_list2(p):
	global texto
	"""statement_list : statement"""
	texto+="Statement 2"
	p[0] = NonTerminal("Statement 2", p[1])

def p_statement_list3(p):
	global texto
	"""statement_list : statement_list statement newline"""
	texto+="Statement 3"
	p[0] = NonTerminal("Statement 3", p[1], p[2])

def p_statement_list4(p):
	global texto
	"""statement_list : statement_list statement"""
	texto+="Statement 4"
	p[0] = NonTerminal("Statement 4", p[1], p[2])

def p_empty_statement_list(p):
	global texto
	"""statement_list : empty"""
	texto+="Null"
	p[0] = Null()

def p_statement2(p):
	global texto
	"""statement : assign_value"""
	texto+="Assign statement"
	p[0] = NonTerminal("Assign statement", p[1])

def p_assign_value(p):
	global texto
	"""assign_value : identifier assign_operator value"""
	texto+="Assign value"
	p[0] = NonTerminal("Assign value", Terminal(p[1]), p[2], p[3])

def p_assign_operator1(p):
	global texto
	"""assign_operator : assign"""
	texto+="Assign"
	p[0] = NonTerminal("Assign", Terminal(p[1]))

def p_assign_operator2(p):
	global texto
	"""assign_operator : update"""
	texto+="Update"
	p[0] = NonTerminal("Update", p[1])

def p_update1(p):
	global texto
	"""update : increment"""
	texto+="Increment or self string concatenation"
	p[0] = NonTerminal("Increment or self string concatenation", Terminal(p[1]))

def p_update2(p):
	global texto
	"""update : decrement"""
	texto+="Decrement"
	p[0] = NonTerminal("Decrement", Terminal(p[1]))

def p_update3(p):
	global texto
	"""update : self_product"""
	texto+="Self product"
	p[0] = NonTerminal("Self product", Terminal(p[1]))

def p_update4(p):
	global texto
	"""update : self_division"""
	texto+="Self division"
	p[0] = NonTerminal("Self division", Terminal(p[1]))

def p_update5(p):
	global texto
	"""update : self_integer_division"""
	texto+="Self integer division"
	p[0] = NonTerminal("Self integer division", Terminal(p[1]))

def p_update6(p):
	global texto
	"""update : self_module"""
	texto+="Self module"
	p[0] = NonTerminal("Self module", Terminal(p[1]))

def p_update7(p):
	global texto
	"""update : self_power"""
	texto+="Self power"
	p[0] = NonTerminal("Self power", Terminal(p[1]))

def p_value1(p):
	global texto
	"""value : number"""
	texto+="Number"
	p[0] = NonTerminal("Number", p[1])

def p_number1(p):
	global texto
	"""number : float"""
	texto+="Float"
	p[0] = NonTerminal("Float", Terminal(p[1]))

def p_number2(p):
	global texto
	"""number : integer"""
	texto+="Integer"
	p[0] = NonTerminal("Integer", Terminal(p[1]))

def p_number3(p):
	global texto
	"""number : identifier"""
	texto+="Variable"
	p[0] = NonTerminal("Variable", Terminal(p[1]))

def p_value2(p):
	global texto
	"""value : boolean"""
	texto+="Boolean"
	p[0] = NonTerminal("Boolean", p[1])

def p_boolean1(p):
	global texto
	"""boolean : True"""
	texto+="True"
	p[0] = NonTerminal("True", Terminal(p[1]))

def p_boolean2(p):
	global texto
	"""boolean : False"""
	texto+="False"
	p[0] = NonTerminal("False", Terminal(p[1]))

def p_boolean3(p):
	global texto
	"""boolean : identifier"""
	texto+="Variable"
	p[0] = NonTerminal("Variable", Terminal(p[1]))

def p_value3(p):
	global texto
	"""value : text"""
	texto+="Text"
	p[0] = NonTerminal("Text", p[1])

def p_text1(p):
	global texto
	"""text : string"""
	texto+="String"
	p[0] = NonTerminal("String", Terminal(p[1]))

def p_text2(p):
	global texto
	"""text : formatted_string"""
	texto+="Formatted string"
	p[0] = NonTerminal("Formatted string", p[1])

def p_text3(p):
	global texto
	"""text : identifier"""
	texto+="Variable"
	p[0] = NonTerminal("Variable", Terminal(p[1]))

def p_formatted_string(p):
	global texto
	"""formatted_string : text module left_parenthesis element right_parenthesis"""
	texto+="Formatted string"
	p[0] = NonTerminal("Formatted string", Terminal(p[1]), Terminal(p[2]), p[4])

def p_value4(p):
	global texto
	"""value : expression"""
	texto+="Expression"
	p[0] = NonTerminal("Expression", p[1])

def p_expression1(p):
	global texto
	"""expression : arithmetic_expression"""
	texto+="Arithmetic expression"
	p[0] = NonTerminal("Arithmetic expression", p[1])

def p_arithmetic_expression1(p):
	global texto
	"""arithmetic_expression : number arithmetic_operator number"""
	texto+="Arithmetic expression 1"
	p[0] = NonTerminal("Arithmetic expression 1", p[1], p[2], p[3])

def p_arithmetic_expression2(p):
	global texto
	"""arithmetic_expression : arithmetic_expression arithmetic_operator number"""
	texto+="Arithmetic expression 2"
	p[0] = NonTerminal("Arithmetic expression 2", p[1], p[2], p[3])

def p_arithmetic_operator1(p):
	global texto
	"""arithmetic_operator : plus"""
	texto+="Sum"
	p[0] = NonTerminal("Sum", Terminal(p[1]))

def p_arithmetic_operator2(p):
	global texto
	"""arithmetic_operator : minus"""
	texto+="Difference"
	p[0] = NonTerminal("Difference", Terminal(p[1]))

def p_arithmetic_operator3(p):
	global texto
	"""arithmetic_operator : product"""
	texto+="Product"
	p[0] = NonTerminal("Product", Terminal(p[1]))

def p_arithmetic_operator4(p):
	global texto
	"""arithmetic_operator : division"""
	texto+="Division"
	p[0] = NonTerminal("Division", Terminal(p[1]))

def p_arithmetic_operator5(p):
	global texto
	"""arithmetic_operator : integer_division"""
	texto+="Integer division"
	p[0] = NonTerminal("Integer division", Terminal(p[1]))

def p_arithmetic_operator6(p):
	global texto
	"""arithmetic_operator : module"""
	texto+="Module"
	p[0] = NonTerminal("Module", Terminal(p[1]))

def p_arithmetic_operator7(p):
	global texto
	"""arithmetic_operator : power"""
	texto+="Power"
	p[0] = NonTerminal("Power", Terminal(p[1]))

def p_expression2(p):
	global texto
	"""expression : boolean_expression"""
	texto+="Boolean expression"
	p[0] = NonTerminal("Boolean expression", p[1])

def p_boolean_expression1(p):
	global texto
	"""boolean_expression : number relational_operator number"""
	texto+="Boolean expression 1"
	p[0] = NonTerminal("Boolean expression 1", p[1], p[2], p[3])

def p_boolean_expression2(p):
	global texto
	"""boolean_expression : arithmetic_expression relational_operator number"""
	texto+="Boolean expression 2"
	p[0] = NonTerminal("Boolean expression 2", p[1], p[2], p[3])

def p_boolean_expression3(p):
	global texto
	"""boolean_expression : number relational_operator arithmetic_expression"""
	texto+="Boolean expression 3"
	p[0] = NonTerminal("Boolean expression 3", p[1], p[2], p[3])

def p_boolean_expression4(p):
	global texto
	"""boolean_expression : arithmetic_expression relational_operator arithmetic_expression"""
	texto+="Boolean expression 4"
	p[0] = NonTerminal("Boolean expression 4", p[1], p[2], p[3])

def p_boolean_expression5(p):
	global texto
	"""boolean_expression : boolean boolean_operator boolean"""
	texto+="Boolean expression 5"
	p[0] = NonTerminal("Boolean expression 5", p[1], p[2], p[3])

def p_boolean_expression6(p):
	global texto
	"""boolean_expression : not boolean"""
	texto+="Boolean expression 6"
	p[0] = NonTerminal("Boolean expression 6", Terminal(p[1]), p[2])

def p_boolean_expression7(p):
	global texto
	"""boolean_expression : not boolean_expression"""
	texto+="Boolean epxression 7"
	p[0] = NonTerminal("Boolean expression 7", Terminal(p[1]), p[2])

def p_boolean_expression8(p):
	global texto
	"""boolean_expression : boolean_expression boolean_operator boolean"""
	texto+="Boolean expression 8"
	p[0] = NonTerminal("Boolean expression 8", p[1], p[2], p[3])

def p_boolean_expression9(p):
	global texto
	"""boolean_expression : boolean_expression relational_operator number"""
	texto+="Boolean expression 9"
	p[0] = NonTerminal("Boolean expression 9", p[1], p[2], p[3])

def p_boolean_expression10(p):
	global texto
	"""boolean_expression : boolean_expression relational_operator arithmetic_expression"""
	texto+="Boolean expression 10"
	p[0] = NonTerminal("Boolean expression 10", p[1], p[2], p[3])

def p_relational_operator1(p):
	global texto
	"""relational_operator : equals"""
	texto+="Equals"
	p[0] = NonTerminal("Equals", Terminal(p[1]))

def p_relational_operator2(p):
	global texto
	"""relational_operator : non_equal"""
	texto+="Not equal"
	p[0] = NonTerminal("Non_equal", Terminal(p[1]))

def p_relational_operator3(p):
	global texto
	"""relational_operator : less"""
	texto+="Less"
	p[0] = NonTerminal("Less", Terminal(p[1]))

def p_relational_operator4(p):
	global texto
	"""relational_operator : greater"""
	texto+="Greater"
	p[0] = NonTerminal("Greater", Terminal(p[1]))

def p_relational_operator5(p):
	global texto
	"""relational_operator : less_equal"""
	texto+="Less equal"
	p[0] = NonTerminal("Less equal", Terminal(p[1]))

def p_relational_operator6(p):
	global texto
	"""relational_operator : greater_equal"""
	texto+="Greater equal"
	p[0] = NonTerminal("Greater equal", Terminal(p[1]))

def p_boolean_operator1(p):
	global texto
	"""boolean_operator : and"""
	texto+="And"
	p[0] = NonTerminal("And", Terminal(p[1]))

def p_boolean_operator2(p):
	global texto
	"""boolean_operator : or"""
	texto+="Or"
	p[0] = NonTerminal("Or", Terminal(p[1]))

def p_expression_3(p):
	global texto
	"""expression : string_concatenation"""
	texto+="String concatenation"
	p[0] = NonTerminal("String concatenation", p[1])

def p_string_concatenation1(p):
	global texto
	"""string_concatenation : text plus text"""
	texto+="String concatenation 1"
	p[0] = NonTerminal("String concatenation 1", p[1], Terminal(p[2]), p[3])

def p_string_concatenation2(p):
	global texto
	"""string_concatenation : string_concatenation plus text"""
	texto+="String concatenation 2"
	p[0] = NonTerminal("String concatenation 2", p[1], Terminal(p[2]), p[3])

def p_value5(p):
	global texto
	"""value : list"""texto
	texto+="List"
	p[0] = NonTerminal("List", p[1])

def p_value6(p):
	global texto
	"""value : function_call"""
	texto+="Function"
	p[0] = NonTerminal("Function", p[1])

def p_value7(p):
	global texto
	"""value : None"""
	texto+="None"
	p[0] = Terminal(p[1])

def p_list(p):
	global texto
	"""list : left_bracket element right_bracket"""
	texto+="List statement"
	p[0] = NonTerminal("List statement", p[2])

def p_element1(p):
	global texto
	"""element : value"""
	texto+="Element"
	p[0] = NonTerminal("Element", p[1])

def p_element2(p):
	global texto
	"""element : element comma value"""
	texto+="Elements"
	p[0] = NonTerminal("Elements", p[1], p[3])

def p_statement4(p):
	global texto
	"""statement : function_call"""
	texto+="Function call statement"
	p[0] = NonTerminal("Function call statement", p[1])

def p_function_call(p):
	global texto
	"""function_call : identifier left_parenthesis argument right_parenthesis"""
	texto+="Function call"
	p[0] = NonTerminal("Function call", Terminal(p[1]), p[3])

def p_argument1(p):
	global texto
	"""argument : value"""
	texto+="Function call argument"
	p[0] = NonTerminal("Function call argument", p[1])

def p_argument2(p):
	global texto
	"""argument : argument comma value"""
	texto+="Function call argument"
	p[0] = NonTerminal("Function call argument", p[1], p[3])

def p_argument3(p):
	global texto
	"""argument : empty"""
	texto+="No function call arguments"
	p[0] = Null()

def p_statement5(p):
	global texto
	"""statement : return value"""
	texto+="Return statement"
	p[0] = NonTerminal("Return statement", Terminal(p[1]), p[2])

def p_statement6(p):
	global texto
	"""statement : break"""
	texto+="Break statement"
	p[0] = NonTerminal("Break statement", Terminal(p[1]))

def p_empty(p):
	"""empty :"""
	pass

def p_error(p):
	global texto	
	texto+="Invalid syntax %s" % p

def main():	
	global texto
	file= open("input.py",'r')
	content= file.read()
	file.close()
	parser = yacc.yacc()
	result = yacc.parse(content)

	graphFile = open('graph.txt','w')
	graphFile.write(result.translate())
	graphFile.close()	
	
	texto+="\n"+result.translate()
	texto+= "El programa traducido se guardo en el archivo \"graph.txt\". Puedes visualizar el contenido del archivo en www.webgraphviz.com"

	print(texto)
	#return texto

if __name__ == '__main__':   
	main()