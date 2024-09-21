def extreme(list1):
	if len(list1)<1:
		return
	mini=list1[0]
	maxi=list1[0]
	for i in list1:
		if mini>i:
			mini = i
		if maxi<i:
			maxi = i
	
	return mini,maxi
	

list1 = [1,2,3,4,5]
result = extreme(list1)
print("Min,max values are: ",result)
