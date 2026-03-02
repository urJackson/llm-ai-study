# 1.生成1-20的平方列表。
# 2.从如下数学列表中提取所有偶数，并计算其平方，组成一个新的列表。

#method1
list = []
for i in range(1,21):
    list.append(i*i)
print(list)

#method2
list0 = []
list0 = [i**2 for i in range(1,21)]
print(list0)


list1 = [19, 23, 54, 64, 87, 20, 109, 232, 123, 43, 26, 55, 72]
# list2 = []
# for i in list1:
#     if i % 2 == 0:
#         list2.append(i*i)

# method3
list2 = [i**2 for i in list1 if i%2 == 0]
print(list2)