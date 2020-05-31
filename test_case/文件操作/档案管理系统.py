"""
将数据保存到本地文件内，并读取文件
1,注册页面
2，登录页面
3，查阅文件目录
4，借书
5，归还图书
"""
is_login = False


# 注册页面
def register():
    print('------欢迎来到注册页面------')
    username = input('请输入用户名:')
    password = input('请输入密码:')
    confirm_password = input('请输入确认密码:')
    if password == confirm_password:
        with open(r'F:\Test_Python2\user.txt', 'a') as wstream:
            wstream.write('{},{}\n'.format(username, password))
        wstream.close()
        print('恭喜您，注册成功')
    else:
        print('您输入的两次密码不一致，请从新注册！')


# 登录页面
def login():
    print('------欢迎来到登录页面------')
    username = input('请输入用户名:')
    password = input('请输入密码:')
    with open(r'F:\Test_Python2\user.txt') as rstream:
        container = rstream.readlines()
        for user in container:
            input_user = '{},{}\n'.format(username, password)
            if user == input_user:
                print('恭喜您，登录成功！')
                return True
                break


        else:
            print("您输入的账号或密码错误，请从新输入")
            return False


# 图书查询
def book_query():
    global is_login
    if is_login:
        with open(r'F:\Test_Python2\books.txt') as rstream:
            contains = rstream.readlines()
            print('图书馆可借阅的图书有:')
            for book in contains:
                print(book, end='')
    else:
        answer = input('系统还没有登录，是否要登录（yes/no）')
        answer = answer.lower()
        if answer == 'yes':
            login()
        else:
            print('您输入的有误')


# register()
#print(login())
is_login = login()
book_query()
