# class Foo(object):
#     """类三种方法语法格式"""
#
#     def instance_method(self):
#         print("是类{}的实例方法,只能被实例对象调用".format(Foo))
#
#     @staticmethod
#     def static_method():
#         print("是静态方法")
#
#     @classmethod
#     def class_method(cls):
#         print("是类方法")
#
# foo = Foo()
# foo.instance_method()
# foo.static_method()
# foo.class_method()
# print("---------------")
# Foo.static_method()
# Foo.class_method()
#
#
# 类方法用在模拟java定义多个构造函数的情况。 由于python类中只能有一个初始化方法，不能按照不同的情况初始化类
#
#
# class Book(object):
#
#     def __init__(self, title):
#         self.title = title
#
#     @classmethod
#     def create(cls, title):
#         book = cls(title=title)
#         return book
#
# book1 = Book("python")
# book2 = Book.create("python and django")
# print(book1.title)
# print(book2.title)
#
# 类中静态方法调用静态方法的情况 和 类方法调用静态方法的情况，可以让cls代替类
#
#
# class Foo(object):
#     x = 1
#     y = 2
#
#     @staticmethod
#     def average(*mixes):
#         return sum(mixes) / len(mixes)
#
#     @staticmethod
#     def static_method():
#         return Foo.average(Foo.x, Foo.y)
#
#     @classmethod
#     def class_method(cls):
#         return cls.average(cls.x, cls.y)
#
# foo = Foo()
# print(foo.static_method())
# print(foo.class_method())


class Foo(object):
    x = 1
    y = 2

    def print_func(self):
        print("Foo print_func")

    @staticmethod
    def average(*mixes):
        print("Foo average")
        return sum(mixes) / len(mixes)

    @staticmethod
    def static_method():
        print("Foo static_method")
        return Foo.average(Foo.x, Foo.y)

    @classmethod
    def class_method(cls):
        print("Foo class_method")
        print(cls.x, cls.y)
        return cls.average(cls.x, cls.y)


class Son(Foo):
    x = 3
    y = 5

    def print_func(self):
        print("Son print_func")

    @staticmethod
    def average(*mixes):
        print("Son average")
        return sum(mixes) / 3

    @classmethod
    def class_method(cls):
        print("Son class_method")
        return cls.average(cls.x, cls.y)

p = Son()
f = Foo()
print(p.print_func())
print(p.static_method())
print(p.class_method())
print("----------------------")
print(f.class_method())

import importlib

aa = importlib.import_module("lib.aa")
print(aa.C().name)