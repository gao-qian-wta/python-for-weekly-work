"""

输入任意学生数的各科成绩信息并计算相关分数,若一名学生成绩信息输入不完整，则忽略该学生成绩

"""

# 循环录入学生成绩
grade = []
major = ["语文成绩", "数学成绩", "外语成绩"]
majornum = len(major)
a = 0 #初始计数
while True:
    grade.append([])
    for i in range(0, majornum):
        x = input("请输入第" + str(a+1) + "个学生的" + major[i] + "    输入exit退出")
        if x == "exit":
            break
        grade[a].append(x)
    if x == "exit":
        break
    a += 1

grade.pop()


# 定义计算函数
def sum_s(num_location):
    return sum(int(ii[num_location]) for ii in grade)

def avg_a(num_location):
    return (sum(int(ii[num_location]) for ii in grade) / a)

def max_m(num_location):
    return max(int(ii[num_location]) for ii in grade)

def min_m(num_location):
    return min(int(ii[num_location]) for ii in grade)


# 计算结果输出
print("语文总分%.2f，平均分%.2f，最高分%.2f，最低分%.2f" % (sum_s(0), avg_a(0), max_m(0), min_m(0)))
print("数学总分%.2f，平均分%.2f，最高分%.2f，最低分%.2f" % (sum_s(1), avg_a(1), max_m(1), min_m(1)))
print("外语总分%.2f，平均分%.2f，最高分%.2f，最低分%.2f" % (sum_s(2), avg_a(2), max_m(2), min_m(2)))
