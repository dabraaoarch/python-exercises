import threading

fib_list = {}
cont = 0

def fib(num):
	if num == 0:
		return 0
	if num == 1 or num == 2:
		return 1
	return fib(num-1) + fib(num-2)
	#if not (num in fib_list.keys()):
	#	fib_list[num] = fib(num -1) + fib(num-2)
	
	#return fib_list[num]

def print_fib(num, arq, target):
	for i in range(0,target):
		print("{} - Exec: {} - Arq: {}".format(fib(num), i, arq))


if __name__ == "__main__":
	target = 15
	for arq in ["abc", "def", "ghi"]:
		trd1 = threading.Thread(target=print_fib(15, arq, target))
		trd2 = threading.Thread(target=print_fib(14, arq, target))
		
		trd1.start()
		trd2.start()
	