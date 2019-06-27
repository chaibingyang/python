# 题目：试写一个三位数，从小到大排列，然后再从大到小排列。
number = int(input("请输入一个不多于5位的正整数:"))
if 1 <= number <= 99999:
    if number // 10000 != 0:
        print("这是五位数")
    elif number // 1000 != 0:
        print("这是四位数")
    elif number // 100 != 0:
        print("这是三位数")
    elif number // 10 != 0:
        print("这是二位数")
    else:
        print("这是1位数")
    for letter in str(number):
        print(letter)
else:
    print("输入有误")