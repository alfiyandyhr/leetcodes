class MyQueue():
	def __init__(self):
		self.array = []

	def push(self, x: int) -> None:
		self.array.append(x)

	def pop(self) -> int:
		return self.array.pop(0)

	def peek(self) -> int:
		return self.array[0]

	def empty(self) -> bool:
		try:
			if self.array[0]:
				return False
		except IndexError:
			return True

	def __str__(self):
		return f'{self.array}'

obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.pop()
print(obj.empty())