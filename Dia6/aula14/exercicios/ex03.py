algo = input("digite algo")

match algo:
    case "":
        print("string vazia")
    case _:
        print("string não vazia")