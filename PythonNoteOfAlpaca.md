# Python

## 0. pta题带知识点

### 0.1 ToFootInch

```python
import math

def change(cent):
    fd = cent/30.48
    f = int(math.floor(fd))
    d = int(math.floor((fd - f) * 12))
    print("{} {}".format(f,d))

cent = int(input())
change(cent)
```

#### 0.1.1 Python取整

+ 向上取整：**math.ceil()**
+ 四舍五入：**round()**
+ 向下取整：**math.floor()**
+ 向0取整：**int()**
+ 整除：**"//"**

```python
(-1) // 2 # -0.5
>>> -1
```

#### 0.1.2 Python中input

默认是string类型，如需要其他类型需要进行转换

#### 0.1.3 format函数

Python中如果需要在打印里穿插进函数，需要用.format(a,b,c,...)来进行插入对应的"{}"位点(占位符)

```python
# 怎么会有人傻乎乎的随手写的本地邮箱导致github绿不了啊啊啊啊啊
# 尚硅谷我恨你
```

### 0.2 ThenWhatTime

```python
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

if (time % 100 + nmin % 60) >= 0:
            a = ((time // 100 + (nmin // 60)) + (time % 100 + nmin % 60) // 60) * 100 + (time % 100 + nmin % 60) % 60
            judge(a)
else:
    a = ((time // 100 + (nmin // 60)) + ((time % 100 + nmin % 60) // 60 - 1)) * 100 + 60 + (time % 100 + nmin % 60)
    judge(a)
```



在python中，int的/（除法）和//（整除）是不同的，python中/会返回小数，而//

返回int

### 0.3 BubbleSort

```python
def swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

def bubbleSort(arr, k):
        for k in arr:
            for j in arr: 
                if (arr[j] > arr[j + 1]):
                    swap(arr, j, j + 1)

def printArray(arr):
    for i in arr:
        if(i!=0):
            print(" ")
        print(arr[i])

str0 = input().split(" +")
n = int(str0[0])
k = int(str0[1])-1
arr = int(input().split(" +"))
# 读取数据还有点问题
bubbleSort(arr, k)
printArray(arr)
```

