class Stack:

	def __init__(self):
		"""Create an empty stack"""
		self.items = []
	
	def isEmpty(self):
		return len(self.items)==0

	def pop(self):
		if(self.isEmpty()): raise ValueError("Empty stack, cannot pop")
		
		return self.items.pop()
	
	def push(self,newItem):
		self.items.append(newItem)
	
		
		
