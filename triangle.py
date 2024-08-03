s1=int(input("Enter side 1st:"))
s2=int(input("Enter side 2nd:"))
s3=int(input("Enter side 3rd:"))

if s1+s2>s3 and s2+s3>s1 and s3+s1>s2:
	print("Given is a valid triangle")
else:
	print("Given is not a valid triangle")
