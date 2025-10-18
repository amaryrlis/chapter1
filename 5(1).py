#python基本语法
print("Hello, World!")  # 输出Hello, World!
# 变量赋值
x = 5
y = 10
sum = x + y
print("Sum:", sum)  # 输出Sum: 15
# 条件语句
if sum > 10:
    print("Sum is greater than 10")
else:
    print("Sum is 10 or less")
# 循环语句
for i in range(5):
    print("Iteration:", i)
# 函数定义
def greet(name):
    return "Hello, " + name + "!"
print(greet("Alice"))  # 输出Hello, Alice!
# 列表操作
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)
# 字典操作
person = {"name": "Bob", "age": 25}
print("Name:", person["name"])  # 输出Name: Bob
print("Age:", person["age"])    # 输出Age: 25
# 异常处理
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")
# 类定义
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return "Woof! My name is " + self.name
my_dog = Dog("Buddy")
print(my_dog.bark())  # 输出Woof! My name is Buddy
# 文件操作
with open("example.txt", "w") as file:
    file.write("This is an example file.")
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:", content)  # 输出File Content: This is an example file.
# 模块导入
import math
print("Square root of 16 is", math.sqrt(16))  # 输出Square root of 16 is 4.0
# 列表推导式
squares = [x**2 for x in range(10)]
print("Squares:", squares)  # 输出Squares: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Lambda函数
add = lambda a, b: a + b
print("Lambda Add:", add(3, 7))  # 输出Lambda Add:
  10
# 使用map函数
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)  # 输出Doubled: [2, 4, 6, 8, 10]
# 使用filter函数
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)  # 输出Even Numbers: [2, 4]
# 使用生成器
def countdown(n):
    while n > 0:
        yield n
        n -= 1
for number in countdown(5):
    print("Countdown:", number)  # 输出Countdown: 5 ... Countdown: 1
# 使用装饰器
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before", original_function.__name__)
        return original_function()
    return wrapper_function
@decorator_function
def say_hello():
    print("Hello!")
say_hello()  # 输出Wrapper executed before say_hello \n Hello!
# 使用集合
my_set = {1, 2, 3, 4, 5}
my_set.add(6) 
print("Set:", my_set)  # 输出Set: {1, 2, 3, 4, 5, 6}
# 使用元组
my_tuple = (10, 20, 30)
print("Tuple:", my_tuple)  # 输出Tuple: (10, 20, 30)
# 列表排序
unsorted_list = [5, 2, 9, 1, 5, 6]
sorted_list = sorted(unsorted_list)
print("Sorted List:", sorted_list)  # 输出Sorted List: [1, 2, 5, 5, 6, 9]
# 使用zip函数
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print("Zipped:", zipped)  # 输出Zipped: [(1, 'a'), (2, 'b'), (3, 'c')]
# 使用enumerate函数
for index, value in enumerate(['x', 'y', 'z']):
    print("Index:", index, "Value:", value)
# 输出Index: 0 Value: x \n Index: 1 Value: y \n Index: 2 Value: z
# 使用datetime模块
import datetime
now = datetime.datetime.now()
print("Current Date and Time:", now)  # 输出Current Date and Time: <current date and time>
# 使用正则表达式
import re
pattern = r'\bfoo\b'
text = "foo bar baz foo"
matches = re.findall(pattern, text)
print("Matches:", matches)  # 输出Matches: ['foo', 'foo']
# 使用列表的extend方法
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_a.extend(list_b)
print("Extended List:", list_a)  # 输出Extended List: [1, 2, 3, 4, 5, 6]
# 使用字符串的format方法
name = "Charlie"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # 输出My name is Charlie and I am 30 years old
# 使用列表的pop方法
my_list = [10, 20, 30, 40, 50]
popped_value = my_list.pop()
print("Popped Value:", popped_value)  # 输出Popped Value: 50
print("List after pop:", my_list)  # 输出List after pop: [10, 20, 30, 40]
# 使用字典的get方法
