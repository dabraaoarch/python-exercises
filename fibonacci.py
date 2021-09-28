fib_list = {}

def fib(num):
	if num < 2:
		return num
	#return fib(num-1) + fib(num-2)
	if not (num in fib_list.keys()):
		fib_list[num] = fib(num -1) + fib(num-2)
	
	return fib_list[num]
	
if __name__ == "__main__":
	print(fib(100))
	print(fib(200))
	print(fib(350))