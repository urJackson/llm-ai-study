# 合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)。

num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

num_list = num_list1 + num_list2
num_list.sort()
print(num_list)
new_list = []
for num in num_list:
    if num not in new_list:
        new_list.append(num)
print(f"去重后：{new_list}")