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


class QueueMin:

	def __init__(self):
		self.s1 = []
		self.s2 = []

	def min(self):
		if(len(self.s1)==0 or len(self.s2)==0):
			minimum = self.s2[-1][1] if(len(self.s1)==0) else self.s1[-1][1]
		else:
			minimum = min(self.s1[-1][1], self.s2[-1][1])
		return minimum

	def enqueue(self, new_element):
		minimum = new_element if(len(self.s1)==0) else min(new_element,self.s1[-1][1])
		self.s1.append((new_element, minimum))

	def dequeue(self):
		if(len(self.s2)==0):
			while(not len(self.s1)==0):
				element = self.s1[-1][0]
				self.s1.pop()
				minimum = element if(len(self.s2)==0) else min(element, self.s2[-1][1])
				self.s2.append((element,minimum))

		remove_element = self.s2[-1][0]
		self.s2.pop()
		return remove_element

def minimumInSubarrays(a, k):
	"""Recieve an array of length n and a positive length k
	and returns minimun in all subarrays a[i:i+k] in O(n)"""
	q = QueueMin()
	out = []
	for i in range(min(k,len(a))):
		q.enqueue(a[i])
	out.append(q.min())

	for el in a[k:]:
		q.enqueue(el)
		q.dequeue()
		out.append(q.min())

	return out
