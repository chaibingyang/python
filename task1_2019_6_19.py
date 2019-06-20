height = float(input("请输入篮球的初始高度:"))
n = 0
distance = height
while n < 10:
    distance += height
    height /= 2
    n += 1
distance -= height*2
print('蓝球经过的距离%s米' % distance)
print('第十次蓝球弹跳高度%s米'% height)