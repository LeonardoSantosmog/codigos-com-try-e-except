try:
    numero = int(input("digite o numero: "))

    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
except:
    print("Deu errado")