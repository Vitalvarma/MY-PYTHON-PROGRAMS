def reverselist(list1):
	reverse_list = []
	for i in range(len(list1)-1,-1,-1):
		reverse_list.append(list1[i])
	return reverse_list
		
list1 = [1,2,3,4,5,6,7,8,9,10]
print("LIST: ",list1)
result = reverselist(list1)
print("REVERSE LIST: ",result)

