"""
sys模块
time模块
1.时间戳  time.time()
2.将时间戳转换成字符串  time.ctime(t)
3.将时间戳改成元组 s1 = time.localtime()
4.将元组改成时间戳  time.mktime(s1)
5.将元组的时间改成字符串  time.strftime('%Y-%m-%d')
6.将字符串改成元组的方式  time.strptime('2020/6/7','%Y/%m/%d')
datetime模块
1.时间差  datetime.timedelta
random模块
hashlib模块：加密

"""
import time
import datetime
import random


# t = time.time()
# print(t)
# time.sleep(3)
# t1 = time.time()
# print(t1)
# s = time.ctime(t)
# print(s)
# s1 = time.localtime()
# print(s1)
# print(s1.tm_hour)
#
# tt = time.mktime(s1)
# print(tt)
#
# s = time.strftime('%Y-%m-%d %H:%M:%S')
# print(s)
#
# r = time.strptime('2020/6/7', '%Y/%m/%d')
# print(r)
#
# print('-------------------------------------------')
# # 时间差
# timedel = datetime.timedelta(days=3)
# now = datetime.datetime.now()
# s = now + timedel
# print(s)
# ran = random.random() #产生0~1之间的随机小数
# # print(ran)
# #
# # ran = random.randrange(1,10,2)
# # print(ran)
# # ran = random.randrange(1,10)
# # print(ran)
# #
# # ran = random.randint(1,10)
# # print(ran)
# #
# # list1 = ['薛强','彭帅','王新欣']
# # ran = random.choice(list1)
# # print(ran)
# #
# # ran = random.shuffle(list1)  #打乱列表的顺序
# # print(list1)

# 验证码 随机产生大小写字母和数字的四位组合
# chr(数字) 转化成字母 ，ord(字母) 字母或汉字转化成数字


def func():
    code = ''
    for i in range(4):
        ran1 = str(random.randint(0, 9))
        ran2 = chr(random.randint(65, 90))  # 随机产生大写字母
        ran3 = chr(random.randint(97, 122))  # 随机产生小写字母
        r = random.choice([ran1, ran2, ran3])
        code += r
    return code


fun = func()
print(fun)
