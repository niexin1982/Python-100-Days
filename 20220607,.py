# -*- coding: utf-8 -*-

from pickle import TRUE


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][2])
# 打印Lisa:
print(L[2][2])



height = 1.75
weight = 80.5

weight = 50
bmi = weight /height **2
print('bmi= ',bmi)
if bmi > 32:
    print('严重肥胖')
elif bmi >= 28 :
    print('肥胖')
elif bmi >= 25 :
    print('过重')
elif bmi >= 18.5 :
    print('正常')
elif bmi < 18.5 :
    print('过轻')

d ={'a':95,'b':80,'c':100}
print(d['a'])




def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))

def mul(*numbers):
    if len(numbers) == 0:
        raise TypeError
    else:
        product = 1
        for x in numbers:
            product = product * x

        return product

 # 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')   

def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(5, 'A', 'B', 'C')

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L) 

print(list(range(100))[1:len(list(range(100)))//2:2])

def findMinAndMax(L):
    if len(L) == 0 :
        return(None,None)
    else:
        min = L[0]
        max = L[0]
        for str in L:
            if str < min:
                min = str
            if str > max :
                max = str  
        return (min , max )

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
