# 猜数字
import random
rn = random.randint(1,10)
if rn % 2 == 0:
    print("提示：————该数字是偶数————")
else:
    print("提示：————该数字是奇数————")
while True:
    num = int(input("请猜出该数字："))
    if num == rn:
        print("恭喜你猜对了！")
        break
    else:
        print("你猜错了，请再猜一遍吧。")