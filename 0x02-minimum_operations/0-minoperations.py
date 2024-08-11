#!/usr/bin/python3
"""Calculates the minimum number of operations to achieve n characters in a string"""


def minOperations(n):
	"""Function that returns the minimum number of operations to 
		achieve n characters"""
	my_str = "H"
	count = 0

	while (len(my_str) < n):
			times = (len(my_str) // 2) + 1
			my_str.join('H' * times)
			count += 1
			if count > n:
				return 0
	return count

