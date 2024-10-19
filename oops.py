
class SingleInheritanceDemo:
	variable1=10
	def read_variables(self,variable2,variable3):
		self.variable2=variable2
		self.variable3=variable3
	def write_variable(self):
		print(self.variable2)
		print(self.variable3)
		print(SingleInheritanceDemo.variable1)

obj = SingleInheritanceDemo()
obj.read_variables(23,45)
obj.write_variable()

class CheckConstructor:
	def __init__(self,num1,num2,num3):
		self.num1=num1
		self.num2=num2
		self.num3=num3
	def SumOfTheNumbers(self):
		return self.num1+self.num2+self.num3

obj2 = CheckConstructor(1,23,4)
output=obj2.SumOfTheNumbers()
print(output)

#MultilevelInheritance
class parent:
	def parent_method(self):
		print("Parent Method")
		
class child1(parent):
	def child1_method(self):
		print("child1 method")
		
class child2(child1):
	def child2_method(self):
		print("child2 method")
		
obj3=child2()
obj3.child2_method()
obj3.child1_method()
obj3.parent_method()

#multipleinheritance

class animal():
	def animal_method(self):
		print("This is an animal")
	
class pet():
	def pet_method(self):
		print("This can be a good pet") 
		
class dog(animal,pet):
	def dog_method(self):
		print("Dog is a animal ,which can be a good pet")


obj4=dog()
obj4.pet_method()
obj4.animal_method()
obj4.dog_method()


#destructor
class DeconstructorDemo:
	def __init__(self):
		print("Constructor created.")
	def __del__(self):
		print("Destructor called, Constructor deleted.")
		
obj5=DeconstructorDemo()
del obj5


































