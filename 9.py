try:
    quantidade = int(input("Digite a quantidade de numeros: "))
    positivo = 0
    negativo = 0
    zero = 0

    for i in range(quantidade):
        i = int(input("Digite o numero: "))

        if i > 0:
            positivo += 1
        elif i < 0:
            negativo +=1
        else:
            zero +=1

    print(f"positivos: {positivo}")
    print(f"negativo: {negativo}")
    print(f"zero: {zero}")
except:
    print("Deu errado")