# matrix_1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14 ,15 , 16]]
# matrix = [[1, 2, 5, 6]]

# row = len(matrix)
# col = len(matrix[0])

# row_start = 0
# row_end = row - 1
# col_start = 0
# col_end = col - 1

# # For a square matrix the no of rings will be (n + 1) // 2

# # Printing the first row
# while row_start <= row_end or col_start <= col_end:
#     idx = col_start
#     while idx <= col_end and idx >= 0 and idx <= col:
#         print(matrix[row_start][idx], end=" ")
#         idx += 1

#     # Right most column
#     idx = row_start + 1
#     while idx <= row_end and idx >= 0 and idx <= row:
#         print(matrix[idx][col_end], end=" ")
#         idx += 1

#     idx = col_end - 1
#     while idx >= col_start and idx >= 0 and idx <= col:
#         print(matrix[row_end][idx], end=" ")
#         idx -= 1

#     idx = row_end - 1
#     while idx >= row_start + 1 and idx >= 0 and idx <= row:
#         print(matrix[idx][col_start], end=" ")
#         idx -= 1

#     row_start += 1
#     col_end -= 1
#     row_end -= 1
#     col_start += 1


matrix = [[1,2,3,4], [4,5,6,7],[8,9,10,11], [1,2,3,4]]

rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], "row=", i, "col=",j, end=" ")
    print()

# x = 2
# matrix[0][2]
# matrix[1][2]
# matrix[2][2]
# ..
# matrix[row-1][2]

# for i in range(0, rows):
#     print(matrix[i][2], end=" ")


for i in range(0, cols):
    print(matrix[2][i])
