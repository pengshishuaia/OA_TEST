"""
注册页面，字段有
用户名
密码
确认密码
邮箱
手机号码
"""
print('-------------欢迎来到注册页面-------------')
database = []
while True:
    user = {}
    username = input('请输入用户名：')
    user['username'] = username
    password = input('请设置密码：')
    Confirm_password = input('请输入确认密码（要和设置的密码保持一致）：')
    if password == Confirm_password:
        user['password'] = password
    else:
        print("您输入的两次密码不一致，请从新输入！")
        continue
    email = input('请输入邮箱号码：')
    phone = input('请输入手机号码：')
    user['email'] = email
    user['phone'] = phone
    database.append(user)
    answer = input('您是否要继续注册（y/n）')
    if answer != 'y':
        print('欢迎下次光临！')
        break
print(database)
