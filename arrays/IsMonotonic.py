# Monotonic Array
#
# Write a function that takes in an array of integers and returns a
# boolean representing whether the array is monotonic.
#
# An array is said to be monotonic if its elements, from left to right,
# are entirely non-increasing or entirely non-decreasing.
#
# Note that empty arrays and arrays of one element are monotonic.
#
# Sample Input
#   array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
# Sample Output
#   true
#
def isMonotonic(array):
    if array == None or len(array) <= 2:
        return True

    direction = array[1] - array[0]

    i = 2
    while i < len(array):
        if direction > 0:
            if array[i] < array[i - 1]:
                return False
        elif direction < 0:
            if array[i] > array[i - 1]:
                return False
        else:
            direction = array[i] - array[i - 1]
        i += 1
    return True