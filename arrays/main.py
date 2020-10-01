# def solve():
#     A = [4, 6, 1, 2, 3, 44]
#     target = 9

#     A.sort()  # nlogn
#     left = 0
#     right = len(A) - 1

#     while left < right:
#         sum = A[left] + A[right]
#         if sum == target:
#             return True
#         elif sum < target:
#             left += 1
#         else:
#             right -= 1
#     return False

# # o(n) + o(nlogn)
# # o(nlogn)


n = 3
matrix1 = [[0 for _ in range(n)] for _ in range(n)]
matrix1[2][1] = 100
matrix1[5][1] = 100
# matrix1 = [[0,0,0],[0,0,0],[0,0,0]]

print(matrix1)