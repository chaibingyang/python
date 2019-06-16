distance = 363300000000
thickness = 0.088
n = 0
while thickness <= distance:
    thickness = thickness*2
    n += 1
print("要上月球，我们应该折%d次" % n)
print(thickness)
