'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
	# initialize rtn list
	rtn = []
	# initialize i1 and i2
	i1 = 0
	i2 = k - 1
	# while window indices are in bounds of the array
	while i2 != (len(nums)):
		# append max number of window to rtn list
		# rtn.append(max(nums[i1:(i2 + 1)]))
		# another way to append max of window to rtn list
		rtn.append(sorted(nums[i1:(i2 + 1)])[-1])
		# increment i1 and i2
		i1 += 1
		i2 += 1
	# return list of max numbers
	return rtn

if __name__ == '__main__':
	# Use the main function here to test out your implementation
	arr = [1, 3, -1, -3, 5, 3, 6, 7]
	k = 3

	print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
