list = [];
n=int(input("Enter num of ele: "))
for i in range(n):
	ele = int(input("Enter ele: "))
	list.append(ele)
	
list.sort()

print("List: ",list)
print("Maximum position: ",list[len(list)-1])
print("Minimum position: ",list[0])
