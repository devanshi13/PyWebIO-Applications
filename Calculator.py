from pywebio.input import*
from pywebio.output import*
def calculator():
	a = input("Enter First Number :", type=FLOAT)
	b = input("Enter Second Number :", type=FLOAT)
	result = 0
	operation = radio("Chooose one operation :", options=['+','-','*','/','%'])
	operation_name=""
	if operation=='+':
		operation_name="Addition"
		result = a+b
	elif operation=='-':
		operation_name="Subtaction"
		result = a-b
	elif operation=='*':
		operation_name="Multiplication"
		result = a*b
	elif operation=='/':
		operation_name="Division"
		result = a/b
	else:
		operation_name="Modulus"
		result = a%b
	
	put_text("The operation selected is : %s." % (operation_name))
	put_text("The output is : %.2f" % (result))

if __name__ == "__main__":
	calculator()
	