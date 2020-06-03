class Student:
    def __init__(self,name,age,book):
        self.name = name
        self.age = age
        self.books = []
        self.books.append(book)
    def score(self,book):
            self.books.append(book)
            print('{}一共有{}本书'.format(self.name,self.books))

stu = Student('彭帅',23,'盗墓笔记')
stu.score('寻秦记')
stu = Student('王欣欣',18,'鬼吹灯')
stu.score('斗罗大陆')