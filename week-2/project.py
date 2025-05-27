import sys 
#checking pytohn version for smooth execution 

import sys 

if sys.version_info<(3,5):
	sys.exit("from intern  update python to 3.5 or later") 

class node: 
# This class is to define node class 
#Node has data and next as data members 

	def __init__ (self , data: int  )-> None: 
		self.data =data 
		self.next:'node' | None = None  

#defining linked list with functions add and delete 

class  linked_list : 
	def __init__(self) -> None : #only works with python3 not with python2 
		self.head: 'node'|None = None 

	def add (self, val : int  )->None:  
#n is new node 
		n = node(val) 
		if not self.head: 
			self.head = n
			return 
		temp = self.head 	 
		while temp.next !=None : 
			temp = temp.next 
		temp.next = n


#Deletes the nth node 
	def delete (self,  index: int )->None : 
		#assuming when index is 1 the we are at head 
		try:	
			if not self.head: 
				raise ValueError("deleating from empty list") 
			if index<1: 
				raise IndexError("Index must be greater than 1 or 1 ") 
			temp=self.head 
			if index==1:
				self.head=temp.next 
				return 
			prev: node | None = None 
			for i in range(index-1):
				prev =temp 
				temp = temp.next 
				if not temp: 
					raise IndexError("Index out of bound ") 
			prev.next = temp.next 
		except (ValueError, IndexError)as error :
			print(error) 


#Print the linked list 
	def list_printer(self)->None: 
		if not self.head :
			print("The list is empty.") 
			return 
		temp=self.head
		while temp:
			print(temp.data, end="->")
			temp=temp.next
		print("None") 


#This is testing the implimentation 
ll= linked_list()


#testing the adding function 
ll.add(10) 
ll.add(20) 
ll.add(30) 
ll.add(40) 

ll.list_printer()

#deleting 2 nd  index 
ll.delete(2)
ll.list_printer() 

#testing exceptions 
ll.delete(20)#trying to get index out of bount exception 









		
