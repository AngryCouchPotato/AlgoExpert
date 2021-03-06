# Move Element To End
#
# You're given an array of integers and an integer. Write a function
# that moves all instances of that integer in the array to the end of
# the array and returns the array.
#
# The function should perform this in place i.e., it should mutate the input array)
# and doesn't need to maintain the order of the other integers.
#
# Sample Input
#   array = [2, 1, 2, 2, 2, 3, 4, 2]
#   toMove = 2
#
# SampleOutput
#   [1, 3, 4, 2, 2, 2, 2, 2]
def moveElementToEnd(array, toMove):
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] == toMove:
            while left < right and array[right] == toMove:
                right -= 1
            array[left], array[right] = array[right], array[left]
        left += 1
    return array
