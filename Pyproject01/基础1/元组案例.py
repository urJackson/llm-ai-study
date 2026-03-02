# 根据提供的学生成绩单，完成如下需求:
from sys import maxsize

students = (
    ("S001","王林",85,92,78),
    ("S002","李慕婉",92,88,95),
    ("S003","十三",78,85,82),
    ("S004","曾牛",88,79,91),
    ("S005","周轶",95,96,89),
    ("S006","王卓",76,82,77),
    ("S007","红蝶",89,91,94),
    ("S008","徐立国",75,69,82),
    ("S009","许木",86,89,98),
    ("S010","遁天",66,59,72),
)
# 1.计算每个学生的总分、各科平均分，然后一并输出出来。
# 方法一
# print("学号 \t 姓名 \t 语文 \t 数学 \t 英语 \t 总分 \t 平均分")
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")

# 方法二
for id,name,Chinese,Math,English in students:
    total = Chinese + Math + English
    avg = total / 3
    print(f"{id} \t {name} \t {Chinese} \t {Math} \t {English} \t {total} \t {avg:.1f}")
print()
# 2.统计各科成绩的最低分、最高分、平均分，并输出。
chinese = [s[2] for s in students]
math = [s[3] for s in students]
english = [s[4] for s in students]
print(f"语文de最高分：{max(chinese)},最低分：{min(chinese)},平均分为{sum(chinese)/len(chinese)}")
print(f"数学de最高分：{max(math)},最低分：{min(math)},平均分为{sum(math)/len(math)}")
print(f"英语de最高分：{max(english)},最低分：{min(english)},平均分为{sum(english)/len(english)}")

print()
# 3.查找成绩优秀(平均分大于90)的学生，并输出。
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    if avg >= 90:
        print(f"{s[1]}成绩优秀")