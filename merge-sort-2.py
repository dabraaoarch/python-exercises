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
	print(mergeSort([1,5,7,10,2,8,5,4,3,6,8]))