def flippingMatrix(matrix):
    
    n = len(matrix)
    result = 0

    for i in range(n//2):
        for j in range(n//2):
            result += max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
    
    return result


matrix = [
    [12, 7, 1, 19, 5, 10],
    [3, 14, 20, 4, 17, 8], #i = j =1 
    [22, 16, 9, 6, 11, 13],
    [24, 15, 2, 18, 21, 25],
    [23, 26, 30, 29, 27, 28],
    [35, 32, 31, 33, 34, 36]
]

result = flippingMatrix(matrix)

print(result)