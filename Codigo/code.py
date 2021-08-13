print("Se calculara el imc con los siguientes datos")

peso = int(input("Cual es tu peso?: "))
Altura = float(input("Cual es tu altura?: "))

imc = peso/Altura**2

if imc >=0 or imc <= 18.50:
    print("Bajo de peso")
elif imc > 18.50 or imc <= 24.99:
    print("Tu peso es normal")
elif imc >= 25.00:
    print("Sobrepeso")
elif imc >= 30.00:
    print("Peligro de obesidad")
print(imc)