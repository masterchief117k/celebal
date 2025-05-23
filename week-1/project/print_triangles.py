size = 3
print("the size of triangle is " , size)

print("THIS IS LOWER TRIANGLE ") 

for i in range(0,size+1) :  
	for j in range(0,i): 
		print("*" , end="") 
	print("")
print(50 * "-") 

print("THIS IS UPPER TRIANGULAR ") 

for i in range (size , 0 , -1 ) : 
	for j  in range (0,i) : 
		print("*" , end="") 
	print("")
print(50 * "-") 

print("THIS IS A PYRAMID") 

for i in range(0,size ) : 
	print( " " * (size - i) + "* " * (i+1) ) 
#the basic idead over hear is to print an traingle with spaces follow it with a a triangle with * adn space to form a pyramid 
