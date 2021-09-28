import math

def binarySearch(itens, item):
	arranged = mergeSort(itens)
	if item > arranged[len(arranged)-1] or item < arranged[0]:
		return False
	return binaryLoop(arranged, item, 0, len(itens)-1)

def binaryLoop(itens, item, start, end):
	if end == start and itens[end] != item:
		return False
	middle = math.floor(((end-start)/2) + start)
	if item == itens[middle]:
		return middle
	if item < itens[middle]:
		return binaryLoop(itens, item, start, middle)
	return binaryLoop(itens, item, middle+1, end)
	
	
def exchangePlace(arr, start_place, end_place):
	if len(arr) == 0 or start_place == end_place:
		return arr
	aux = arr[end_place]
	arr[end_place] = arr[start_place]
	arr[start_place] = aux
	return arr

def mergeSort(arr, start=None, end=None):
	if start == None:
		start = 0
	if end == None:
		end = len(arr) - 1
	if len(arr) == 0:
		return []
	middle = (end - start) // 2 + start	
	if start >= end:
		return arr		
	if end == start+1:
		if arr[end] < arr[start]:
			arr = exchangePlace(arr, start, end)
		return arr

	arr = mergeSort(arr, middle, end)
	arr = mergeSort(arr, start, middle-1)
	
	i = start
	j = middle
	ordered = []
	while i < middle and j <= end:
		if arr[i] > arr[j]:
			ordered = ordered + [arr[j]]
			j = j + 1
		else:
			ordered = ordered + [arr[i]]
			i = i + 1
	arr = arr[0:start] + ordered + arr[i:middle] + arr[j:end+1] + arr[end+1:]
	return arr	
	
if __name__=="__main__":
	print(binarySearch([0,5,6,8,7,1,2,5,85,95,24], 24))