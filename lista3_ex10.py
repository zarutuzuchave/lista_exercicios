# 10. Encontre todos os números primos entre 2 e 20.000.
for num in range(2, 20001):
    divisores = 0

    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1

    if divisores == 2:
        primo = num
        print(primo)
