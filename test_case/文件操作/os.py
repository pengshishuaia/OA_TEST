
"""
os.path里面的函数
"""
import os
dir = os.getcwd()
print("当前文件夹的目录为：",dir)
all = os.listdir(r'F:\Test_Python1') #返回指定目录下的所有文件和文件夹，保存到列表中心
print('当前文件夹下的目录为：{}'.format(all))

#创建文件夹
os.mkdir()
#删除文件夹：rmdir() 只能删除空文件夹
os.rmdir()
#删除文件
os.remove()
#删除文件夹（文件夹下有文件），思路：首先删除文件夹下的文件，然后再删除文件
#切换目录