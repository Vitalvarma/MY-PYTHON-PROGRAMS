n = int(input("Enter a number: "))
origin = n
sum = 0
while n>0:
	rem = n % 10
	sum += rem ** 3
	n = n // 10
	
if origin==sum:
	print(origin,"is a armstrong number")
else:
	print(origin,"is not a armstrong number")

