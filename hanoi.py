
	
def torreHanoi(number, index, destination):
	positions = "ABC"
	if number == 1:
		print("move disk from {} to {}".format(index,destination))
		return True
		
	available = positions.replace(index,"")
	available = available.replace(destination,"")
	torreHanoi(number-1, index,available)
	print("move disk from {} to {}".format(index,destination))
	torreHanoi(number-1, available, destination)
	
if __name__ == "__main__":
	torreHanoi(11, "A", "B")