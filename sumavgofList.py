list = [];
n=int(input("Enter num of ele: "))
for i in range(n):
	ele = int(input("Enter ele: "))
	list.append(ele)
	
print("List: ",list)
print("Sum: ",sum(list))
print("Average: ",sum(list) / n)
