# coding=utf-8
"""
添加购物车功能
定义两个函数，一个登录函数，一个添加函数
"""


def login():
    username = input('请输入账号:')
    password = input('请输入密码:')
    if username == 'ps' and password == '123456':
        print('登录成功')
        return True
    else:
        print('登录失败')
        return False


is_login = False


def add_shopping(trade):
    global is_login
    if is_login:
        if trade:
            print("您已经将商品{}成功添加购物车".format(trade))
        else:
            print('您没有选择任何商品')
    else:
        # 请登录
        answer = input('系统还没有登录，是否要登录（yes/no）')
        if answer == 'yes':
            is_login = login()
        else:
            print('很遗憾')


is_login = login()

add_shopping("阿玛尼")


