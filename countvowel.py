s=input("Enter the string: ")
vow=['a','e','i','o','u','A','U','O','I','E']
count=0
for i in s:
	if i in vow:
		count+=1
		
print(count)
