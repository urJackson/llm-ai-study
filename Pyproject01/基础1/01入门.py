base = 10000
now = 0
Rkeyword = "123"
Ikeyword = input("请输入密码：")
while Rkeyword != Ikeyword:
    print("密码错误！请重新输入。")
    Ikeyword = input("请输入密码：")
print("密码正确！！！")
money = int(input("请输入取款金额："))
while money>base:
    print("余额不足！请重新输入。")
    money = int(input("请输入取款金额："))
else:
    print(f"取款成功！！！\n剩余余额：{base-money}")
