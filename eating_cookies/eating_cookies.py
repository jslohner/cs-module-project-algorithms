'''
Input: an integer
Returns: an integer
'''
# import sys
# sys.setrecursionlimit(10 ** 6)
def eating_cookies(n, mem):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	elif n in mem:
		return mem[n]
	else:
		mem[n] = eating_cookies((n - 1), mem) + eating_cookies((n - 2), mem) + eating_cookies((n - 3), mem)
		return mem[n]

if __name__ == "__main__":
	# Use the main function here to test out your implementation
	num_cookies = 500

	print(f"There are {eating_cookies(num_cookies, {})} ways for Cookie Monster to eat {num_cookies} cookies")
