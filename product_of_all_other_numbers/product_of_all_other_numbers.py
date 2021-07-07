'''
Input: a List of integers
Returns: a List of integers
'''
# import math
def product_of_all_other_numbers(arr):
	# initialize return array
	rtn_arr = []
	# loop through indices of array
	for i in range(len(arr)):
		# create new array of all numbers
		# that aren't the current number
		x = [arr[j] for j in range(len(arr)) if j != i]
		# get product
		product = 1
		for num in x:
			product *= num
		# append product to return array
		rtn_arr.append(product)
		# rtn_arr.append(math.prod(x))
	# return array
	return rtn_arr


if __name__ == '__main__':
	# Use the main function to test your implementation
	# arr = [1, 2, 3, 4, 5]
	arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

	print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
