'''
总结列表知识点：
1.定义
list = [] 空列表
2.符号
+   合并[]+[]
*   []* n
in  a in list 返回false或true
not in a not in list 返回false或true
is 是否相等
not is 是否不想等

3.系统给出的列表用函数
len(list) 列表的长度
sorted(list) 列表排序
max(list)  列表最大值
min(list)  列表最小值
list()     强制转换成列表类型
enumerate()  枚举 index value

4.列表自身的函数
添加元素：
    append() 末尾添加
    extend() 末尾添加一组元素
    insert(位置,值) 制定位置添加
删除元素：
    del list[index]
    remove(值) 删除指定元素，如果指定的元素不存在则报异常
    pop() 默认删除最后一个元素
    clear() 清空元素
其他：
    count() 统计指定元素的个数
    sort()  排序
    reverse() 翻转
5.算法
选择排序
冒泡排序
'''