"""
开发：登录验证
"""
import time

is_login = False  # 默认没有登录


def login():
    username = input('请输入账号：')
    password = input('请输入密码：')
    if username == 'admin' and password == '123456':
        print('登录成功！')
        return True
    else:
        print('登录失败！')
        return False


# 定义装饰器，进行付款验证
def login_require(func):
    def wrapper(*args, **kwargs):
        global is_login
        print('----付款----')
        # 验证用户是否登录
        if is_login:
            func(*args, **kwargs)
        else:
            # 跳转到登录页面
            print('您还没有登录，请先登录')
            is_login = login()
            print('打印结果', is_login)

    return wrapper


@login_require
def Pay(money):
    print('您需要支付的金额为{}'.format(money))
    print('支付中....')
    time.sleep(2)
    print('支付完成')


Pay(1000)

Pay(2000)