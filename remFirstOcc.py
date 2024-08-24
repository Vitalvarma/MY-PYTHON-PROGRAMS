list = [];
n=int(input("Enter num of ele: "))
for i in range(n):
	ele = int(input("Enter ele: "))
	list.append(ele)

k = int(input("Element to be removed: "))
for j in range(n):
	if(list[j]==k):
		list.remove(list[j])
		break

print("List After removing: ",list)

