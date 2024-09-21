def lcm(a,b):
	if a>b:
		high=a
	else:
		high=b
	while(1):
		if(high%a==0) and (high%b==0):
			lcm=high
			break
		high+=1
	return lcm
	
def gcd(a,b):
	return a * b / lcm(a,b)
	
a=int(input("Enter the 1st ele: "))
b=int(input("Enter the 2nd ele: "))

print("LCM of two numbers: ",lcm(a,b))
print("GCD of two numbers: ",gcd(a,b))
	
