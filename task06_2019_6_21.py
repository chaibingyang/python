# 题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个。
# 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一
# 半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。程序分析：
# 采取逆向思维的方法，从后往前推断。
number = 1
day = 10
while day > 1:
    number = (number + 1) * 2
    day -= 1
print("桃总数是%s" % number)
