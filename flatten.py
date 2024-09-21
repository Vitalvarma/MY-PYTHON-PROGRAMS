def flatten(listmain):
	return [j for i in listmain for j in i]
	
	
inpu = [[1,2,3,4,5],[4,5,6,7,8],[2,3,4,6,7,8]]
result = flatten(inpu)
print("Flatten list: ",result)

