str = 'peng@shuai is student'

msg = str.lower()  # lower()将字符串中的所有字母改成小写
print(msg)

print(str.upper())  # upper()将字符串中的所有字母改成大写

print(str.isdigit())  # isdigit()判断符串中的内容是否全为数字，是返回True,不是返回False
print(str.isalpha())  # isalpha()判断符串中的内容是否全为字母，是返回True,不是返回False，空格，特殊字符不算字母
print(str.split('@'))  # split()函数是将字符串按照特殊字符分割为数组

'''
输入两个字符串，从第一个字符串中删除第二个字符串中所有的字符
例如输入：'They are students' 和'aeiou'
删除之后第一个字符串的结果为：'Thy r stdnts'
'''
str1 = 'They are students'
str2 = 'aeiou'
str3 = ''
# 方法一
# for i in str2:
#     str1 = str1.replace(i,'')
# print(str1)
#
# 方法二
# for i in str1:
#     if i not in str2:
#         str3 += i
# str1 = str3
# print(str1)
#
# # 方法三
# for i in str2:
#     if i not in str3:
#         str3 += i
#         # print(str3)  # 去除Str2字符串中的重复项
# for i in str3:
#     str1 = str1.replace(i,'')
# print(str1)

'''
小王喜欢的单词有以下特性
1，单词的每个字母都是大写
2，单词没有连续相同的字母
思路：1，首先判断单词是否都是字母
      2，如果都是字母，判断字母是否都是大写
      3，判断相邻的字母是否重复
'''
str = input('请输入一个单词：')

for i in range(len(str)):
    msg = str.isupper()
    if msg == False:  # 如果msg为真
        print('该字符串有小写字符或其他字符，小王不喜欢')
        break
    else:
        if i < len(str)-1 and str[i] == str[i+1]:
            print('有连续相同的字母,小王不喜欢')
            break
else:
    print('单词小王喜欢')
