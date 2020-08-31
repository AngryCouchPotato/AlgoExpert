# Spiral Traverse
#
# Write a function that takes in an n x m two-dimensional array
# (that can be square-shaped when n==m) and returns a one-dimensional
# array of all the array's elements in spiral order.
#
# Spiral order starts at the top left corner of the two-dimensional array,
# goes to the right, and proceeds in a spiral pattern all the way until every
# elememt has been visited.
#
# Sample Input:
#   array = [
#       [1,2,3,4],
#       [12,13,14,5],
#       [11,16,15,6],
#       [10,9,8,7],
#   ]
#
# Sample Output
#   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
#
def spiralTraverse(array):
    if array == None or len(array) == 0:
        return []
    res = []
    topRow, bottomRow = 0, len(array) - 1
    leftColumn, rightColumn = 0, len(array[0]) - 1
    while leftColumn <= rightColumn and topRow <= bottomRow:
        i = leftColumn
        while i <= rightColumn:
            res.append(array[topRow][i])
            i += 1

        i = topRow + 1
        while i <= bottomRow:
            res.append(array[i][rightColumn])
            i += 1

        i = rightColumn - 1
        while i >= leftColumn:
            if topRow == bottomRow:
                break
            res.append(array[bottomRow][i])
            i -= 1

        i = bottomRow - 1
        while i > topRow:
            if leftColumn == rightColumn:
                break
            res.append(array[i][leftColumn])
            i -= 1

        topRow += 1
        bottomRow -= 1
        rightColumn -= 1
        leftColumn += 1

    return res