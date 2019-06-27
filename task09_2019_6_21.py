# 题目： 编写一个程序，找出大于200的最小的质数
number = 200
while True:
    a = True
    i = 2
    while i < number:
        if number % i == 0:
            a = False
            break
        i += 1
    if a == True:
        print("大于200的最小的质数%d" % number)
        break
    number = number + 1
