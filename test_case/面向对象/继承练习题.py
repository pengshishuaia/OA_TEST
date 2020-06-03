"""
编写一个简单的工资管理程序。系统可以管理一下四类人：工人（worker），销售员（salesman），经理（manager），销售经理（salemanager）
所有的员工都有工号，姓名，工资等属性，有设置姓名，获取姓名，获取员工号，计算工资等方法
1，工人：工人具有工作小时数和时薪的属性，工资计算方法为工作小时数*时薪
2，销售员：具有销售额和提成的比例的属性，工资计算方法为销售额*提成比例
3，经理：有固定的月薪属性，工作方法有固定月薪
4，销售经理：工资计算方法为销售额*提成比例+固定月薪
请跟进以上要求设计合理的类，完成以下功能
1，添加所有类型人员
2，计算月薪
3，显示所有人工资
"""


class Person:
    def __init__(self, name, number, salary):
        self.name = name
        self.number = number
        self.salary = salary

    def __str__(self):
        msg = '工号:{},姓名;{},薪水;{}'.format(self.name, self.number, self.salary)
        return msg

    def getSalary(self):
        return self.salary


class Worker(Person):
    def __init__(self, name, number, salary, hour, wage):
        super().__init__(name, number, salary)
        self.hour = hour
        self.wage = wage

    def getSalary(self):
        money = self.hour * self.wage
        self.salary += money
        #print('员工姓名:{}，员工编号：{}的时薪为:{}人民币,一共工作了{}小时,总工资为{}'.
              #format(self.name, self.number, self.wage, self.hour, money))
        return self.salary


class Salesman(Person):
    def __init__(self, name, number, salary, saleroom, percent):
        super().__init__(name, number, salary)
        self.saleroom = saleroom
        self.percent = percent

    def getSalary(self):
        money = self.saleroom * self.percent
        self.salary += money
        return self.salary


class Manager(Person):
    pass


class Salemanager(Person):
    pass


work = Worker('彭帅', '08137', 2000, 40, 500)
salary = work.getSalary()
print('月薪：',salary)
