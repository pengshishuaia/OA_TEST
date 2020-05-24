# 定义生产验证码函数
import random


def verification_code(number):
    s = '1234567890qazwsxedcrfvtgbyhnujmikolpGYHJKIGGW'
    code = ''
    for i in range(number):
        index = random.randint(0, len(s) - 1)
        code += s[index]
    return code


# 定义登录函数
def login():
    username = input('请输入用户名：')
    password = input('请输入密码：')
    code = verification_code(4)
    print(code)
    captcha = input('请输入验证码')
    if code.lower() == captcha.lower():
        if username == 'ps' and password == '123456':
            print('登录成功！')
        else:
            print('输入的账号或密码有误！')
    else:
        print('您输入的验证码有误！')


login()
