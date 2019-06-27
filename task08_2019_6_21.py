# 题目：分别使用for循环，while循环求1到100之间所有能被3整除的整数的和。
n = 1
sum = 0
while n <= 100:
    if n % 3 == 0:
        sum += n
    n += 1
print("总和为%s" % sum)
sum = 0
for i in range(1,101):
    if i % 3 == 0:
        sum += i
print("总和为%s" % sum)