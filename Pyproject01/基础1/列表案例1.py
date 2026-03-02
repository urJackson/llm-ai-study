# 将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值、最大值和平均值。

s = []
for i in range(1,11):
    num = int(input(f"请输入第{i}个数字："))
    s.append(num)
s.sort()
print(s)
print(f"列表s的最小值为{min(s)}，列表s的最大值为{s[-1]}，列表s的平均值为{sum(s)/ len(s)}")