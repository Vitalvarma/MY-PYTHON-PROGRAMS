list1 = [];
n1=int(input("Enter num of ele in list1: "))
for i in range(n1):
	ele1 = input("Enter ele: ")
	list1.append(ele1)

list2 = [];
n2=int(input("Enter num of ele in list2: "))
for i in range(n2):
	ele2 = input("Enter ele: ")
	list2.append(ele2)

output =[]
k = len(list1) if len(list1) < len(list2) else len(list2)
for i in range(k):
	output.append(list1[i] + list2[i])
	
print(output)
