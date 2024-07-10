numero = int(input("Insira um número:"))

match numero % 2:
    case 0:
        print(f"O número {numero} é par.")
    case 1:
        print(f"O número {numero} é impar.")
    case _:
        print("Inválido.")