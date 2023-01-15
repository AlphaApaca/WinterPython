import math

def change(cent):
    fd = cent/30.48
    f = int(math.floor(fd))
    d = int(math.floor((fd - f) * 12))
    print("{} {}".format(f,d))

cent = int(input())
change(cent)