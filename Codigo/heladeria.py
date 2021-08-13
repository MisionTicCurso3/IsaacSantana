print("Bienvenido a la heladeria")
print("El helado sencillo vale 1900")
print(" Estos son los toppings que puedes agregar a tu helado:")
print("t2 : El topping de oreo cuesta 1.000")
print("t3 : El topping de KitKat cuesta 1.500.")
print("t4 : El topping de brownie cuesta 2.500.")
print("t5 : El topping de barquillo cuesta 950.")
print("Para elegir los topping utiliza los comandos t1,t2,t3,t4")

Hn =  1900
t2 =  1000
t3 =  1500
t4 = 2500
t5 =  950


topping_1 = input("Que tipo de topping deseas elegir?: ")
if topping_1 == "t2":
    Valor_2 = Hn + t2
    print("su valor con el t2 es", Valor_2)
elif topping_1 == "t3":
    Valor_3 = Hn + t3
    print("su valor con el t3 es", Valor_3)
elif topping_1 == "t4":
    Valor_4 = Hn + t4
    print("su valor con el t4 es", Valor_4)
elif topping_1 == "t5":
    Valor_5 = Hn + t5
    print("su valor con el t5 es", Valor_5 )         
else:
    print("Lo siento no ha elegido los comandos t2 t3 t4 t5")

Valor_2 = Hn + t2
Valor_3 = Hn + t3
Valor_4 = Hn + t4
Valor_5 = Hn + t5

# Pass = input("Desea agregar otro topping? responda (si, no): ")
# if Pass == "si":
topping_2 = input("Que tipo de topping deseas elegir?: ")
if topping_2 == "t2":
    Valor2_1 = t2 + valor_2
    print("su valor con el t2 es",Valor2_1)
elif topping_2 == "t3":
    Valor2_3 = t3 + Valor_3
    print("su valor con el t3 es",Valor2_3 )
elif topping_2 == "t4":
    Valor2_4 = t4 + Valor_4
    print("su valor con el t4 es",Valor2_4)
elif topping_2 == "t5":
    Valor2_5 = t5 + Valor_5
    print("su valor con el t5 es",Valor2_5)
else:
    print("Lo siento no ha elegido los comandos t2 t3 t4 t5")

    




# # topping_2 = input("Eliga su segundo topping: ")
# # if topping_2 == "t3":
# #     valor_2 = Hn + t3
# #     print("su valor con el t3 es ", valor_2)






