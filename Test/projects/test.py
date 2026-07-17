name = '张三'
age = '24'
gender = '男'

a = 1
# for a in range(6):
#     print('python')
# print('结束')    

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