count = 1
sum = 1
n = 0
while count <= 5:
    sum = sum * count
    count = count + 1
n += sum
count = 1
sum = 1
while count <= 4:
    sum = sum * count
    count = count + 1
n += sum
count = 1
sum = 1
while count <= 3:
    sum = sum * count
    count = count + 1
n += sum
count = 1
sum = 1
while count <= 2:
    sum = sum * count
    count = count + 1
n += sum
count = 1
sum = 1
while count <= 1:
    sum = sum * count
    count = count + 1
n += sum
print("1!+2!+3!+4!+5!=%s" % n)