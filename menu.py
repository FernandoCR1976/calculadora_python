import calculadora
def menu(a,b):
    while True:
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")

        opcion = input("Seleccione una opcion")
        if opcion == '1':
            print(calculadora.sumar(a,b))
        elif opcion == "2":
            print(calculadora.restar(a,b))
        elif opcion == "3":
            print(calculadora.multiplicar(a,b))
        elif opcion == "4":
            print(calculadora.dividir(a,b))
        elif opcion == "5":
            print("saliendo del programa")
            break
        else:
            print("Ingrese una opcion entre 1 y 5")