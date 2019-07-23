class Node:
	def __init__(self, data = None):
		self.data = data
		self.next = None

class Queue:

	def __init__(self):
		"""Create an empty queue"""
		self.head = None
		self.tail = None 

	
	def isEmpty(self):
		return self.head == None

	def peek(self):
		"""Show queue peek"""
		if(self.isEmpty()): raise ValueError("Peek has no elements.")
		return self.head.data
	
	def enqueue(self,newData):
		"""Enqueue an element to the queue"""

		newNode = Node(newData)
			
		if(self.isEmpty()): 
			self.head = newNode
			self.tail = newNode
		else:
			self.tail.next = newNode
	
	def dequeue(self):
		if(self.isEmpty()): raise ValueError("Empty queue, cannot dequeue")
			
		data = self.head.data
		self.head = self.head.next
		
		if(self.head == None): self.tail = self.head		
		
		return data
		
