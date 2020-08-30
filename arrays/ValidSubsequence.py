# Validate subsequence
#
# Given two non-empty arrays of integers, write a function that determines whether the second array
# is a subsequence of the first one.
#
# A subsequence of an array is set of numbers that aren't necessarily adjacent in the array but that
# are in the same order as they appear in the array. Fo instance, the numbers [1,3,4] form a subsequence
# of the array [1,2,3,4], and so do the numbers [2,4]. Note that a single number in an array and the array
# itself are both valid subsequence of the array.
#
# Sample Input:
# 	array = [2, 1, 22, 25, 6, -1, 8, 10]
# 	sequence = [1, 6, -1, 10]
# Sample Output
#	true
#
def isValidSubsequence(array, sequence):
    if array == None or len(array) == 0:
		return []
	i = 0
	j = 0
	res = False
	while i < len(sequence):
		res = False
		digit = sequence[i]
		while j < len(array):
			if array[j] == digit:
				res = True
				j += 1
				break
			j += 1
		if res == False:
			return res
		i += 1
	return res
