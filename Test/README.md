# Python知识点

## 第一章
    1.逻辑运算符
```py
    //对于and的逻辑运算符，先检查左边，当左边是假时候，那么就直接返回左边，如果是真则返回右边
    print(2-2 and ture)  //输出是0
    print(true and true) //输出是true
```
## 第二章
    1.判断标识符
```py
# python中没有括号把判断后执行的操作围起来，其中代替的标准就是缩进，按照缩进为结束的标志
a = 1
if a < 10:
    print('执行')
print('结束')

if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print('好')
print('结束')# 无缩进结束标志
```
    2.循环
```py
while n > 10：
    print('1')
print('结束')

a = 1
for a in range(6):
    print('python')
    continue # 如果有continue则会跳过print('c')，进入下一次循环
    break # 直接结束循环
    print('c')
print('结束') 
```
## 第三章
    1.函数
```py
    def welcome():
    print('欢迎')

for a in range(7):
    welcome()
```
    2.实参和形参是和C语言一样的

    3.可变参数
```py

# *代表可变位置参数：表示传入不带关键字的参数
# **代表可变关键字参数：表示传入必须要带关键字的参数
    def complex_func(a, b, *args, default_val=10, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"default={default_val}")
    print(f"kwargs={kwargs}")

complex_func(1, 2, 3, 4, 5, default_val=99, x=100, y=200)
# 输出:
# a=1, b=2
# args=(3, 4, 5)
# default=99
# kwargs={'x': 100, 'y': 200}

```
    4.结构体
```py
# student 定义新的结构体类型
    class Student:
# def __init__(self, ...): 就是构造函数
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s1 = Student("Alice", 20, 92.5)   # 创建
print(s1.name)   # 访问，输出 Alice
print(s1.age)    # 20
s1.score = 95.0  # 修改
```
