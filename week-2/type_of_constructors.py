#this is construcotr for any class in pyton 

class person: 
	def __init__(self, name , age): 
		self.name =name 
		self.age = age 
p1 = person("john " , 30 ) 
print(p1.name) 
print(p1.age) 
print(p1) 

#here we are printing the string of the class via  calling object we can use __strr__ constructor 

class person: 
	def __init__(self,name, age ) : 
		self.name = name 
		self.age = age 
	def __str__(self): 
		return f"{self.name} age is {self.age} " 
p1 = person("sirra" , 117) 
print(p1) 
#this gives me the object value inested of object address  

#self is not a key word it can be replaced with anything we want 

class person: 
	def __init__(cool , name , age)  :
		cool.name = name 
		cool.age = age 
p1 = person("cool self " , 2) 
print(p1.name , p1.age ) 

#We will delet oabject  
print(p1.age) 
del p1.age 
try: 
	print(p1.age) 
except AttributeError: 
	print("called p1.age but we used del to depeat p1.age and freed the space " ) 
