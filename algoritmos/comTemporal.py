import time
import sys
sys.setrecursionlimit(3000)

def factorial(n):
    respuesta = 1
    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta


def factorial_r(n):
    if n == 1:
        return 1
    else:
        return (n * factorial_r(n - 1))


if __name__ == '__main__':
    n = 1500

    comienzo2 = time.time()
    factorial(n)
    final2 = time.time()
    print(final2 - comienzo2)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)