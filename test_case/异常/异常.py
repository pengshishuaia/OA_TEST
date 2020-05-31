'''
异常:在程序运行的时候产生的错误
异常处理：
格式：
try:
    可能出现异常的代码
except:
    执行出现异常的代码
finally:（可以不写）
    无论有没有异常都会执行

情况1：可以有多个except
try:
    可能出现异常的代码
except:
    执行出现异常的代码
except:
    执行出现异常的代码
情况2
try:
    pass
except NameError:
    pass
except FileNotFoundError:
    pass
except Exception:
    pass
情况3
try:
    pass
except NameError:
    pass
except FileNotFoundError:
    pass
except Exception as err:
    print(err)
情况4
try:
    pass
except NameError:
    pass
except FileNotFoundError:
    pass
except Exception as err:
    print(err)
finally:
    pass
'''
'''
在实际的应用场景中，除了代码出错Python解释器会抛出异常之外，我们还可以根据自己的业务需求自定义异常并主动抛出
抛出异常的2个步骤：

1）创建一个Exception对象
使用raise关键字抛出异常对象
实战演练----输入的密码少于6位
需求：

定义一个函数input_pwd,提示用户输入密码
如果用户输入的密码少于6位，抛出异常
如果用户输入的密码大于等于6位，则返回输入的密码
'''
def input_pwd():
    # 1.提示用户输入密码
    pwd  = input("请输入密码：")

    # 2.判断密码长度，如果长度 >= 6，返回用户输入的密码
    if len(pwd) > 6:
        return pwd
    # 3.密码长度小于6位，则需要抛出异常

    # 创建异常对象
    ex = Exception("密码长度小于6位")

    # 抛出异常对象
    raise ex

# 调用函数
try:
    user_pwd = input_pwd()
    print(user_pwd)
except Exception as err:
    print(err)
else:
    print('注册成功')
