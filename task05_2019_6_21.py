# 题目：假设某员工今年的年薪是30000元，年薪的年增长率6%。编写一个Java应用程序计算该员工10年后的年薪，并统计未来10年（从今年算起）总收入。
wages = 30000
money = 0
n = 1
while n <= 10:
    money += wages
    wages += wages * 0.06
    n += 1
print("该员工年薪为%s" % wages)
print("该员工一共收入为%s" % money)