def es_primo(num1):
    for n in range(2, num1):
        if num1 % n == 0:
            print(num1, "No es primo")
            return False
    print("Es primo")
    return True
print("Introduce tu primer numero y te dire si es primo: ")
es_primo(int(input()))
print("Introduce tu segundo numero y te dire si es primo: ")
es_primo(int(input()))