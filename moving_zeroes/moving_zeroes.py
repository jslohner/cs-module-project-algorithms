'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
	# loop through indices of array
	for i in range(len(arr)):
		# if num is 0 pop the num
		# and append it to the array
		if arr[i] == 0:
			arr.append(arr.pop(i))
		# if num isn't 0 pop the num and insert
		# it at the beginning of the array
		else:
			arr.insert(0, arr.pop(i))
	# return mutated array
	return arr

if __name__ == '__main__':
	# Use the main function here to test out your implementation
	arr = [0, 3, 1, 0, -2]

	print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
