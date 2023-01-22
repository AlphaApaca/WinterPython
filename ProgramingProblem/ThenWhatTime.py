
def judge(a):
    a = int(a)
    if a / 100 >= 1:
        print(a)
    elif a / 10 >= 1:
        print("0{}".format(a))
    elif a / 10 == 0:
        print("00{}".format(a))

# def pt(time, nmin):
#     print('\n')
#     print(time // 100 + (nmin // 60))
#     print('\n')
#     print((time % 100 + nmin % 60) // 60)
#     print('\n')
#     print(time % 100 + nmin % 60)

str = input().split(" ")
time = int(str[0])
nmin = int(str[1])

if (time % 100 + nmin % 60) >= 0:
            a = ((time // 100 + (nmin // 60)) + (time % 100 + nmin % 60) // 60) * 100 + (time % 100 + nmin % 60) % 60
            judge(a)
#           pt(time, nmin)
else:
    a = ((time // 100 + (nmin // 60)) + ((time % 100 + nmin % 60) // 60 - 1)) * 100 + 60 + (time % 100 + nmin % 60)
    judge(a)
#   pt(time, nmin)