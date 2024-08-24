list = [];
n=int(input("Enter num of ele: "))
for i in range(n):
	ele = int(input("Enter ele: "))
	list.append(ele)
	
print("List: ",list)
ele = list[len(list)-1]
list[len(list)-1] = list[0]
list[0] = ele
print("List After interchanging first and last elements: ",list)
