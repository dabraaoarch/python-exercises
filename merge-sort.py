def exchangePlace(arr, start_place, end_place):
	if len(arr) == 0 or start_place == end_place:
		return arr
	aux = arr[end_place]
	arr[end_place] = arr[start_place]
	arr[start_place] = aux
	return arr
	
def merge(array_to_merge, start, middle, end):
	left = array_to_merge[start:middle]
	right = array_to_merge[middle:end+1]
	bigger = (array_to_merge[middle] if array_to_merge[middle] > array_to_merge[end] else array_to_merge[end]) + 1
	count_start = start
	count_left = count_right = 0
	left += [bigger]
	right += [bigger]
	print("{} - {}".format(left, right))
	'''while left[count_left] != bigger and right[count_right] != bigger:
		if left[count_left] < right[count_right]:
			array_to_merge[count_start] = left[count_left]
			count_left += 1
		else:
			array_to_merge[count_start] = right[count_right]
			count_right += 1
		count_start += 1'''
	return array_to_merge
	
def mergeSort(arr, start=None, end=None):
	start = 0 if start == None else start
	end = (len(arr) - 1) if end == None else end
	
	if end-start <= 1:
		return arr
	middle = (end - start) // 2 + start	
	
	arr = mergeSort(arr, middle, end)
	arr = mergeSort(arr, start, middle-1)

	print(merge(arr, start, middle, end))
	'''left = arr[start:middle]
	right = arr[middle+1:end]
	#input("{} - {} - {} - {}".format(left, right, end, arr))
	bigger = (arr[middle] if arr[middle] > arr[end] else arr[end]) + 1 
	count_start = start
	count_left = count_right = 0
	left += [bigger]
	right += [bigger]
	while left[count_left] != bigger and right[count_right] != bigger:
		if left[count_left] > right[count_right]:
			arr[count_start] = left[count_left]
			count_left += 1
		else:
			arr[count_start] = right[count_right]
			count_right += 1
		count_start += 1
	'''
	return arr	

#print([1,5,7,10,2,3,8,5,4,3,6,8])
print(mergeSort([1,5,7,10,2,8,5,4,3,6,8]))
			

		 	 