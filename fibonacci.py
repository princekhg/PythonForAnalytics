fib = [1, 1]


def generate_fibo():
    n = int(input("Enter total numbers of fibonacci numbers you want to generate"))
    for i in range(2, n):
        c = fib[i-1] + fib[i-2]
        fib.append(c)
    return fib


print(generate_fibo())

