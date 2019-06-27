# 题目：判断一个随机整数是否能被5和6同时整除（打印能被5和6整除），
# 或只能被5整除（打印能被5整除），或只能被6整除，（打印能被6整除），
# 不能被5或6整除，（打印不能被5或6整除）
import random

random_number = random.randint(1, 10000000)
print("这个数是%s" % random_number)
if random_number % 5 == 0:
    if random_number % 6 == 0:
        print("能被5和6整除")
    else:
        print("不能被5和6整除")
else:
    print("不能被5和6整除")