'''
实例方法（普通方法）——————————————————————随着实例属性的改变而改变
类方法（无论是类调用还是实例调用）———————————————都是类属性的值，不随实例属性的变化而变化
静态方法————————————————————————————不可以访问类属性，故直接输出传入方法的值
静态方法和类方法：
1，只能访问类属性和方法，对象的是无法访问的
2，都可以通过类名调用访问
3，可以在创建对象之前使用，因为是不依赖对象的
'''
class A():
    explanation = 'This is my programs'
    #普通方法
    def normalMethod(self,explanation):
        print(self.explanation)
    #类方法
    @classmethod
    def classMethod(cls,explanation):
        print(cls.explanation)
    #静态方法
    @staticmethod
    def staticMethod(explanation):
        print(explanation)


#创建对象
print(A())
a = A()
print(a)
#print(a.explanation)
a.explanation='This is new'
#A.normalMethod('测试0')  #普通方法不能直接被类调用
a.normalMethod('测试1')  # 打印结果 This is new

a.classMethod('测试2')   # 打印结果 This is my programs
A.classMethod('测试3')   # 打印结果 This is my programs

a.staticMethod('测试4')  # 打印结果 测试4
A.staticMethod('测试5')  # 打印结果 测试5