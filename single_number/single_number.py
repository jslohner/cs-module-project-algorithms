'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
	# create memory storage
	mem = {}
	# loop through array
	for num in arr:
		# if num is already in
		# mem add 1 to it's value
		if num in mem:
			mem[num] += 1
		# otherwise initialize number
		# with value of 1
		else:
			mem[num] = 1
	# loop through mem
	for key in mem:
		# if key has value of 1
		# return that key
		if mem[key] == 1:
			return key

if __name__ == '__main__':
	# Use the main function to test your implementation
	arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

	print(f"The odd-number-out is {single_number(arr)}")
