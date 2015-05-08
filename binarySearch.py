def binarysearch(array, begin = 0,end = len(arr), prevPos = 0):
	if (arr[begin] == key):
		return True
	elif(arr[begin] > key):
		return binarySearch(arr, prevPos,begin,prevPos)
	elif(arr[begin] < key):
		prevPos = begin
		begin = begin + (end - begin)/2
		return binarySearch(arr, begin,end, prevPos)
	else:
		return False

