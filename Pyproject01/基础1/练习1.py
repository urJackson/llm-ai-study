# 需求1:将1-1000之间(含1000)所有的5的倍数的数字累加起来。
# 需求2:统计字符串"akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"字符串中有多少个a和k。
sum = 0
for i in range(1,1001):  # 更高效：range(5,1001,5)
    if i % 5 == 0:
        sum += i
print(sum)

ksum , asum = 0 , 0
str = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
for i in str:
    if i == "a":
        asum += 1
    elif i == "k":
        ksum += 1
print(f"a总共有{asum}个, k总共有{ksum}个")