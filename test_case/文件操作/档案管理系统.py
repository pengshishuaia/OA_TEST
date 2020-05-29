"""
将数据保存到本地文件内，并读取文件
1,注册页面
2，登录页面
3，查阅文件目录
4，借书
5，归还图书
"""

# 注册页面
def register():
    print('------欢迎来到注册页面------')
    username = input('请输入用户名:')
    password = input('请输入密码:')
    confirm_password = input('请输入确认密码:')
    if password == confirm_password:
        with open(r'E:\python_test\user.txt', 'a') as wstream:
            wstream.write('{},{}\n'.format(username, password))
        wstream.close()
        print('恭喜您，注册成功')
    else:
        print('您输入的两次密码不一致，请从新注册！')

#登录页面
def login():
    print('------欢迎来到登录页面------')
   # username = input('请输入用户名:')
    #password = input('请输入密码:')
    with open(r'E:\python_test\user.txt') as rstream:
        container = rstream.readlines()
        for user in container:
            print(user,end='')
            print(type(user))
            print(user.split(','))
            #if username == user[0] and password == user[1]:
                #print('登录成功！')
            #else:
                #print('账号或密码错误，请从新登录')

        # print(container)  ['彭帅,123456\n', '王欣欣,123456\n']


login()
