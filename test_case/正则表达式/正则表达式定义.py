'''
分组：()
re 模块
match 从头开始查找
search  查找一次
findall  查找所有
sub(正则表单时，新内容，str字符串)  替换
split 切割
'''
import re
#
# msg = '0012-85068083'
# result = re.match(r'(\d{3}|\d{4})-(\d{8})$',msg)
# print(result)
# print(result.group(1))
# print(result.group(2))
#
#
# msg1 = '<h1>hello word<h1>'
# result = re.match(r'(<\w+>)(.+)(<\w+>)$',msg1)
# print(result)
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
#
msg2 = '<h1>hello word1<h1>'
result1 = re.match(r'<(\w+)>(.+)<\1>',msg2)
print(result1)
print(result1.group(1))



msg3 = '<html><h1>helloword<h1><html>'

result = re.match(r'<(?P<name>\w+)><(?P<name1>\w+)>(.+)<(?P=name1)><(?P=name)>',msg3)
print(result)
