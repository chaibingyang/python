# 题目：编写一个程序，计算邮局汇款的汇费。如果汇款金额小于100元，汇费为一元，如果金额在100元与5000元之间，按1%收取汇费，如果金额大于5000元，汇费为50元。
money = int(input("请输入汇款金额："))
if 0 < money < 100:
    charge = 1
elif 100 <= money <= 5000:
    charge = money * 0.01
elif money >= 5000:
    charge = 50
else:
    print("输入有误")
print("收取汇费%s" % charge)
