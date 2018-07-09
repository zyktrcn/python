#!/usr/local/bin/python3

# char = 'S'
# string = 'hello' + \
#         'word'
# print(char)
# # print('#')
# print(string)

# input('enter: \n')

# a, b = 1, 2
# print(a+b, a-b, a/b, a//b, a%b, a**b)

# s = 'hello word'
# print(s[1:5], s*3, s[1])

# list = [1, 'hello', 100.002, 'word']
# list[1] = 'word'
# list[3] = ['hello', 'word']
# print(list, list[1], type(list), len(list))

# tupe = (1001, 'hello', 'word', [100, 'string'], (2, 3))
# print(tupe, tupe[1], type(tupe), len(tupe))

# list = [1, 2, 3, 4]
# def add(item):
#     return item + 1
# subList = [add(item) for item in list]
# print(subList)

# listO = [1, 2, 3, 4]
# listT = [2, 3, 4, 5]
# def add(o, t):
#     return o*t
# subList = [add(o, t) for t in listT for o in listO]
# print(subList)

# list = [
# 	[1, 2, 3, 4],
# 	[2, 3, 4, 5],
# 	[3, 4, 5, 6]
# ]
# subList = [[items[i] for items in list] for i in range(4)]
# print(subList)

# for items in list:
# 	for item in items:
# 		print(item)

# n = 0
# while n < len(list):
# 	m = 0
# 	while m < len(list[n]):
# 		print(list[n][m])
# 		m = m+1	
# 	n = n+1

# for item in range(0, 100, 20):
# 	print(item)

# list = [1, 2, 3, 4]
# del list[:]
# del list[0]
# del list[1:3]
# del list
# print(list)

# array = {1, 2, 'hello', 'word'}
# array = set('abcd')
# array = {x for x in range(4)}
# print(array)
# print(1 in array)
# for index, val in enumerate(array):
# 	print(index, val)

# obj = {
# 	'jack': 1,
# 	'jason': 2,
# 	'sape': 3
# }
# obj = dict([('jack', 1), ('jason', 2), ('sape', 3)])
# print(obj)
# print(obj['jack'])
# for key, val in obj.items():
# 	print(key, ':', val)

# for x in range(1, 11):
# 	print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))

# for x in range(1, 11):
# 	print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# for x in range(1, 11):
# 	print(repr(x).center(3), repr(x*x).center(4), repr(x*x*x).center(5))

# for x in range(1, 11):
# 	print(repr(x).ljust(3), repr(x*x).ljust(4), repr(x*x*x).ljust(5))

# for x in range(1, 11):
# 	print(repr(x).zfill(2), repr(x*x).zfill(2), repr(x*x*x).zfill(2))

# print('{0} and {1}'.format('span', 'eggs'))
# print('{seafood} is seafood'.format(seafood = 'seafood'))
# print('seafood is {}'.format('seafood', 'fruit'))
# print('pi is {0:.3f}'.format(3.1412173123))
# print('pi is {0:10}'.format(3.14))

# file = open('text', 'w+')
# file.write('this is an another doc')
# file.seek(0)
# content = file.read()
# print(content)
# file.close()

# file = open('text', 'r')
# def getContent():
# 	return file.read()
# print(getContent())
# print(getContent())
# file.seek(0)
# print(getContent())
# file.close()

# import pickle
# string = 'this is a doc'
# ano = 'this is an another doc'

# file = open('text', 'wb')
# pickle.dump(string, file)
# pickle.dump(ano, file)
# file.close()

# import pprint, pickle
# file = open('text', 'rb')
# content = pickle.load(file)
# pprint.pprint(content)
# file.close()

# class animal:
	
# 	def __init__(self, name, legs):
# 		self.name = name
# 		self.legs = legs

# 	def output(self):
# 		return self.name

# x = animal('dog', 4)
# print(x.name, x.legs, x.output())

# class dog(animal):
# 	def getLegs(self):
# 		return self.legs

# 	def output(self):
# 		return 'output'

# y = dog('dog', 4)
# print(y.name, y.legs, y.output(), y.getLegs())

# import os
# path = os.getcwd()
# print(path)

# list = [1, 2, 'example', 4, 'hello']
# list.append('apple')
# print(list)
# index = list.index(1)
# print(index)
# list.remove(4)
# print(list)
# list.remove(1)
# print(list)
# list.remove(2)
# print(list)
# more = list + ['example', 'more', 9]
# print(more)
# string = ",".join(list)
# print(string)
# li = string.split(',')
# print(li)

# import calendar
# year = int(input("year: "))
# month = int(input("month: "))
# print(calendar.month(year, month))

# import re
# string = '123abc456'
# rule = '([0-9]*)([a-z]*)([0-9]*)'
# search = re.search(rule, string)
# print(search.group(0))
# print(search.group(1))
# print(search.group(2))
# print(search.group(3))
# rule = '([0-9]{3})'
# findall = re.findall(rule, string)
# print(findall)

# import pymysql
# db = pymysql.connect("127.0.0.1", "root", "199456", "Python")
# cursor = db.cursor()
# insert = "INSERT INTO user VALUES (2, 'Fu', 'Jintao')"
# try:
# 	cursor.execute(insert)
# 	db.commit()
# except:
# 	db.rollback()
# select = "SELECT * FROM user"
# cursor.execute(select)
# delete = "DELETE FROM user WHERE id = 1"
# try:
# 	cursor.execute(delete)
# 	db.commit()
# except:
# 	db.rollback()
# data = cursor.fetchall()
# data = cursor.fetchmany(2)
# data = cursor.fetchone()
# print(data)
# db.close()






















