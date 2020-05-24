user_list = [{"name": '彭大帅', "tel": "18910503484", "QQ": "381833187"},
             {"name": '王欣欣', "tel": "17801239596", "QQ": "381833186"},
             {"name": '彭小二', "tel": "18910508888", "QQ": "381836666"}]


def insert_user():  # 新增用户信息
    # 新建字典
    arr = {}
    user = input("请输入姓名:")
    phone = input("请输入手机号码:")
    number = input("请输入QQ号码:")
    arr['name'] = user
    arr['tel'] = phone
    arr['QQ'] = user
    print(arr)
    user_list.append(arr)
    print(user_list)


def check_number(number):
    # 判断输入的数字是否合法
    if number.isdigit():  # 输入是数字，转换成整型
        number = int(number)
        if 0 < number < len(user_list):
            return True
    return False


def del_user():
    number = input("请输入要删除的序号(序号从0开始)：")
    is_valid = check_number(number)
    if is_valid:
        answer = input("你确实要删除吗！yes or no：\t")
        # 删除列表中的用户有两种办法
        # remove:删除列表中指定的元素
        # pop:删除列表中制定位置的元素，默认最后一个
        if answer.lower() == 'yes':  # lower() 方法转换字符串中所有大写字符为小写。
            user_list.pop(int(number))

    else:
        print("输入的序号不合法！！！")

    print(user_list)


def update_user():  # 更新用户信息
    update_information = input("请输入您要修改名片人的姓名:")
    i = 0
    for user_name in user_list:
        i += 1
        if update_information in user_name['姓名']:
            print('要修改的名片的信息已经找到')
            break
    print(user_name)

    user = input("请输入姓名:")
    phone = input("请输入手机号码:")
    number = input("请输入QQ号码:")
    user_name['name'] = user
    user_name['tel'] = phone
    user_name['QQ'] = number
    print(user_name)
    print(list)


def search_user():
    query_user = input("请输入要查询的姓名：")
    for value in user_list:
        if value['name'] == query_user:
            print("您查询到的信息如下：\n姓名:{name},手机号码:{tel},QQ号码:{QQ}".format(**value))
            break
        else:
            print("没有您要查询的信息")


def all_user():
    print('序号     姓名        手机号码        QQ号码')
    # enumerate函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
    for key, value in enumerate(user_list):
        print(key, value['name'].center(14), value['tel'].center(5), value['QQ'].center(14))


def exit_system():  # 退出系统函数
    answer = input("您是否要退出系统！（yes or no）")
    if answer == 'yes':
        exit()


def Card_system():
    while True:
        print('***********************')
        print("名片印制管理系统V1.0")
        print("1:新增名片")
        print("2:删除名片")
        print("3:修改名片")
        print("4:查询名片信息")
        print("5:查询所有名片信息")
        print("6:退出")
        print('***********************')
        temp = input("请输入要选择的操作（输入数字即可）：")
        if temp == '1':
            insert_user()
        elif temp == '2':
            del_user()
        elif temp == '3':
            update_user()
        elif temp == '4':
            search_user()
        elif temp == '5':
            all_user()
        elif temp == '6':
            exit_system()


if __name__ == '__main__':
    Card_system()
