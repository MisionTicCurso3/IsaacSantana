def es_primo(num1,num2):
    for n in range(2, num1):
        if num1 % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True
    for i in range(2, num2):
        if num2 % i == 0:
            print("No es primo", i, "es divisor")
            return False
    print("Es primo")
    return True
print("Introduce dos numeros y te dire si son primos: ")
es_primo(int(input()), int(input()))

