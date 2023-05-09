class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        spiralFill(matrix, 0, len(matrix) - 1, 0, len(matrix[0]) - 1, spiral)

        return spiral


def spiralFill(array, startrow, endrow, startcol, endcol, spiral):
    if startrow > endrow or startcol > endcol:
        return

    for col in range(startcol, endcol + 1):
        spiral.append(array[startrow][col])

    for row in range(startrow + 1, endrow + 1):
        spiral.append(array[row][endcol])

    for col in reversed(range(startcol, endcol)):
        if startcol == endcol or startrow == endrow:
            break
        spiral.append(array[endrow][col])

    for row in reversed(range(startrow + 1, endrow)):
        if startcol == endcol or startrow == endrow:
            break
        spiral.append(array[row][startcol])


    spiralFill(array, startrow + 1, endrow - 1, startcol + 1, endcol - 1, spiral)