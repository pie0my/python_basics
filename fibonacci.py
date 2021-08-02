from typing import Optional


def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        a = b
        b = a + b


for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=',')
print("\b")

print("\b")
