# for i in range(0, 5): # 0 1 2 3
#     for j in range(0, 5):
#         print(i, j)
#         if i >= 3:
#             break
#     print("")

# # 0 0 0 1 0 2 0 3
# # 1 0 1 1 1 2 1 3
# # 2 0 2 1 2 2 2 3
# # 3 0 3 1 3 2 3 3

for i in range(0, 5):
    for j in range(0, 5):
        if j >= 3:
            continue
        print("daf")
        print("j=",j)
    print("i=", i)


