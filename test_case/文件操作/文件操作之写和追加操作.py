'''
写文件
write(内容)，每次都会讲原来的内容情况，然后写当前的内容
writeable（）判断文件是否可写
writelines（）
open(r'D:\test\test.txt','w') w：要情况原文件的内容，然后在填写
open(r'D:\test\test.txt','a') a：在原文本的基础上，追加内容
'''
container = '''
你好：
    欢迎来的python学习时间。
                    谢谢！
'''
# stream = open(r'D:\test\test.txt','w')
# stream.write(container)
# stream.write('赌神:周润发\n')
# stream.write('赌圣:周星驰\n')
# stream.writelines(['赌神:高进\n','赌侠:刘德华\n'])
# stream.close()  # 释放资源


stream = open(r'D:\test\test.txt','a')
stream.write(container)
stream.write('赌神:周润发\n')
stream.write('赌圣:周星驰\n')
stream.writelines(['赌神:高进\n','赌侠:刘德华\n'])
stream.close()  # 释放资源