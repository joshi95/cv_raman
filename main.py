t = int(input()) # 3
while t > 0:
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))

    # cnt = 0
    # for i in range(0, n):
    #     if A[i] in B:
    #         cnt += 1

    cnt = 0
    for i in range(0, n):
        for j in range(0, m):
            if A[i] == B[j]:
                cnt += 1

    if cnt == n:
        print("True")
    else:
        print("False")
    t -= 1