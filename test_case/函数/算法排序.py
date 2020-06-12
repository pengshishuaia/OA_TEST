'''
冒泡排序
思路:（从小到大排序）
从第一个数字和后一个数字进行比较，比较之后，（从小到大排序），如果后面的数字比前面的数字小，进行位置的交换，如果后面
的数字比前面的大，则进行位置的交换，然后第二个位置的数字在于后面的数字进行比较，以此类推
选择排序
思路：（从小到大排序）
拿第一个数据和后面的数字分别比较，如果比第一个比较的数字小，则进行位置交换，然后在拿该数和后面的数进行比较
'''

arr = [6, 3, 7, 9, 2, 5, 4, 28, 8, 90, 100]


# 选择排序算法
def selection_sort(arr):
    for index in range(len(arr)):
        for j in range(index + 1, len(arr)):
            if arr[index] > arr[j]:
                arr[index], arr[j] = arr[j], arr[index]


selection_sort(arr)
print(arr)


# 冒泡排序算法
def bubble_sort(arr):
    for index in range(len(arr)):
        for i in range(index + 1, len(arr)):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]


bubble_sort(arr)
print(arr)
