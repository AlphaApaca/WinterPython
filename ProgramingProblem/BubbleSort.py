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