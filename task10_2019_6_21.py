# 题目：由命令行输入一个4位整数，求将该数反转以后的数，如原数为1234，反转后的数位4321
number = int(input("请输入一个4位整数："))
a = number // 1000
b = number % 1000
b = b // 100
c = number % 100
c = c // 10
d = number % 10
print(d*1000+c*100+b*10+a)