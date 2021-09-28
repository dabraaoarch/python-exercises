def mapArray(list_to_map):
	mapped_object = {}
	for index in range(0, len(list_to_map)):
		list_item = list_to_map[index] 
		if list_item in mapped_object.keys():
			mapped_object[list_item] += [index]
		else:
			mapped_object[list_item] = [index]
	return mapped_object
	
def countFrequency(itens_list, item):
	mapped_list = mapArray(itens_list)
	return len(mapped_list[item]) if item in mapped_list.keys() else False
	
if __name__ == "__main__":
	print(countFrequency("Daniel Abraao", "a"))
