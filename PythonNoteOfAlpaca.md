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
+ 整除：**"\\\\"**

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
```

