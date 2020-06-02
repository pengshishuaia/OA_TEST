'''
has a 的实例讲解
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
        self.books.append(book)

    def borrow_book(self, book):
        for book1 in self.books:
            print('book1的值为:',book1)
            if book1.bname == book.bname:
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
stu = Student('彭帅', computer, book)
print(stu)
stu.show_book()
book2 = Books('鬼吹灯', '天下霸唱', 8)
stu.borrow_book(book2)
print('*'*30)
stu.show_book()
