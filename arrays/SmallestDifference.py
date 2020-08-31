# Smallest Difference
#
# Write a function that takes in two non-empty arrays of integers, find
# the pair of numbers (one from each array) whose absolute difference
# is closest to zero, and returns an array containing these two numbers,
# with the number from the first array in the first position.
#
# You can assume that there will only be one pair of number with the
# smallest difference.
#
# Sample Input
#   arrayOne = [-1, 5, 10, 20, 28, 3]
#   arrayTwo = [26, 134, 135, 15, 17]
#
# Sample Output
#   arrayOne = [28, 26]
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    pOne = 0
    pTwo = 0
    diff = None
    res = None
    while pOne < len(arrayOne) and pTwo < len(arrayTwo):
        if diff == None or diff > abs(arrayOne[pOne] - arrayTwo[pTwo]):
            diff = abs(arrayOne[pOne] - arrayTwo[pTwo])
            res = [arrayOne[pOne], arrayTwo[pTwo]]
        if arrayOne[pOne] == arrayTwo[pTwo]:
            return [arrayOne[pOne], arrayTwo[pTwo]]
        elif arrayOne[pOne] < arrayTwo[pTwo]:
            pOne += 1
        else:
            pTwo += 1
    return res


