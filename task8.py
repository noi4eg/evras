# Напишите программу, проводящую вычисление n-го числа ряда Фибоначчи. Числа Фибоначчи - элементы числовой последовательности, 
# в которой первые два числа равны 0 и 1, а каждое последующее число равно сумме двух предыдущих чисел.

def fib(n):
    n1 = 0
    n2 = 1
    if 0 == n:
        sum = 0
    elif 1 == n:
        sum = 1
    else:
        for elem in range (1,n):
            sum = n1 + n2
            n1 = n2
            n2 = sum
            
    return sum


def fib_rec(n):
    if n in {0, 1}:
        return n
    return fib_rec(n-1) + fib_rec(n-2)


n = int(input().strip())

print (fib(n))
print (fib_rec(n))


