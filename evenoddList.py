list=[]
n=int(input("Enter num of ele: "))
for i in range(n):
	ele = int(input("Enter ele: "))
	list.append(ele)
	
even=[]
odd=[]
for i in range(n):
	if(list[i]%2==0):
		even.append(list[i])
	else:
		odd.append(list[i])

print("List: ",list)
print("Even List: ",even)
print("Odd List: ",odd)
