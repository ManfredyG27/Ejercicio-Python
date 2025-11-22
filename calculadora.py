def mostrar_menu():
    print("==== Calculadora en Python ====")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            print("Saliendo...")
            break

        if opcion in ["1", "2", "3", "4"]:
            try:
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Entrada inválida. Usa números.")
                continue

            if opcion == "1":
                print("Resultado:", sumar(a, b))
            elif opcion == "2":
                print("Resultado:", restar(a, b))
            elif opcion == "3":
                print("Resultado:", multiplicar(a, b))
            elif opcion == "4":
                print("Resultado:", dividir(a, b))
        else:
            print("Opción no válida.")

        print()  # Línea en blanco para separar

if __name__ == "__main__":
    main()
