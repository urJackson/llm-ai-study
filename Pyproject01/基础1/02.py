# 嵌套循环：打印长度为m，宽度为n的*长方形

# m = int(input("请输入长度："))
# n = int(input("请输入宽度："))
#
# for i in range(m):
#     for j in range(n):
#         print("*",end=" ")
#     print()

# 打印99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} x {i} = {i*j}",end="\t")
    print()

