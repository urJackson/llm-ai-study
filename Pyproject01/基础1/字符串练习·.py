# 1.输入一个字符串，判断该字符串是否是回文(两边对称)  e.g.黄山落叶松叶落山黄 / 上海自来水来自海上


# 2.将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来。

# poem = input("请输入诗句：")
# words = poem[::-1]
# if words == poem:
#     print("YES")
# else:
#     print("NO")


str = input("请输入：")
new_str = str[::-1]
last = new_str.upper().split()
print(last)