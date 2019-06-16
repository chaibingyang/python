n = int(input("请输入需要求阶乘的值："))
count = 1
sum = 1
while count <= n:
    sum = sum * count
    count = count + 1
print(sum)
