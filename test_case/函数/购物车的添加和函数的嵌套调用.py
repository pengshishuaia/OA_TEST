# coding=utf-8
"""
加入购物车
判断用户是否登录，如果已经的登录，成功添加购物车，否则提示请先登录后添加
成功 ture  不成功false
两个函数一个登陆函数，一个添加购物车的函数
"""


def login(username, password):
    if username == 'ps' and password == 123456:
        return True
    else:
        print('没有登录，请从新登录')
        return False


isdigit = False  #判断用户是否登录的变量，，默认不登录


def add_shopping_cart(trade):
    global isdigit
    if isdigit:
        if trade:
            print('已成功将{}加入购物车中'.format(trade))
        # else:
            # answer = input('请选择商品，是否要登录（yes/no）')
            # if answer == 'yes':
            #     username = input("请输入用户名：")
            #     password = int(input("请输入密码："))
            #     isdigit = login(username, password)
            #     print('isdigit',isdigit)
            # else:
            #     print("很遗憾！！")
    else:
        answer = input('请选择商品，是否要登录（yes/no）')
        if answer == 'yes':
            username = input("请输入用户名：")
            password = int(input("请输入密码："))
            isdigit = login(username, password)
            print('isdigit', isdigit)
        else:
            print("很遗憾！！")


username = input("请输入用户名：")
password = int(input("请输入密码："))

isdigit = login(username, password)
add_shopping_cart("阿玛尼")
