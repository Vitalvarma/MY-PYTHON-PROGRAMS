def addition(a,b):
	return a+b
def subtraction(a,b):
	return a-b
def multiplication(a,b):
	return a*b
def division(a,b):
	return a/b
	
input1 = int(input("Enter 1st input: "))
input2 = int(input("Enter 2nd input: "))

result_add = addition(input1,input2)
result_sub = subtraction(input1,input2)
result_mul = multiplication(input1,input2)
result_div = division(input1,input2)

print("ADD: ",result_add,"SUB: ",result_sub,"MUL: ",result_mul,"DIV: ",result_div)
