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

class StackMin:

    def __init__(self):
        """Create an empty stack, with min Query in O(1):
        contains elements (el,min_until_el)"""
        self.items = []

    def __str__(self):
        return str(self.items)
    def isEmpty(self):
        return len(self.items) == 0

    def pop(self):
        if(self.isEmpty()):
            raise ValueError("Empty stack, cannot pop.")

        return self.items.pop()

    def peek(self):
        if(self.isEmpty()):
            raise ValueError("Empty stack.")

        return self.items[-1]

    def push(self, newItem):
        if(self.isEmpty()):
            self.items.append((newItem,newItem))
        else:
            self.items.append((newItem, min(newItem, self.peek()[1])))

    def min(self):
        if(self.isEmpty()):
            return None
        return self.peek()[1]
