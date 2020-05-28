'''
文件操作：
文件上传
文件下载
stream = open（path/filename,'rt'）rt为默认，----返回值stream（流）
container = stream.read()   -----读取流中的内容
注意：如果传递的path/filename有问题，则会报错
如果是图片或其他类型文件（不是txt格式），则不能使用默认的读取方式 mode = rb
read（）读取所有内容
readline() 读取一行内容
readlines() 读取所有内容，并且将内容放到列表中心
readable() 判断文档是否可读
'''

stream = open(r'D:\test\test.txt')
# print(stream.read())
# print(stream.readable())
# print(stream.readline())
# print(stream.readlines())
