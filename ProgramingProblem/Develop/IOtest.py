import time


# f = open("C:/Users/26847/Desktop/repository.txt", "r", encoding="UTF-8")
# print(type(f))

# print(f"f is: {f.read(10)}")
# print(f"the rest of f is: {f.read()}")

print("--------------------------------")
# lines = f.readlines()
# print(type(lines))
# print(lines)
print("--------------------------------")
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(line1)
# print(line2)
# print(line3)
print("--------------------------------")
# for line in f:
#    print(f"The repository of Alphalpaca is: {line}")
# f.close()
# 解除文件占用
# time.sleep(10000)

with open("C:/Users/26847/Desktop/repository.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"The repository of Alphalpaca is: {line}")