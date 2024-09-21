def mulreturn(a,b,c):
	return a+b+c, a+b+c/3, a*b*c

input1 = int(input("Enter the 1st ele: "))
input2 = int(input("Enter the 2nd ele: "))
input3 = int(input("Enter the 3rd ele: "))

result = mulreturn(input1,input2,input3)
print("The sum,avg,product of the given numbers: ",result)
