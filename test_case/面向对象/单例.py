'''
单例模式
开发模式：单例模式
'''


# class Singleton():
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = object.__new__(cls)
#             return cls.__instance
#         else:
#             return cls.__instance
#
#
# s1 = Singleton()
# print(s1)
# s2 = Singleton()
# print(s2)


def singleton(cls):
    instance = cls()
    instance.__call__ = lambda: instance
    return instance

@singleton
class Student():
    def __init__(self):
        name = 'jack'
        age = 18

stu1 = Student
stu2 = Student
print(stu1)
print(stu2)
