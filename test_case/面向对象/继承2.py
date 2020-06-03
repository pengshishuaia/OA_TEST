'''
has a 的实例讲解
知识点：
1，has a
    一个类中使用另外一中自定义类型
    student 使用compute和books类
2，类型
    系统类型：1，int str float 2，dict list tuple set
    自定义类型:算是自定义的类，都可以将其当成一种类型
    s = student（）
    s是student类型的对象
'''


class Computer:
    def __init__(self, type, color):
        self.type = type
        self.color = color

    def online(self):
        print('正在上网中....')

    def __str__(self):
        # '正在用品牌为:{},颜色为{}的电脑在上网'.format(self.type, self.color)
        return self.type + '---' + self.color


class Books:
    def __init__(self, bname, author, number):
        self.bname = bname
        self.author = author
        self.number = number

    def __str__(self):
        return self.bname + '---' + self.author + '---' + str(self.number)


class Student:
    def __init__(self, name, computer, book):
        self.name = name
        self.computer = computer
        self.books = []
        self.books.append(book)  # books = ['盗墓笔记---南派三叔---10']

    def borrow_book(self, book):   # book = book2 鬼吹灯---天下霸唱---8
        # print('books的值为',self.books)
        for book1 in self.books:
            print('book1的值为:',book1)
            if book1.bname == book.bname:
                print(book1.bname)
                print(book.bname)
                print('已经借过了')
                break
        else:
            self.books.append(book)
            print('添加成功')

    def show_book(self):
        for book in self.books:
            print(book.bname)

    def __str__(self):
        return self.name + '---' + str(self.computer) + '---' + str(self.books)


computer = Computer('苹果', '深灰色')
book = Books('盗墓笔记', '南派三叔', 10)

print(book)   # 盗墓笔记---南派三叔---10
stu = Student('彭帅', computer, book)
#stu = Student('彭帅', computer, book2)
print(stu)
#stu.show_book()

book2 = Books('鬼吹灯', '天下霸唱', 8)
# print(book2)
stu.borrow_book(book2)
print('*'*30)
stu.show_book()
