n=int(input("Enter the number: "))

check=lambda x:"even" if x%2==0 else "odd"

print(n,"is",check(n))

