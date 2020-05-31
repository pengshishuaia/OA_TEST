'''
列表推导式 字典推导式 集合推导式
列表推导式
格式：[表达式 for 变量 in 列表]    或者  [表达式 for 变量 in 列表 if 条件]
old_list= [1,23,4,56]
new_list = [i for i in old_list if i%2==0 ]
'''

#  列表推导式
old_list = [1, 23, 4, 56]
new_list = [i for i in old_list if i % 2 == 0]
print(new_list)

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list1 = [x ** 2 for x in li]
print(new_list1)
new_list2 = [x ** 2 for x in li if x > 5]
print(new_list2)

print(dict([(x, x * 10) for x in li]))

print([(x, y) for x in range(10) if x % 2 if x > 3 for y in range(10) if y > 7 if y != 8])

vec = [2, 4, 6]
vec2 = [4, 3, -9]
sq = [vec[i] + vec2[i] for i in range(len(vec))]
print(sq)

print([x * y for x in [1, 2, 3] for y in [1, 2, 3]])

testList = [1, 2, 3, 4]


def mul2(x):
    return x * 2


print([mul2(i) for i in testList])

# 集合推导式  {}集合推导式类似列表推导式，只是在列表推导式基础上多了去重的功能
list1 = [1,2,4,56,8,1,23,4,8]
new_set = {i-1 for i in list1 if i > 5}
print(new_set)
# 字典推导式
dict1 = {'name':'ps','age':13,'studenrt':'三年级'}
new_dict = {value:key for value,key in dict1.items()}