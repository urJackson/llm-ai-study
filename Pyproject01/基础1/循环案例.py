# self
# admin = input("请输入用户名：")
# passward = input("请输入密码：")
# while (admin == "" or passward == ""):
#     print("用户名和密码不能为空！请重新输入。")
#     admin = input("请输入用户名：")
#     passward = input("请输入密码：")
# else:
#     while ((admin != "admin" or passward != "666888") and (admin != "zhangsan" or passward != "123456") and (
#             admin != "taoge" and passward != "888666")):
#         print("用户名或密码错误!请重新输入。")
#         admin = input("请输入用户名：")
#         passward = input("请输入密码：")
#     else:
#         print("登陆成功，进入B站首页~")


# answer
while True:
    admin = input("请输入用户名：")
    passward = input("请输入密码：")
    # 空值判断
    if admin == "" or passward == "":
        print("用户名或密码为空，请重新输入！")
        continue
    # 校验
    if admin == "admin" and passward == "123123":
        print("登陆成功,进入B站首页~")
        break
    elif admin == "zhangsan" and passward == "666666":
        print("登陆成功,进入B站首页~")
        break
    elif admin == "jackson" and passward == "888888":
        print("登陆成功,进入B站首页~")
        break
    else:
        print("用户名或密码错误，请重新输入！")