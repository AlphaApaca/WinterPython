def swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

def bubbleSort(arr, k):
        for k in range(len(arr)):
            for j in range(len(arr)-1): 
                if (arr[j] > arr[j + 1]):
                    swap(arr, j, j + 1)

def printArray(arr):
    for i in range(len(arr)):
        if(i!=0):
            print(" ")
        print(arr[i])

str0 = input().split(" ")
n = int(str0[0])
k = int(str0[1])-1
arr = input().split(" ")

for i in range(len(arr)):
    arr[i] = int(arr[i])

bubbleSort(arr, k)
print(arr)
# printArray(arr)