'''
文件的黏贴复制
原理：首先要读取一个文件，然后将文件复制到想要的文件夹

os常用函数
绝对路径
相对路径

dirname()
join()
split()
splittext()
geisize()

'''

#单个文件的黏贴复制
# with open(r'F:\Test_Python1\sky.jpg','rb') as stream:
#     container = stream.read()  # 读取文件内容
#     with open(r'F:\Test_Python2\sky.jpg','wb') as wstream:
#         wstream.write(container)
# print('文件复制完成')

#多个文件的黏贴复制

import os


with open(r'F:\Test_Python1\sky.jpg','rb') as stream:
    container = stream.read()  # 读取文件内容
    print(stream.name)
    file = stream.name
    # rfind() 返回子字符串最后一次出现在字符串中的索引位置，
    # 该方法与 rindex() 方法一样，只不过如果子字符串不在字符串中不会报异常，而是返回-1。
    filename = file[file.rfind('\\')+1:]
    print(filename)
    path = os.path.dirname(__file__)  # 获取当前文件的目录
    path1 = os.path.join(path,filename)
    print(path1)
    with open(path1,'wb') as wstream:
        wstream.write(container)
print('文件复制完成')