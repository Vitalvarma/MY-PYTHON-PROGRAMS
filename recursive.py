def fact(n):
	if n==0:
		return 1
	else:
		return n * fact(n-1)
	
def fibo(n):
	if n<=1:
		return 1
	else:
		return fibo(n-1) + fibo(n-2)
		
def gcd(n,m):
	if n==0:
		return m
	else:
		return gcd(m%n,n)

num = int(input("Enter a number: "))
if num<0:
	print("INVALID")
else:
	print("Factorial of the num: ",fact(num))
	print("fibonacci of the num: ",fibo(num))

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
if num1>num2:
	temp=num2
	num2=num1
	num1=temp
if num1<0 or num2<0:
	print("INVALID")
else:
	print("GCD of the numbers: ",gcd(num1,num2))

