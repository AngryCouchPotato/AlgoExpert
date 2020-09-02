# Longest Peak
#
# Write a function that takes in an array of integers and returns
# the length of the longest peak in the array.
#
# A peak is defined as adjacent integers in the array that are strictly
# increasing until they reach a tip ( the highest value in the peak),
# at which point they become strictly decreasing. At least three integers
# are required to form a peak.
# For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10
# don't and neither do the integers 1, 2, 2, 0. Similarly, the integers 1, 2, 3
# don't form a peak because there aren't any strictly decreasing integers after the 3.
#
# Sample Input
#   array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
# Sample Output
#   6 // 0, 10, 6, 5, -1, -3
#
def longestPeak(array):
    if array == None or len(array) < 3:
        return 0

    peaks = []
    for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            peaks.append(i)

    maxLength = 0
    if len(peaks) == 0:
        return maxLength

    for p in peaks:
        curLength = 1
        l = p
        r = p
        while l > 0 and array[l - 1] < array[l]:
            curLength += 1
            l -= 1
        while r < (len(array) - 1) and array[r] > array[r + 1]:
            curLength += 1
            r += 1
        if curLength > maxLength:
            maxLength = curLength

    return maxLength