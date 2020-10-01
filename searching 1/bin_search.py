A = [1, 2, 3, 4, 5, 6, 77, 88, 99]
x = 77
# First condition is satisfied the array is sorted so we can apply binary search

def binary_search(A, x):
    left = 0
    right = len(A) - 1

    while left <= right:
        mid = (left + right) // 2

        if A[mid] == x:
            return True
        elif A[mid] > x:
            right = mid - 1
        elif A[mid] < x:
            left = mid + 1
    
    return False

print(binary_search(A, 103))