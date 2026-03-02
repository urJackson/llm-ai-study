# 猜数字
import random
rn = random.randint(1,100)
if rn % 2 == 0:
    print("提示：————该数字是偶数————")
else:
    print("提示：————该数字是奇数————")
while True:
    num = int(input("请猜出该数字："))
    if num == rn:
        print("恭喜你猜对了！")
        break
    elif num > rn:
        print("你猜的数字太大了，请再猜一遍吧。")
    else:
        print("你猜的数字太小了，请再猜一遍吧。")