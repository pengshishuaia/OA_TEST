'''

'''


def fun():
    n = 100
    list1 = [2, 3, 9, 5, 4]
    def fun1():
        nonlocal n
        for index,values in enumerate(list1):
            print(index,values)
            list1[index] =values + 10
        print(list1)
        list1.sort()
        print(list1)
        n = n+100
        print(n)
    fun1()

fun()