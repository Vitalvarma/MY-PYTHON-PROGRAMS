def secondlarge1(list1):
	if len(list1)<2:
		return
	list1.sort()
	return list1[-2]

list1 = [1,2,3,4,5]
result1 = secondlarge1(list1)
print("second large value is: ",result1)

def secondlarge2(list1):
	if len(list1)<2:
		return
	maxi=list1[0]
	sec=0
	for i in list1:
		if maxi<i:
			sec=maxi
			maxi=i
		else:
			if i>sec:
				sec=i	
				
	return sec
	

list2 = [1,2,3,4,5]
result2 = secondlarge2(list2)
print("second large value is: ",result2)
