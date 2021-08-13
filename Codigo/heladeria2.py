print("Bienvenido a la heladeria")
print("El helado sencillo vale 1900")
print(" Estos son los toppings que puedes agregar a tu helado:")
print("t2 : El topping de oreo cuesta 1.000")
print("t3 : El topping de KitKat cuesta 1.500.")
print("t4 : El topping de brownie cuesta 2.500.")
print("t5 : El topping de barquillo cuesta 950.")
print("Para elegir los topping utiliza los comandos t1,t2,t3,t4")

Valor_Final = 0
Hn =  1900
t2 =  1000
t3 =  1500
t4 = 2500
t5 =  950

def funcion1(topping_1):
    if topping_1 == "t2":
        Valor_Final = Hn + t2
        print("su valor con el t2 es", Valor_Final)
    elif topping_1 == "t3":
        Valor_Final = Hn + t3
        print("su valor con el t3 es", Valor_Final)
    elif topping_1 == "t4":
        Valor_Final = Hn + t4
        print("su valor con el t4 es", Valor_Final)
    elif topping_1 == "t5":
         Valor_Final = Hn + t5
         print("su valor con el t5 es", Valor_Final )         
    else:
        print("Lo siento no ha elegido los comandos t2 t3 t4 t5")


topping_1 = input("Que tipo de topping deseas elegir?: ")
funcion1(topping_1)

Pass = input("Desea agregar otro topping? responda (si, no): ")
if Pass == "si":
    topping_2 = input("Que tipo de topping deseas elegir?: ")
    if topping_2 == "t2":
        Valor_Final = t2 + Valor_Final
        print("su valor con el t2 es",Valor_Final)
    elif topping_2 == "t3":
        Valor_Final = t3 + Valor_Final
        print("su valor con el t3 es",Valor_Final)
    elif topping_2 == "t4":
        Valor_Final = t4 + Valor_Final
        print("su valor con el t4 es",Valor_Final)
    elif topping == "t5":
        Valor_Final = t5 + Valor_Final
        print("su valor con el t5 es",Valor_Final)
    else:
        print("Lo siento no ha elegido los comandos t2 t3 t4 t5")
else:
    print("Su helado cuesta", Valor_Final)
