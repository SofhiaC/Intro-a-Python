idade = int(input("Insira sua idade:"))

match idade:
    case idade if idade <= 12:
        print("Criança.")
    case idade if 12 < idade <= 18:
        print("Adolescente.")
    case idade if 18 <= idade:
        print("Adulto.")