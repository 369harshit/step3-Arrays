def spiral_traversal(matrix, rows, cols):
    result = []
    top, bottom, left, right = 0, rows - 1, 0, cols - 1

    while top <= bottom and left <= right:
        # Traverse the top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse the right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse the bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Traverse the left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rows = 3
cols = 3
result = spiral_traversal(matrix, rows, cols)
print("Spiral traversal of the matrix:", result)
