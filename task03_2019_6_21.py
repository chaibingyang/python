# 题目：试写一个三位数，从小到大排列，然后再从大到小排列。
number = int(input("请输入一个三位数:"))
if 100 <= number <= 999:
    a = number // 100
    b = number % 100
    b = b // 10
    c = number % 10
    if a > b:
        d = b
        e = a
    else:
        d = a
        e = b
    if c > e:
        print(c, e, d)
        print(d, e, c)
    else:
        if c > d:
            print(e, c, d)
            print(d, c, e)
        else:
            print(e, d, c)
            print(c, d, e)
else:
    print("输入有误")