
def judge(a):
    a = int(a)
    if a / 100 >= 1:
        print(a)
    elif a / 10 >= 1:
        print("0{}".format(a))
    elif a / 10 == 0:
        print("00{}".format(a))

str = input().split(" ")
time = int(str[0])
nmin = int(str[1])

# p = int(time % 100)
# y = int(next % 60)

if (time % 100 + nmin % 60) >= 0:
            a = ((time / 100 + (nmin / 60)) + (time % 100 + nmin % 60) / 60) * 100 + (time % 100 + nmin % 60) % 60
            judge(a)
else:
    a = ((time / 100 + (nmin / 60)) + ((time % 100 + nmin % 60) / 60 - 1)) * 100 + 60 + (time % 100 + nmin % 60)
    judge(a)
# 离谱的事情出现了，怎么会有相同的运算式不一样的结果的
# 明天早上起来再搞
# 直接一个晚的安