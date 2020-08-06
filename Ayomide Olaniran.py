def fib(n):
    a = 1
    b = 1
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    else:
        print('0')
        print(a)
        print(b)
        for i in range(n-3):
            total = a + b
            b = a
            a = total
            print(total)
        print()
        return b

ans = int(input("enter a digit: "))
fib(ans)