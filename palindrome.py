n = int(input("Enter a number: "))
original = n
rev = n % 10
n = n//10
while n>0:
	rev *= 10
	rem = n % 10
	rev += rem
	n = n // 10
if original==rev:
	print(original,"is a palindrome number")
else:
	print(original,"is not a palindrome number")
