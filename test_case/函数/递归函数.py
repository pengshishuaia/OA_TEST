'''
递归函数：函数自己调用自己
特点：
1，递归函数必须有一个终点
2，通常都会有一个入口
用递归过程定义的函数, 称为递归函数, 例如连加,连乘及阶乘等. 凡是递归的函数, 是可计算的, 即能行的.
'''

# 递归函数
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)

result = sum(10)
print(result)
